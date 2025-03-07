# -*- encoding: utf-8 -*-
"""

.. include:: ../README.md
   :start-line: 1

"""
__author__ = 'bibi21000 aka Sébastien GALLET'
__email__ = 'bibi21000@gmail.com'

import os
import sys
import struct
import builtins
import io
import logging

from cofferfile.decorator import reify

__all__ = ["EncryptFile", "Cryptor", "_open_t", "_open_cls"]

READ = 'rb'
WRITE = 'wb'
APPEND = 'ab'
EXCLUSIVE = 'xb'

# Changing these constants will break current format !!!
# what size for meta information ?
# For example, AES GCM nonce, with a length of 12 bytes
# and 4 bytes for chunck length
# 32 bytes seem a reasonable value
META_CHUNK = 4
META_RESERV = 7
META_SIZE = META_RESERV * META_CHUNK + META_CHUNK

# These one are default for class instanciation
BUFFER_SIZE = 1024 * 64
CHUNK_SIZE = BUFFER_SIZE - META_SIZE
WRITE_BUFFER_SIZE = 5 * BUFFER_SIZE

log = logging.getLogger('cofferfile')

if hasattr(io, "text_encoding"):
    text_encoding = io.text_encoding
else:
    # For python 3.9
    def text_encoding(encoding) -> str:
        if encoding is not None:
            return encoding
        if sys.flags.utf8_mode:
            return "utf-8"
        import locale
        _, encoding=locale.getlocale()
        return encoding

class BaseStream(io.BufferedIOBase):
    """Mode-checking helper functions."""

    def _check_not_closed(self):
        if self.closed:
            raise ValueError("I/O operation on closed file")

    def _check_can_read(self):
        if not self.readable():
            raise io.UnsupportedOperation("File not open for reading")

    def _check_can_write(self):
        if not self.writable():
            raise io.UnsupportedOperation("File not open for writing")

    # ~ def _check_can_seek(self):
        # ~ if not self.readable():
            # ~ raise io.UnsupportedOperation("Seeking is only supported "
              # ~ "on files open for reading")
        # ~ if not self.seekable():
            # ~ raise io.UnsupportedOperation("The underlying file object "
              # ~ "does not support seeking")


class DecryptReader(io.BufferedIOBase):
    """Adapts the decryptor API to a RawIOBase reader API"""

    def __init__(self, fp, decrypt_factory, buffer_size=BUFFER_SIZE,
            trailing_error=(), **decrypt_args):
        """"""
        self._fp = fp
        self.buffer_size = buffer_size
        self._eof = False
        self._pos = 0  # Current offset in decrypted stream

        # Set to size of decrypted stream once it is known, for SEEK_END
        self._size = -1

        # Save the decryptor factory and arguments.
        # If the file contains multiple compressed streams, each
        # stream will need a separate decryptor object. A new decryptor
        # object is also needed when implementing a backwards seek().
        self._decrypt_factory = decrypt_factory
        self._decrypt_args = decrypt_args
        self._decryptor = self._decrypt_factory(**self._decrypt_args)

        # Exception class to catch from decryptor signifying invalid
        # trailing data to ignore
        self._trailing_error = trailing_error
        self._marks = 0
        # ~ self._old_data = None

    def close(self):
        """"""
        self._decryptor = None
        return super().close()

    def seekable(self):
        """"""
        return self._fp.seekable()

    def readable(self):
        """"""
        return self._fp.readable()

    def readinto(self, b):
        """"""
        # ~ print(type(b))
        with memoryview(b) as view, view.cast("B") as byte_view:
            data = self.read(len(byte_view))
            # ~ if self._old_data == data:
                # ~ log.warning('duplicate')
            # ~ self._old_data = data
            # ~ log.debug('readinto : %s, byte_view size %s mark %s' %
                # ~ (len(data), len(byte_view), self._marks))
            # ~ log.debug('readinto : %s' %(byte_view))
            byte_view[:len(data)] = data
        return len(data)

    def read(self, size=-1):
        """"""
        if size < 0:
            return self.readall()
        if not size or self._eof:
            return b""
        data = None  # Default if EOF is encountered
        # Depending on the input data, our call to the decryptor may not
        # return any data. In this case, try again after reading another block.
        while True:
            if self._decryptor.eof:
                # ~ log.debug('here self._decryptor.eof %s'%size)
                rawblock = (self._decryptor.unused_data or
                    self._fp.read(self.buffer_size))
                if not rawblock:
                    break
                # Continue to next stream.
                self._decryptor = self._decrypt_factory(**self._decrypt_args)
                try:
                    data = self._decryptor.decrypt(rawblock, size)
                    self._marks += 1
                except self._trailing_error:
                    # Trailing data isn't a valid compressed stream; ignore it.
                    self._marks = 0
                    break
            else:
                # ~ log.debug('here %s'%size)
                if self._decryptor.needs_input:
                    rawblock = self._fp.read(self.buffer_size)
                    if not rawblock:
                        raise EOFError("Compressed file ended before the "
                                       "end-of-stream marker was reached")
                else:
                    rawblock = b""
                # ~ log.debug('rawblock %s'%len(rawblock))
                data = self._decryptor.decrypt(rawblock, size)
                self._marks += 1
            # ~ log.debug("read : data %s, len data %s, unused_data %s, unsent_data %s" %
            # ~ (type(data), len(data) if data is not None else 0, len(self._decryptor.unused_data) if self._decryptor.unused_data is not None else 0, len(self._decryptor.unsent_data)))
            if data:
                break
        if not data:
            self._eof = True
            self._size = self._pos
            return b""
        self._pos += len(data)
        # ~ log.debug("read : data %s, len data %s" % (type(data), len(data)))
        return data

    def readall(self):
        """"""
        chunks = []
        # sys.maxsize means the max length of output buffer is unlimited,
        # so that the whole input buffer can be decrypted within one
        # .decrypt() call.
        while data := self.read(sys.maxsize):
            chunks.append(data)

        return b"".join(chunks)

    # Rewind the file to the beginning of the data stream.
    def rewind(self):
        """"""
        self._fp.seek(0)
        self._eof = False
        self._pos = 0
        self._decryptor = self._decrypt_factory(**self._decrypt_args)

    def seek(self, offset, whence=io.SEEK_SET):
        """"""
        # Recalculate offset as an absolute file position.
        if whence == io.SEEK_SET:
            pass
        elif whence == io.SEEK_CUR:
            offset = self._pos + offset
        elif whence == io.SEEK_END:
            # Seeking relative to EOF - we need to know the file's size.
            if self._size < 0:
                while self.read(io.DEFAULT_BUFFER_SIZE):
                    pass
            offset = self._size + offset
        else:
            raise ValueError("Invalid value for whence: {}".format(whence))

        # Make it so that offset is the number of bytes to skip forward.
        if offset < self._pos:
            self.rewind()
        else:
            offset -= self._pos

        # Read and discard data until we reach the desired position.
        while offset > 0:
            data = self.read(min(io.DEFAULT_BUFFER_SIZE, offset))
            if not data:
                break
            offset -= len(data)

        return self._pos

    def tell(self):
        """Return the current file position."""
        return self._pos


class Cryptor():

    def __init__(self, chunk_size=CHUNK_SIZE):
        """"""
        self.chunk_size = chunk_size
        self._marks = 0
        self.eof = False
        self.needs_input = True
        self.unused_data = None
        self.unsent_data = b''
        self.pos = 0
        log.debug("Cryptor initialized")

    @classmethod
    @reify
    def _imp_hashlib(cls):
        """Lazy loader for hashlib"""
        import importlib
        return importlib.import_module('hashlib')

    @classmethod
    @reify
    def _imp_secrets(cls):
        """Lazy loader for secrets
        """
        import importlib
        return importlib.import_module('secrets')

    @classmethod
    def derive(self, password, salt=None, key_len=32, N=2 ** 14, r=8, p=1, maxmem=0):
        """Derive a key from password (experimental)
        """
        if salt is None:
            salt = self._imp_secrets.token_bytes(32)
        if isinstance(password, str):
            password = password.encode()
        return salt, self._imp_hashlib.scrypt(password, salt=salt, n=N, r=r, p=p,
            dklen=key_len, maxmem=maxmem)

    def _encrypt(self, chunk):
        return chunk

    def encode_meta(self, chunk_size):
        """Always return 32 (META_SIZE) bytes string
        """
        ret = b''
        ret += struct.pack('<I', chunk_size)
        # We add blank data for later
        for i in range(META_RESERV):
            ret += struct.pack('<I', 0)
        return ret

    def decode_meta(self, data):
        """Decode metadata from data and return length of data.
        -1 no data to decode
        -2 means not enough data
        """
        meta = data[:META_SIZE]
        size_chunk = meta[:META_CHUNK]
        if len(size_chunk) == 0:
            return -1
        if len(meta) < META_SIZE:
            return -2
        size = struct.unpack('<I', size_chunk)[0]
        return size

    def crypt(self, data):
        """"""
        ret = b''
        beg = 0
        while True:
            chunk = data[beg:beg + self.chunk_size]
            if len(chunk) == 0:
                break
            enc = self._encrypt(chunk)
            self._marks += 1
            ret += self.encode_meta(len(enc))
            ret += enc
            if len(chunk) < self.chunk_size:
                break
            beg += self.chunk_size

        # ~ log.debug("CofferEncryptor.compress : len ret %s, chunk size %s, marks %s" %
            # ~ (len(ret), self.chunk_size, self._marks))
        return ret

    def flush(self):
        """"""
        return b''

    def _decrypt(self, chunk):
        """"""
        return chunk

    def decrypt(self, data, size=-1):
        """"""
        beg = 0
        ret = b""
        size_data = None
        # ~ len_data = len(data)
        self.eof = False
        self.needs_input = True
        # ~ log.debug("len data %s dat %s, size %s" % (len(data), data[:15], size))
        if self.unused_data is not None:
            # ~ log.debug("len self.unused_data %s" % (len(self.unused_data)))
            data = self.unused_data + data
            self.unused_data = None
        while True:
            size_data = self.decode_meta(data[beg:])
            if size_data == -1:
                # ~ log.debug('len %s'%len(size_struct))
                self.needs_input = False
                self.eof = True
                break
            if size_data == -2:
                self.unused_data = data[beg:]
                break
            chunk = data[beg + META_SIZE:beg + META_SIZE + size_data]

            if len(chunk) < size_data:
                self.unused_data = data[beg:]
                break
            ret += self._decrypt(chunk)
            beg += size_data + META_SIZE

        ret = self.unsent_data + ret
        if self.eof is True and len(ret) > 0:
            self.eof = False
        if self.eof is True and len(ret) == 0:
            self.needs_input = False
            return None
        if size > 0 and len(ret) > size:
            self.unsent_data = ret[size:]
            ret = ret[:size]
        else:
            self.unsent_data = b''
        return ret


class _WriteBufferStream(io.RawIOBase):
    """Minimal object to pass WriteBuffer flushes into CofferFile"""
    def __init__(self, fernet_file):
        """"""
        self.fernet_file = fernet_file

    def write(self, data):
        """"""
        return self.fernet_file._write_raw(data)

    def seekable(self):
        """"""
        return False

    def writable(self):
        """"""
        return True


class EncryptFile(BaseStream):
    """The CofferFile class simulates most of the methods of a file object with
    the exception of the truncate() method.

    This class only supports opening files in binary mode.

    `cofferfile.decorator`
    `cofferfile.aes`

    """

    myfileobj = None
    """Overridden with internal file object to be closed, if only a filename
    is passed in"""

    def __init__(self, filename=None, mode=None, fileobj=None,
            chunk_size=CHUNK_SIZE, write_buffer_size=WRITE_BUFFER_SIZE,
            cryptor=None, **cryptor_args):
        """Constructor for the CofferFile class.

        At least one of fileobj and filename must be given a
        non-trivial value.

        The new class instance is based on fileobj, which can be a regular
        file, an io.BytesIO object, or any other object which simulates a file.
        It defaults to None, in which case filename is opened to provide
        a file object.

        When fileobj is not None, the filename argument is only used to be
        included in the gzip file header, which may include the original
        filename of the uncompressed file.  It defaults to the filename of
        fileobj, if discernible; otherwise, it defaults to the empty string,
        and in this case the original filename is not included in the header.

        The mode argument can be any of 'r', 'rb', 'a', 'ab', 'w', 'wb', 'x', or
        'xb' depending on whether the file will be read or written.  The default
        is the mode of fileobj if discernible; otherwise, the default is 'rb'.
        A mode of 'r' is equivalent to one of 'rb', and similarly for 'w' and
        'wb', 'a' and 'ab', and 'x' and 'xb'.

        The fernet_key argument is the Coffer key used to crypt/decrypt data.

        Encryption is done by chunks to reduce memory footprint. The default
        chunk_size is 64KB.
        """
        self.chunk_size = chunk_size
        if self.chunk_size != CHUNK_SIZE and write_buffer_size == WRITE_BUFFER_SIZE:
            write_buffer_size = 5 * (self.chunk_size + META_SIZE)
        if mode and ('t' in mode or 'U' in mode):
            raise ValueError("Invalid mode: {!r}".format(mode))
        if mode and 'b' not in mode:
            mode += 'b'
        if filename is None:
            filename = getattr(fileobj, 'name', '')
            if not isinstance(filename, (str, bytes)):
                filename = ''
        else:
            filename = os.fspath(filename)
        if fileobj is None:
            fileobj = self.myfileobj = builtins.open(filename, mode or 'rb')
        else:
            self.myfileobj = fileobj
        if mode is None:
            mode = getattr(fileobj, 'mode', 'rb')

        cryptor_cls = self.cryptor_factory(cryptor)

        if mode.startswith('r'):
            self.mode = READ
            raw = DecryptReader(self.myfileobj,
                cryptor_cls, trailing_error=OSError, **cryptor_args)
            self._buffer = io.BufferedReader(raw)

        elif mode.startswith(('w', 'a', 'x')):
            self.mode = WRITE
            self._init_write(filename)
            self.crypt = cryptor_cls(chunk_size=self.chunk_size, **cryptor_args)
            self._buffer_size = write_buffer_size
            self._buffer = io.BufferedWriter(_WriteBufferStream(self),
                                             buffer_size=self._buffer_size)

        else:
            raise ValueError("Invalid mode: {!r}".format(mode))

        self.fileobj = fileobj
        # ~ log.debug("Init CofferFile")

    # ~ @property
    # ~ def mtime(self):
        # ~ """Last modification time read from stream, or None"""
        # ~ return self._buffer.raw._last_mtime

    def __repr__(self):
        """"""
        s = repr(self.myfileobj)
        return '<EncryptFile ' + s[1:-1] + ' ' + hex(id(self)) + '>'

    @classmethod
    @reify
    def _imp_metadata(cls):
        """Lazy loader for metadata"""
        import importlib
        if sys.version_info < (3, 10):
            return importlib.import_module('importlib_metadata')
        else:
            return importlib.import_module('importlib.metadata')

    @classmethod
    def cryptor_factory(self, name=None):
        """"""
        if name is None:
            return self._imp_metadata.entry_points(group='cofferfile.cryptor')
        else:
            crpt = self._imp_metadata.entry_points(group='cofferfile.cryptor', name=name)
            if len(crpt) != 1:
                raise IndexError("Problem loading %s : found %s matches"%(name, len(crpt)))
            return tuple(crpt)[0].load()

    def _init_write(self, filename):
        self.name = filename
        self.size = 0
        self.writebuf = []
        self.bufsize = 0
        self.offset = 0  # Current file offset for seek(), tell(), etc

    def tell(self):
        """Return the current file position."""
        self._check_not_closed()
        self._buffer.flush()
        return super().tell()

    def write(self, data):
        """Write a byte string to the file.

        Returns the number of uncompressed bytes written, which is
        always the length of data in bytes. Note that due to buffering,
        the file on disk may not reflect the data written until close()
        is called.
        """
        self._check_can_write()
        return self._buffer.write(data)

    def _write_raw(self, data):
        # Called by our self._buffer underlying WriteBufferStream.
        if isinstance(data, (bytes, bytearray)):
            length = len(data)
        else:
            # ~ print(type(data))
            # accept any data that supports the buffer protocol
            data = memoryview(data)
            length = data.nbytes
            data = data.tobytes()

        if length > 0:
            self.fileobj.write(self.crypt.crypt(data))
            self.size += length
            self.offset += length

        return length

    def read(self, size=-1):
        """Read up to size uncompressed bytes from the file.

        If size is negative or omitted, read until EOF is reached.
        Returns b'' if the file is already at EOF.
        """
        self._check_can_read()
        return self._buffer.read(size)

    def read1(self, size=-1):
        """Read up to size uncompressed bytes, while trying to avoid
        making multiple reads from the underlying stream. Reads up to a
        buffer's worth of data if size is negative.

        Returns b'' if the file is at EOF.
        """
        self._check_can_read()
        if size < 0:
            size = io.DEFAULT_BUFFER_SIZE
        return self._buffer.read1(size)

    def peek(self, n):
        """Return buffered data without advancing the file position.

        Always returns at least one byte of data, unless at EOF.
        The exact number of bytes returned is unspecified.
        """
        self._check_can_read()
        return self._buffer.peek(n)

    @property
    def closed(self):
        """True if this file is closed."""
        return self.fileobj is None

    def close(self):
        """Flush and close the file.

        May be called more than once without error. Once the file is
        closed, any other operation on it will raise a ValueError.
        """
        fileobj = self.fileobj
        if fileobj is None or self._buffer.closed:
            return
        try:
            if self.mode == WRITE:
                self._buffer.flush()
            elif self.mode == READ:
                self._buffer.close()
        finally:
            self.fileobj = None
            myfileobj = self.myfileobj
            if myfileobj:
                self.myfileobj = None
                myfileobj.close()

    def flush(self):
        """Flush buffers to disk."""
        self._check_not_closed()
        if self.mode == WRITE:
            self._buffer.flush()
            # Ensure the compressor's buffer is flushed
            self.fileobj.write(self.crypt.flush())
            self.fileobj.flush()

    def fileno(self):
        """Invoke the underlying file object's fileno() method.

        This will raise AttributeError if the underlying file object
        doesn't support fileno().
        """
        self._check_not_closed()
        return self.fileobj.fileno()

    def rewind(self):
        '''Return the uncompressed stream file position indicator to the
        beginning of the file
        '''
        if self.mode != READ:
            raise io.UnsupportedOperation("Can't rewind in write mode")
        self._buffer.seek(0)

    def readable(self):
        """Return whether the file was opened for reading."""
        self._check_not_closed()
        return self.mode == READ

    def writable(self):
        """Return whether the file was opened for writing."""
        self._check_not_closed()
        return self.mode == WRITE

    def seekable(self):
        """Return whether the file supports seeking. (experimental)"""
        return self.readable() and self._buffer.seekable()

    def seek(self, offset, whence=io.SEEK_SET):
        """Change the file position. (experimental)

        The new position is specified by offset, relative to the
        position indicated by whence. Values for whence are:

            0: start of stream (default); offset must not be negative
            1: current stream position
            2: end of stream; offset must not be positive

        Returns the new file position.

        Note that seeking is emulated, so depending on the parameters,
        this operation may be extremely slow.
        """
        # ~ self._check_can_seek()
        if self.mode == WRITE:
            self._check_not_closed()
            # Flush buffer to ensure validity of self.offset
            self._buffer.flush()
            if whence != io.SEEK_SET:
                if whence == io.SEEK_CUR:
                    offset = self.offset + offset
                else:
                    raise io.UnsupportedOperation('Seek from end not supported')
            if offset < self.offset:
                raise io.UnsupportedOperation('Negative seek in write mode not supported')
            count = offset - self.offset
            chunk = b'\0' * self._buffer_size
            for i in range(count // self._buffer_size):
                self.write(chunk)
            self.write(b'\0' * (count % self._buffer_size))

        elif self.mode == READ:
            self._check_not_closed()
            return self._buffer.seek(offset, whence)

        return self.offset

    def readline(self, size=-1):
        """Read a line of uncompressed bytes from the file.

        The terminating newline (if present) is retained. If size is
        non-negative, no more than size bytes will be read (in which
        case the line may be incomplete). Returns b'' if already at EOF.
        """
        self._check_not_closed()
        return self._buffer.readline(size)


def _open_t(filename, mode="rb",
         encoding=None, errors=None, newline=None,
         chunk_size=CHUNK_SIZE,
         cryptor=None, **cryptor_args):
    """Open a Fernet file in binary or text mode.

    The filename argument can be an actual filename (a str or bytes object), or
    an existing file object to read from or write to.

    The mode argument can be "r", "rb", "w", "wb", "x", "xb", "a" or "ab" for
    binary mode, or "rt", "wt", "xt" or "at" for text mode. The default mode is
    "rb".

    For binary mode, this function is equivalent to the FernetFile constructor:
    FernetFile(filename, mode, fernet_key). In this case, the encoding, errors
    and newline arguments must not be provided.

    For text mode, a FernetFile object is created, and wrapped in an
    io.TextIOWrapper instance with the specified encoding, error handling
    behavior, and line ending(s).

    Encryption is done by chunks to reduce memory footprint. The default
    chunk_size is 64KB.
    """
    if "t" in mode:
        if "b" in mode:
            raise ValueError("Invalid mode: %r" % (mode,))
    else:
        if encoding is not None:
            raise ValueError("Argument 'encoding' not supported in binary mode")
        if errors is not None:
            raise ValueError("Argument 'errors' not supported in binary mode")
        if newline is not None:
            raise ValueError("Argument 'newline' not supported in binary mode")

    frnt_mode = mode.replace("t", "")
    if isinstance(filename, (str, bytes, os.PathLike)):
        binary_file = EncryptFile(filename, mode=frnt_mode, chunk_size=chunk_size, cryptor=cryptor, **cryptor_args)
    elif hasattr(filename, "read") or hasattr(filename, "write"):
        binary_file = EncryptFile(None, mode=frnt_mode, fileobj=filename, chunk_size=chunk_size, cryptor=cryptor, **cryptor_args)
    else:
        raise TypeError("filename must be a str or bytes object, or a file")

    if "t" in mode:
        encoding = text_encoding(encoding)
        return io.TextIOWrapper(binary_file, encoding, errors, newline)
    else:
        return binary_file


def _open_cls(filename, mode="r",
         encoding=None, errors=None, newline=None,
         chunk_size=CHUNK_SIZE,
         coffer_cls = None,
         level_or_option=None, zstd_dict=None,
         cryptor=None, **cryptor_args):
    """Open a Coffer file in binary or text mode.

    The filename argument can be an actual filename (a str or bytes object), or
    an existing file object to read from or write to.

    The mode argument can be "r", "rb", "w", "wb", "x", "xb", "a" or "ab" for
    binary mode. The default mode is "rb".

    For binary mode, this function is equivalent to the CofferFile constructor:
    CofferFile(filename, mode, cryptor=cryptor, **cryptor_args).

    Encryption is done by chunks to reduce memory footprint. The default
    chunk_size is 64KB.
    """
    if "t" in mode:
        if "b" in mode:
            raise ValueError("Invalid mode: %r" % (mode,))
    else:
        if encoding is not None:
            raise ValueError("Argument 'encoding' not supported in binary mode")
        if errors is not None:
            raise ValueError("Argument 'errors' not supported in binary mode")
        if newline is not None:
            raise ValueError("Argument 'newline' not supported in binary mode")

    frnt_mode = mode.replace("t", "")
    if isinstance(filename, (str, bytes, os.PathLike)):
        binary_file = coffer_cls(filename, mode=frnt_mode, fileobj=None, chunk_size=chunk_size,
            level_or_option=level_or_option, zstd_dict=zstd_dict,
            cryptor=cryptor, **cryptor_args)
    elif hasattr(filename, "read") or hasattr(filename, "write"):
        binary_file = coffer_cls(None, mode=frnt_mode, fileobj=filename, chunk_size=chunk_size,
            level_or_option=level_or_option, zstd_dict=zstd_dict,
            cryptor=cryptor, **cryptor_args)
    else:
        raise TypeError("filename must be a str or bytes object, or a file")

    if "t" in mode:
        encoding = text_encoding(encoding)
        return io.TextIOWrapper(binary_file, encoding, errors, newline)
    else:
        return binary_file

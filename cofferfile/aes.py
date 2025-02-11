# -*- encoding: utf-8 -*-
""" AES encryption (experimental)
"""
__author__ = 'bibi21000 aka Sébastien GALLET'
__email__ = 'bibi21000@gmail.com'

from . import EncryptFile, Cryptor
from . import WRITE_BUFFER_SIZE, CHUNK_SIZE, READ, WRITE, APPEND, EXCLUSIVE # noqa F401
from .decorator import reify

class AesCryptor(Cryptor):

    @reify
    def _imp_Crypto_Cipher_AES(cls):
        """Lazy loader for Crypto.Cipher"""
        import importlib
        return importlib.import_module('Crypto.Cipher.AES')

    def __init__(self, key=None, iv=None, **kwargs):
        super().__init__(**kwargs)
        if key is None or iv is None:
            raise ValueError("Invalid key/iv: {!r}/{!r}".format(key, iv))
        self.cipher = self._imp_Crypto_Cipher_AES.new(key, self._imp_Crypto_Cipher_AES.MODE_CFB, iv)

    def _decrypt(self, chunk):
        return self.cipher.decrypt(chunk)

    def _encrypt(self, chunk):
        return self.cipher.encrypt(chunk)

class AesFile(EncryptFile):

    def __init__(self, filename=None, mode=None, fileobj=None,
            chunk_size=CHUNK_SIZE, write_buffer_size=WRITE_BUFFER_SIZE,
            key=None, iv=None
        ):
        """Constructor for the AesFile class.

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

        The fernet_key argument is the Fernet key used to crypt/decrypt data.

        Encryption is done by chunks to reduce memory footprint. The default
        chunk_size is 64KB.
        """
        super().__init__(filename=filename, mode=mode, fileobj=fileobj,
            chunk_size=chunk_size, write_buffer_size=write_buffer_size,
            cryptor='aes', key=key, iv=iv)

    def __repr__(self):
        s = repr(self.myfileobj)
        return '<AesFile ' + s[1:-1] + ' ' + hex(id(self)) + '>'

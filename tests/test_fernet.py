# -*- encoding: utf-8 -*-
"""Test module

"""
import os
from random import randbytes
import io

from cryptography.fernet import Fernet, InvalidToken

import cofferfile
import fernetfile

import pytest
from .conftest import DummyFile

@pytest.mark.parametrize("buff_size, file_size",
    [
        (1024 * 1, 1024 * 10), (1024 * 1, 1024 * 10 + 4), (1024 * 1, 1024 * 10 + 5),
        (1024 * 10, 1024 * 10), (1024 * 10, 1024 * 10 + 7), (1024 * 10, 1024 * 10 + 3),
        (1024 * 100, 1024 * 10), (1024 * 100, 1024 * 10 + 9), (1024 * 100, 1024 * 10 + 11),
    ])
def test_buffer(random_path, random_name, buff_size, file_size):
    fernetfile.BUFFER_SIZE = buff_size
    key = Fernet.generate_key()
    data = randbytes(file_size)
    dataf = os.path.join(random_path, random_name)
    with fernetfile.open(dataf, mode='wb', fernet_key=key) as ff:
        ff.write(data)
    with open(dataf, "rb") as ff:
        datar = ff.read()
    assert data != datar
    with fernetfile.open(dataf, "rb", fernet_key=key) as ff:
        datar = ff.read()
    fernetfile.BUFFER_SIZE = 1024 * 10
    assert data == datar

def test_encoding(random_path, random_name):
    key = Fernet.generate_key()
    datal = ["Ceci est un texte avec des accents : éè","avec plusieurs","lignes"]
    data = "\n".join(datal)
    dataf = os.path.join(random_path, '%s_encoding.frnt'%random_name)

    with fernetfile.open(dataf, mode='wt', fernet_key=key, encoding="utf-8") as ff:
        ff.write(data)

    with pytest.raises(ValueError):
        with open(dataf, "r", encoding="utf-8") as ff:
            datar = ff.read()
        assert data != datar

    with fernetfile.open(dataf, "rt", fernet_key=key, encoding="utf-8") as ff:
        datar = ff.read()
    assert data == datar

    with fernetfile.open(dataf, "rt", fernet_key=key, encoding="utf-8") as ff:
        datar = ff.read()
    assert data == datar

    with fernetfile.open(dataf, "rt", fernet_key=key, encoding="utf-8") as ff:
        datar = ff.readline()
        assert datal[0] + '\n' == datar
        datar = ff.readline()
        assert datal[1] + '\n' == datar
        datar = ff.readline()
        assert datal[2] == datar

    datal = ["Ceci est un texte avec des accents : éè","avec plusieurs","lignes"]
    dataf = os.path.join(random_path, '%s_encoding2.frnt'%random_name)

    with fernetfile.open(dataf, mode='wt', fernet_key=key, encoding="utf-8") as ff:
        ff.writelines(data)

    with fernetfile.open(dataf, "rt", fernet_key=key, encoding="utf-8") as ff:
        datar = ff.readlines()

    assert datal[0] + '\n' == datar[0]
    assert datal[1] + '\n' == datar[1]
    assert datal[2] == datar[2]

def test_seek(random_path, random_name):
    key = Fernet.generate_key()
    data = randbytes(1784) + b'0111110' + randbytes(3594) + b'0100010' + randbytes(2145)
    dataf = os.path.join(random_path, 'test_seek_%s.frnt'%random_name)

    with fernetfile.open(dataf, mode='wb', fernet_key=key) as ff:
        assert ff.fileno() is not None
        ff.write(data)
        assert ff.writable()
        assert not ff.readable()
        with pytest.raises(OSError):
            ff.rewind()
        with pytest.raises(OSError):
            ff.seek(0, whence=io.SEEK_SET)
        ff.seek(0, whence=io.SEEK_CUR)

    with fernetfile.open(dataf, "rb", fernet_key=key) as ff:
        assert ff.fileno() is not None
        assert ff.readable()
        assert not ff.writable()
        datar = ff.read()
        assert data == datar
        ff.rewind()
        # ~ assert ff.offset == 0
        datar = ff.read()
        assert data == datar
        ff.seek(1784, whence=io.SEEK_SET)
        datar = ff.read(size=7)
        assert b'0111110' == datar[:7]
        ff.seek(3594, whence=io.SEEK_CUR)
        datar = ff.read()
        assert b'0100010' == datar[:7]

    with open(dataf, "rb") as fp:
        with fernetfile.open(fp, "rb", fernet_key=key) as ff:
            datar = ff.read()
            assert data == datar
            ff.rewind()
            # ~ assert ff.offset == 0
            datar = ff.read()
            assert data == datar
            ff.seek(1784, whence=io.SEEK_SET)
            datar = ff.read(size=7)
            assert b'0111110' == datar[:7]

    with fernetfile.open(dataf, "rb", fernet_key=key) as ff:
        ff.seek(-(2145+7), whence=io.SEEK_END)
        datar = ff.read(7)
        assert b'0100010' == datar

def test_reader(random_path, random_name):
    key = Fernet.generate_key()
    data = randbytes(1784) + b'0111110' + randbytes(3594) + b'0100010' + randbytes(2145)
    dataf = os.path.join(random_path, 'test_reader_%s.frnt'%random_name)

    with fernetfile.open(dataf, mode='wb', fernet_key=key) as ff:
        assert ff.fileno() is not None
        ff.write(data)
        assert ff.writable()
        assert not ff.readable()
        with pytest.raises(OSError):
            ff.rewind()
        with pytest.raises(ValueError):
            ff.seek(-1, whence=io.SEEK_END)
        with pytest.raises(OSError):
            ff.seek(-1)

    with open(dataf, "rb") as fdata:
        with fernetfile.open(fdata, "rb", fernet_key=key) as ff:
            datar = ff.read()
        assert data == datar

    with open(dataf, "rb") as ff:
        with cofferfile.DecryptReader(ff, fernetfile.FernetCryptor, fernet_key=key) as fp:
            assert fp.readable()
            assert not fp.writable()
            datar = fp.read()
            assert data == datar
            fp.rewind()
            datar = fp.read(1784)
            datar = fp.read(7)
            assert b'0111110' == datar
            fp.seek(-7, whence=io.SEEK_CUR)
            datar = fp.read(7)
            assert b'0111110' == datar
            fp.seek(-7, whence=io.SEEK_CUR)
            assert fp.tell() == 1784
            datar = fp.read(7)
            assert b'0111110' == datar
            fp.seek(0, whence=io.SEEK_END)
            fp.seek(-(2145+7), whence=io.SEEK_END)
            datar = fp.read(7)
            assert b'0100010' == datar
            with pytest.raises(ValueError):
                fp.seek(0, 999999)

def test_bad_mode(random_path, random_name):
    key = Fernet.generate_key()
    data = randbytes(128)
    dataf = os.path.join(random_path, 'test_bad_mode_%s.frnt'%random_name)

    print(repr(fernetfile.FernetFile))

    with pytest.raises(ValueError):
        with fernetfile.FernetFile(dataf, mode='wbt', fernet_key=key) as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with fernetfile.FernetFile(dataf, mode='zzz', fernet_key=key) as ff:
            ff.write(data)

    with pytest.raises(FileNotFoundError):
        with fernetfile.FernetFile(None, mode='wb', fernet_key=key) as ff:
            ff.write(data)

    with pytest.raises(FileNotFoundError):
        with fernetfile.FernetFile(dataf, fernet_key=key) as ff:
            data = ff.read()

    with pytest.raises(ValueError):
        with fernetfile.open(dataf, mode='wbt', fernet_key=key) as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with fernetfile.open(dataf, mode='wb', fernet_key=key, encoding='utf-8') as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with fernetfile.open(dataf, mode='wb', fernet_key=key, errors=True) as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with fernetfile.open(dataf, mode='wb', fernet_key=key, newline='\n') as ff:
            ff.write(data)

    with pytest.raises(TypeError):
        with fernetfile.open(None, mode='wb', fernet_key=key) as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with fernetfile.open(dataf, mode='wb', fernet_key=None) as ff:
            ff.write(data)

    with pytest.raises(TypeError):
        with fernetfile.FernetFile(1, mode='wb', fernet_key=None) as ff:
            ff.write(data)

def test_fernetfile(random_path, random_name):
    key = Fernet.generate_key()
    data = randbytes(128)
    dataf = os.path.join(random_path, 'test_repr_%s.frnt'%random_name)
    with fernetfile.FernetFile(dataf, mode='wb', fernet_key=key) as ff:
        ff.write(data)
        assert ff.seekable() is False
        assert repr(ff).startswith("<FernetFile ")
        with pytest.raises(OSError):
            data = ff.read()
        with pytest.raises(OSError):
            data = ff.read1()
        with pytest.raises(OSError):
            data = ff.peek(1)
        ff.fileobj = None
        with pytest.raises(ValueError):
            ff.write(b'rrrrrrrr')
        with pytest.raises(ValueError):
            ff.seekable()

    with fernetfile.FernetFile(dataf, mode='wb', fernet_key=key) as ff:
        ff.write(data)

    with fernetfile.FernetFile(dataf, mode='rb', fernet_key=key) as ff:
        fpp = ff
        with pytest.raises(OSError):
            ff.write(b'rrrrrrrr')
        ff.seek(-1)
        assert ff.tell() == 0
        assert ff.seekable() is True

    with fernetfile.FernetFile(dataf, mode='rb', fernet_key=key) as ff:
        fpp = ff
        with pytest.raises(OSError):
            ff.write(b'rrrrrrrr')
        ff.seek(-1)

    with pytest.raises(ValueError):
        fpp.write(b'rrrrrrrr')
    fpp.close()

    with pytest.raises(ValueError):
        with fernetfile.FernetFile(dataf, mode='fff', fileobj="fake", fernet_key=key) as ff:
            data = ff.read()

def test_peek(random_path, random_name):
    key = Fernet.generate_key()
    data = b'azazazazazazaz\n'
    dataf = os.path.join(random_path, 'test_peek_%s.frnt'%random_name)
    with fernetfile.FernetFile(dataf, mode='wb', fernet_key=key) as ff:
        ff.write(data)

    with fernetfile.FernetFile(dataf, mode='wb', fernet_key=key) as ff:
        ff.write(data)

    with fernetfile.FernetFile(dataf, mode='rb', fernet_key=key) as ff:
        datar = ff.read1()
        assert datar == data

    with fernetfile.FernetFile(dataf, mode='rb', fernet_key=key) as ff:
        datar = ff.read1(1)
        assert datar == b'a'

    with fernetfile.FernetFile(dataf, mode='rb', fernet_key=key) as ff:
        datar = ff.readline()
        assert datar == data

    with fernetfile.FernetFile(dataf, mode='rb', fernet_key=key) as ff:
        data = ff.peek(128)
        assert datar == data

def test_files_encrypt(random_path, random_name):

    key = Fernet.generate_key()

    datafsrc = os.path.join(random_path, 'test_%s.dat'%random_name)
    dataftgt = os.path.join(random_path, 'test_%s.dtc'%random_name)
    datafdec = os.path.join(random_path, 'test_%s.dec'%random_name)

    with open(datafsrc, 'wb') as f:
        for i in range(1024):
            f.write(randbytes(1024 * 5))

    with open(datafsrc, 'rb') as fin, fernetfile.open(dataftgt, mode='wb', fernet_key=key) as fout:
        while True:
            data = fin.read(7777)
            if not data:
                break
            fout.write(data)

    with fernetfile.open(dataftgt, mode='rb', fernet_key=key) as fin, open(datafdec, 'wb') as fout :
        while True:
            data = fin.read(8888)
            if not data:
                break
            fout.write(data)

    with open(datafsrc, 'rb') as f1, open(datafdec, 'rb') as f2:
        assert f1.read() == f2.read()

def test_bad_file(random_path, random_name):
    key = Fernet.generate_key()
    data = randbytes(128)
    dataf = os.path.join(random_path, 'test_bad_%s.frnt'%random_name)
    with fernetfile.FernetFile(dataf, mode='wb', fernet_key=key) as ff:
        ff.write(data)

    with fernetfile.FernetFile(dataf, mode='rb', fernet_key=key) as ff:
        datar = ff.read()

    with open(dataf, mode='rb') as ff:
        cdata = ff.read()

    with open(dataf, mode='wb') as ff:
        ff.write(cdata[:-1])

    with fernetfile.FernetFile(dataf, mode='rb', fernet_key=key) as ff:
        with pytest.raises(EOFError):
            data = ff.read()

    with open(dataf, mode='wb') as ff:
        ff.write(cdata[:-45] + b'o' + cdata[45:])

    with fernetfile.FernetFile(dataf, mode='rb', fernet_key=key) as ff:
        with pytest.raises(InvalidToken):
            data = ff.read()

def test_EncryptFile(random_path, random_name):
    key = Fernet.generate_key()
    data = randbytes(128)
    dataf = os.path.join(random_path, 'test_encrypt_%s.frnt'%random_name)
    assert len(fernetfile.EncryptFile.cryptor_factory()) > 0

    with pytest.raises(IndexError):
        assert fernetfile.EncryptFile.cryptor_factory('baddd') is not None

    assert fernetfile.EncryptFile.cryptor_factory('fernet') is not None


    with fernetfile.EncryptFile(dataf, mode='wb', cryptor='fernet', fernet_key=key) as ff:
        assert repr(ff).startswith("<EncryptFile ")
        ff.write(data)

    with fernetfile.FernetFile(dataf, mode='rb', fernet_key=key) as ff:
        datar = ff.read()

    assert data == datar

    with open(dataf, "rb") as fdata:
        with fernetfile.EncryptFile(fileobj=fdata, mode=None, cryptor='fernet', fernet_key=key) as ff:
            datar = ff.read()
        assert data == datar


def test_DummyFile(random_path, random_name):
    data = randbytes(128)
    dataf = os.path.join(random_path, 'test_dummy_%s.frnt'%random_name)

    with DummyFile(dataf, mode='wb') as ff:
        assert repr(ff).startswith("<DummyFile ")
        ff.write(data)

    with DummyFile(dataf, mode='rb') as ff:
        datar = ff.read()

    assert data == datar


def test_append(random_path, random_name):
    key = Fernet.generate_key()
    data = randbytes(1784) + b'0111110' + randbytes(3594) + b'0100010' + randbytes(2145)
    dataap = randbytes(2715)
    dataf = os.path.join(random_path, 'test_seek_%s.frnt'%random_name)

    with fernetfile.open(dataf, mode='wb', fernet_key=key) as ff:
        assert ff.fileno() is not None
        ff.write(data)
        assert ff.writable()
        assert not ff.readable()
        with pytest.raises(OSError):
            ff.rewind()
        with pytest.raises(OSError):
            ff.seek(0, whence=io.SEEK_SET)
        ff.seek(0, whence=io.SEEK_CUR)

    with fernetfile.open(dataf, mode='ab', fernet_key=key) as ff:
        ff.write(dataap)

    with fernetfile.open(dataf, "rb", fernet_key=key) as ff:
        assert ff.fileno() is not None
        assert ff.readable()
        assert not ff.writable()
        datar = ff.read()
        assert data + dataap == datar
        ff.rewind()
        # ~ assert ff.offset == 0
        datar = ff.read()
        assert data + dataap == datar
        ff.seek(1784, whence=io.SEEK_SET)
        datar = ff.read(size=7)
        assert b'0111110' == datar
        ff.seek(3594, whence=io.SEEK_CUR)
        datar = ff.read(size=7)
        assert b'0100010' == datar
        ff.seek(2145, whence=io.SEEK_CUR)
        datar = ff.read(size=3715)
        assert dataap == datar

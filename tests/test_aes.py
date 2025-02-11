# -*- encoding: utf-8 -*-
"""Test module

"""
import os
import io
from random import randbytes
import tarfile
import lzma
import bz2
import zipfile
import struct

import fernetfile

import pytest

try:
    import Crypto
    AES = True

    from cofferfile.aes import AesFile, open as aes_open

except ModuleNotFoundError:
    AES = False
    # ~ class AesFile():
        # ~ pass

@pytest.mark.skipif(not AES, reason="requires the pycryptodome library")
@pytest.mark.parametrize("chunk_size, file_size",
    [
        (1024 * 1, 1024 * 10), (1024 * 1, 1024 * 10 + 4), (1024 * 1, 1024 * 10 + 5),
        (1024 * 10, 1024 * 10), (1024 * 10, 1024 * 10 + 7), (1024 * 10, 1024 * 10 + 3),
        (1024 * 100, 1024 * 10), (1024 * 100, 1024 * 10 + 9), (1024 * 100, 1024 * 10 + 11),
    ])
def test_buffer_fernet_file(random_path, random_name, chunk_size, file_size):

    key = b'Sixteen byte keySixteen byte key'
    iv = b'Sixteen byte key'

    data = randbytes(file_size)
    dataf = os.path.join(random_path, random_name)
    with AesFile(dataf, mode='wb', key=key, iv=iv, chunk_size=chunk_size) as ff:
        ff.write(data)
    with open(dataf, "rb") as ff:
        datar = ff.read()
    assert data != datar
    with AesFile(dataf, "rb", key=key, iv=iv) as ff:
        datar = ff.read()
    assert data == datar

    data = random_name * 2
    dataf = os.path.join(random_path, random_name)
    with aes_open(dataf, mode='wt', key=key, iv=iv, chunk_size=chunk_size) as ff:
        ff.write(data)
    with open(dataf, "rb") as ff:
        datar = ff.read()
    assert data != datar
    with aes_open(dataf, "rt", key=key, iv=iv) as ff:
        datar = ff.read()
    assert data == datar

@pytest.mark.skipif(not AES, reason="requires the pycryptodome library")
@pytest.mark.parametrize("chunk_size, file_size",
    [
        (1024 * 1, 1024 * 10), (1024 * 1, 1024 * 10 + 4), (1024 * 1, 1024 * 10 + 5),
        (1024 * 10, 1024 * 10), (1024 * 10, 1024 * 10 + 7), (1024 * 10, 1024 * 10 + 3),
        (1024 * 100, 1024 * 10), (1024 * 100, 1024 * 10 + 9), (1024 * 100, 1024 * 10 + 11),
    ])
def test_buffer_aes_open(random_path, random_name, chunk_size, file_size):

    key = b'Sixteen byte keySixteen byte key'
    iv = b'Sixteen byte key'

    data = randbytes(file_size)
    dataf = os.path.join(random_path, random_name)
    with aes_open(dataf, mode='wb', key=key, iv=iv, chunk_size=chunk_size) as ff:
        ff.write(data)
    with open(dataf, "rb") as ff:
        datar = ff.read()
    assert data != datar
    with aes_open(dataf, "rb", key=key, iv=iv) as ff:
        datar = ff.read()
    assert data == datar

    data = random_name * 2
    dataf = os.path.join(random_path, random_name)
    with aes_open(dataf, mode='wt', key=key, iv=iv, chunk_size=chunk_size) as ff:
        ff.write(data)
    with open(dataf, "rb") as ff:
        datar = ff.read()
    assert data != datar
    with aes_open(dataf, "rt", key=key, iv=iv) as ff:
        datar = ff.read()
    assert data == datar

@pytest.mark.skipif(not AES, reason="requires the pycryptodome library")
def test_bad(random_path, random_name):
    key = b'Sixteen byte keySixteen byte key'
    iv = b'Sixteen byte key'
    data = randbytes(128)
    dataf = os.path.join(random_path, 'test_bad_%s.frnt'%random_name)
    dataok = os.path.join(random_path, 'test_ok_%s.frnt'%random_name)

    with AesFile(dataok, mode='wb', key=key, iv=iv) as ff:
        assert repr(ff).startswith('<AesFile')

    with pytest.raises(ValueError):
        with AesFile(dataf, mode='wbt', key=key, iv=iv) as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with AesFile(dataf, mode='zzz', key=key, iv=iv) as ff:
            ff.write(data)

    with pytest.raises(FileNotFoundError):
        with AesFile(None, mode='wb', key=key, iv=iv) as ff:
            ff.write(data)

    with pytest.raises(FileNotFoundError):
        with AesFile(dataf, key=key, iv=iv) as ff:
            data = ff.read()

    with pytest.raises(ValueError):
        with aes_open(dataf, mode='wbt', key=key, iv=iv) as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with aes_open(dataf, mode='wb', key=key, iv=iv, encoding='utf-8') as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with aes_open(dataf, mode='wb', key=key, iv=iv, errors=True) as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with aes_open(dataf, mode='wb', key=key, iv=iv, newline='\n') as ff:
            ff.write(data)

    with pytest.raises(TypeError):
        with aes_open(None, mode='wb', key=key, iv=iv) as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with aes_open(dataf, mode='wb', key=None) as ff:
            ff.write(data)

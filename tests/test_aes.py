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

    from cofferfile.aes import AesFile

except ModuleNotFoundError:
    AES = False
    # ~ class NaclFile():
        # ~ pass

@pytest.mark.skipif(not AES, reason="requires the pycryptodome library")
@pytest.mark.parametrize("buff_size, file_size",
    [
        (1024 * 1, 1024 * 10), (1024 * 1, 1024 * 10 + 4), (1024 * 1, 1024 * 10 + 5),
        (1024 * 10, 1024 * 10), (1024 * 10, 1024 * 10 + 7), (1024 * 10, 1024 * 10 + 3),
        (1024 * 100, 1024 * 10), (1024 * 100, 1024 * 10 + 9), (1024 * 100, 1024 * 10 + 11),
    ])
def test_buffer_aes(random_path, random_name, buff_size, file_size):
    fernetfile.BUFFER_SIZE = buff_size
    key = b'Sixteen byte keySixteen byte key'
    iv = b'Sixteen byte key'
    data = randbytes(file_size)
    dataf = os.path.join(random_path, random_name)
    with AesFile(dataf, mode='wb', key=key, iv=iv) as ff:
        ff.write(data)
    with open(dataf, "rb") as ff:
        datar = ff.read()
    assert data != datar
    with AesFile(dataf, "rb", key=key, iv=iv) as ff:
        datar = ff.read()
    fernetfile.BUFFER_SIZE = 1024 * 10
    assert data == datar

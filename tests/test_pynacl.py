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

from nacl import utils
from nacl.secret import SecretBox

import fernetfile

import pytest

try:
    import nacl
    NACL = True

    from naclfile import NaclFile

except ModuleNotFoundError:
    NACL = False
    # ~ class NaclFile():
        # ~ pass

@pytest.mark.skipif(not NACL, reason="requires the pynacl library")
@pytest.mark.parametrize("buff_size, file_size",
    [
        (1024 * 1, 1024 * 10), (1024 * 1, 1024 * 10 + 4), (1024 * 1, 1024 * 10 + 5),
        (1024 * 10, 1024 * 10), (1024 * 10, 1024 * 10 + 7), (1024 * 10, 1024 * 10 + 3),
        (1024 * 100, 1024 * 10), (1024 * 100, 1024 * 10 + 9), (1024 * 100, 1024 * 10 + 11),
    ])
def test_buffer_nacl(random_path, random_name, buff_size, file_size):
    fernetfile.BUFFER_SIZE = buff_size
    key = utils.random(SecretBox.KEY_SIZE)
    data = randbytes(file_size)
    dataf = os.path.join(random_path, random_name)
    with NaclFile(dataf, mode='wb', secret_key=key) as ff:
        ff.write(data)
    with open(dataf, "rb") as ff:
        datar = ff.read()
    assert data != datar
    with NaclFile(dataf, "rb", secret_key=key) as ff:
        datar = ff.read()
    fernetfile.BUFFER_SIZE = 1024 * 10
    assert data == datar

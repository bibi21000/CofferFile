# -*- encoding: utf-8 -*-
"""Test module

"""
import os
import io
from random import randbytes
import tarfile
import struct

from cryptography.fernet import Fernet

from cofferfile.zstd import clean_level_or_option, ZstdTarFile
import fernetfile

import pytest


try:
    import pyzstd
    ZSTD = True

    from fernetfile.zstd import FernetFile as ZstdFernetFile, open as zstd_open
    from fernetfile.tar import TarFile as TarZstdFernetFile, open as zstd_tar_open

except ModuleNotFoundError:
    ZSTD = False
    # ~ class ZstdFernetFile():
        # ~ pass

@pytest.mark.skipif(not ZSTD, reason="requires the pyzstd library")
@pytest.mark.parametrize("buff_size, file_size", [ (1024 * 32, 1024 * 1024 * 1) ])
def test_crypt_zstd(random_path, random_name, buff_size, file_size):
    key = Fernet.generate_key()
    data = randbytes(file_size)
    dataf = os.path.join(random_path, 'test%s.frnt'%random_name)
    with ZstdFernetFile(dataf, mode='wb', fernet_key=key, chunk_size=buff_size) as ff:
        ff.write(data)
    with open(dataf, "rb") as ff:
        datar = ff.read()
    assert data != datar
    with fernetfile.open(dataf, "rb", fernet_key=key) as ff:
        datar = ff.read()
        datar = pyzstd.decompress(datar)
    assert data == datar
    with ZstdFernetFile(dataf, "rb", fernet_key=key) as ff:
        datar = ff.read()
    assert data == datar

    with open(dataf, "rb") as fdata:
        with zstd_open(fdata, "rb", fernet_key=key) as ff:
            datar = ff.read()
        assert data == datar


@pytest.mark.skipif(not ZSTD, reason="requires the pyzstd library")
@pytest.mark.parametrize("buff_size, file_size", [ (1024 * 64, 1024 * 512 + 21) ])
def test_crypt_zstd_tar(random_path, random_name, buff_size, file_size):
    key = Fernet.generate_key()
    dataf = os.path.join(random_path, 'test%s.tbzf'%random_name)

    dataf1 = os.path.join(random_path, 'file1%s.out'%random_name)
    with open(dataf1, "wb") as out:
        out.write(os.urandom(file_size * 5))
    with open(dataf1, "rb") as ff:
        ddataf1 = ff.read()

    dataf2 = os.path.join(random_path, 'file2%s.out'%random_name)
    with open(dataf2, "wb") as out:
        out.write(os.urandom(file_size * 50))
    with open(dataf2, "rb") as ff:
        ddataf2 = ff.read()

    with TarZstdFernetFile(dataf, mode='w', fernet_key=key, chunk_size=buff_size) as ff:
        ff.add(dataf1, 'file1%s.out'%random_name)
        ff.add(dataf2, 'file2%s.out'%random_name)

    os.unlink(dataf1)
    os.unlink(dataf2)

    with TarZstdFernetFile(dataf, "r", fernet_key=key) as ff:
        fdatae = ff.extractfile('file1%s.out'%random_name)
        assert fdatae.read() == ddataf1
        fdatae = ff.extractfile('file2%s.out'%random_name)
        assert fdatae.read() == ddataf2

@pytest.mark.parametrize("buff_size, file_size", [ (1024 * 32, 1024 * 512 + 31) ])
def test_crypt_zstd_tar_append(random_path, random_name, buff_size, file_size):
    key = Fernet.generate_key()
    dataf = os.path.join(random_path, 'test%s.tbzf'%random_name)

    dataf1 = os.path.join(random_path, 'file1%s.out'%random_name)
    with open(dataf1, "wb") as out:
        out.write(os.urandom(file_size * 5))
    with open(dataf1, "rb") as ff:
        ddataf1 = ff.read()

    dataf2 = os.path.join(random_path, 'file2%s.out'%random_name)
    with open(dataf2, "wb") as out:
        out.write(os.urandom(file_size * 50))
    with open(dataf2, "rb") as ff:
        ddataf2 = ff.read()

    dataf3 = os.path.join(random_path, 'file3%s.out'%random_name)
    with open(dataf3, "wb") as out:
        out.write(os.urandom(file_size * 10))
    with open(dataf3, "rb") as ff:
        ddataf3 = ff.read()

    with TarZstdFernetFile(dataf, mode='w', fernet_key=key, chunk_size=buff_size) as ff:
        ff.add(dataf1, 'file1%s.out'%random_name)
        ff.add(dataf2, 'file2%s.out'%random_name)

    os.unlink(dataf1)
    os.unlink(dataf2)

    # Can't append to tar/bz2
    with pytest.raises(io.UnsupportedOperation):
        with TarZstdFernetFile(dataf, mode='a', fernet_key=key, chunk_size=buff_size) as ff:
            ff.add(dataf3, 'file3%s.out'%random_name)

    # ~ os.unlink(dataf3)

    # ~ with TarZstdFernetFile(dataf, "r", fernet_key=key) as ff:
        # ~ fdatae = ff.extractfile('file1.out')
        # ~ assert fdatae.read() == ddataf1
        # ~ fdatae = ff.extractfile('file2.out')
        # ~ assert fdatae.read() == ddataf2
        # ~ fdatae = ff.extractfile('file3.out')
        # ~ assert fdatae.read() == ddataf3

def test_zstd_encoding(random_path, random_name):
    key = Fernet.generate_key()
    datal = ["Ceci est un texte avec des accents : éè","avec plusieurs","lignes"]
    data = "\n".join(datal)
    dataf = os.path.join(random_path, 'test_encoding_%s.frnt'%random_name)

    with zstd_open(dataf, mode='wt', fernet_key=key, encoding="utf-8") as ff:
        ff.write(data)

    with pytest.raises(ValueError):
        with open(dataf, "r", encoding="utf-8") as ff:
            datar = ff.read()
        assert data != datar

    with zstd_open(dataf, "rt", fernet_key=key, encoding="utf-8") as ff:
        datar = ff.read()
    assert data == datar

    with zstd_open(dataf, "rt", fernet_key=key, encoding="utf-8") as ff:
        datar = ff.read()
    assert data == datar

    with zstd_open(dataf, "rt", fernet_key=key, encoding="utf-8") as ff:
        datar = ff.readline()
        assert datal[0] + '\n' == datar
        datar = ff.readline()
        assert datal[1] + '\n' == datar
        datar = ff.readline()
        assert datal[2] == datar

    datal = ["Ceci est un texte avec des accents : éè","avec plusieurs","lignes"]
    dataf = os.path.join(random_path, 'test_encoding.frnt')

    with zstd_open(dataf, mode='wt', fernet_key=key, encoding="utf-8") as ff:
        ff.writelines(data)

    with zstd_open(dataf, "rt", fernet_key=key, encoding="utf-8") as ff:
        datar = ff.readlines()

    assert datal[0] + '\n' == datar[0]
    assert datal[1] + '\n' == datar[1]
    assert datal[2] == datar[2]


def test_files_zstd_encrypt(random_path, random_name):

    key = Fernet.generate_key()

    datafsrc = os.path.join(random_path, 'test%s.dat'%random_name)
    dataftgt = os.path.join(random_path, 'test%s.dtc'%random_name)
    datafdec = os.path.join(random_path, 'test%s.dec'%random_name)

    with open(datafsrc, 'wb') as f:
        for i in range(1024):
            f.write(randbytes(1024 * 5 + i))

    with open(datafsrc, 'rb') as fin, zstd_open(dataftgt, mode='wb', fernet_key=key) as fout:
        while True:
            data = fin.read(7777)
            if not data:
                break
            fout.write(data)

    with zstd_open(dataftgt, mode='rb', fernet_key=key) as fin, open(datafdec, 'wb') as fout :
        while True:
            data = fin.read(8888)
            if not data:
                break
            fout.write(data)

    with open(datafsrc, 'rb') as f1, open(datafdec, 'rb') as f2:
        assert f1.read() == f2.read()

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
    dataf = os.path.join(random_path, 'test%s.frnt'%random_name)
    with zstd_open(dataf, mode='wb', fernet_key=key) as ff:
        ff.write(data)
    with open(dataf, "rb") as ff:
        datar = ff.read()
    assert data != datar
    with zstd_open(dataf, "rb", fernet_key=key) as ff:
        datar = ff.read()
    fernetfile.BUFFER_SIZE = 1024 * 10
    assert data == datar

def test_zst_bad_mode(random_path, random_name):
    key = Fernet.generate_key()
    data = randbytes(128)
    dataf = os.path.join(random_path, 'test_bad_mode_%s.frnt'%random_name)

    print(repr(ZstdFernetFile))

    with pytest.raises(ValueError):
        with ZstdFernetFile(dataf, mode='wbt', fernet_key=None) as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with ZstdFernetFile(dataf, mode='wbt', fernet_key=key) as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with ZstdFernetFile(dataf, mode='zzz', fernet_key=key) as ff:
            ff.write(data)

    with pytest.raises(FileNotFoundError):
        with ZstdFernetFile(None, mode='wb', fernet_key=key) as ff:
            ff.write(data)

    with pytest.raises(FileNotFoundError):
        with ZstdFernetFile(dataf, fernet_key=key) as ff:
            data = ff.read()

    with pytest.raises(ValueError):
        with zstd_open(dataf, mode='wbt', fernet_key=key) as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with zstd_open(dataf, mode='wb', fernet_key=key, encoding='utf-8') as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with zstd_open(dataf, mode='wb', fernet_key=key, errors=True) as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with zstd_open(dataf, mode='wb', fernet_key=key, newline='\n') as ff:
            ff.write(data)

    with pytest.raises(TypeError):
        with zstd_open(None, mode='wb', fernet_key=key) as ff:
            ff.write(data)

    with pytest.raises(ValueError):
        with zstd_open(dataf, mode='wb', fernet_key=None) as ff:
            ff.write(data)

    with pytest.raises(TypeError):
        with zstd_open(dataf, mode='wb', fernet_key=key, zstd_dict=1) as ff:
            ff.write(data)

def test_clean_level_or_option(random_path, random_name):

    assert clean_level_or_option({}, mode="r") is None
    assert clean_level_or_option(level_or_option = {
        pyzstd.CParameter.compressionLevel : 12,
        pyzstd.CParameter.nbWorkers : 2
    }, mode="r") is None
    assert len(clean_level_or_option(level_or_option = {
        pyzstd.DParameter.windowLogMax : 24
    }, mode="r")) == 1
    assert clean_level_or_option({}, mode="w") is None
    assert len(clean_level_or_option(level_or_option = {
        pyzstd.CParameter.compressionLevel : 12,
        pyzstd.CParameter.nbWorkers : 2
    }, mode="w")) == 2
    assert clean_level_or_option(level_or_option = {
        pyzstd.DParameter.windowLogMax : 24
    }, mode="w") is None

def test_zst_tar(random_path, random_name):
    datafsrc = os.path.join(random_path, 'test%s.dat'%random_name)
    with open(datafsrc, 'wb') as f:
        for i in range(1024):
            f.write(randbytes(1024 * 5 + i))

    with ZstdTarFile('%s/titi.zstt'%random_path, 'w') as r:
        r.add(datafsrc, 'test.dat')

    with pytest.raises(TypeError):
        with ZstdTarFile('%s/titi.zstt'%random_path, 'w', titi=None) as r:
            r.add(datafsrc, 'test.dat')


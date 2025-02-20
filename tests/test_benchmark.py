# -*- encoding: utf-8 -*-
"""Test module

"""
import os
import importlib
import time
from random import randbytes
import urllib.request
import zipfile
import tarfile

from cryptography.fernet import Fernet
from nacl import utils
from nacl.secret import SecretBox

from Crypto.Random import get_random_bytes

import fernetfile

import pytest
from .conftest import DummyFile
from fernetfile.zstd import FernetFile as _ZstdFernetFile, CParameter, open as zstd_open
import naclfile
from naclfile import NaclFile
from naclfile.zstd import NaclFile as _ZstdNaclFile, open as naclz_open
from naclfile.tar import TarFile as _TarZstdNaclFile
from aesfile import AesFile
from aesfile.zstd import AesFile as _ZstdAesFile, open as aesz_open
from aesfile.tar import TarFile as _TarZstdAesFile
from fernetfile.tar import TarFile as _TarZstdFernetFile
from .test_chain import Bz2FernetFile, LzmaFernetFile, TarBz2FernetFile, TarLzmaFernetFile

class ZstdFernetFile(_ZstdFernetFile):
    pass

class TarZstdFernetFile(_TarZstdFernetFile):
    pass

class ZstdNaclFile(_ZstdNaclFile):
    pass

class TarZstdNaclFile(_TarZstdNaclFile):
    pass

class ZstdAesFile(_ZstdAesFile):
    pass

class TarZstdAesFile(_TarZstdAesFile):
    pass

try:
    import pytest_ordering
    DO = True
    # ~ DO = False
except ModuleNotFoundError:
    DO = False

# ~ @pytest.mark.skip("Manual test")
@pytest.mark.skipif(not DO, reason="requires the pytest_ordering package")
@pytest.mark.run(order=21)
def test_benchmark_general_header(random_path):
    with open('BENCHMARK.md','wt') as ff:
        ff.write("\n")
        ff.write("\n")
        ff.write("# General benchmarks\n")
        ff.write("\n")
        ff.write("| Class                | Data                 |  Chunk size |  Orig size  | Crypt size |  Comp ratio | WTime  | Rtime  |\n")
        ff.write("|:---------------------|:---------------------|------------:|------------:|-----------:|------------:|-------:|-------:|\n")
    if os.path.isfile('docpython.pdf.zip') is False:
        urllib.request.urlretrieve("https://docs.python.org/3/archives/python-3.13-docs-pdf-a4.zip", "docpython.pdf.zip")
        with zipfile.ZipFile('docpython.pdf.zip', 'r') as zip_ref:
            zip_ref.extractall('.')
    if os.path.isfile('docpython.html.zip') is False:
        urllib.request.urlretrieve("https://docs.python.org/3/archives/python-3.13-docs-html.zip", "docpython.html.zip")
        with zipfile.ZipFile('docpython.html.zip', 'r') as zip_ref:
            zip_ref.extractall('.')

# ~ @pytest.mark.skip("Manual test")
@pytest.mark.skipif(not DO, reason="requires the pytest_ordering package")
@pytest.mark.run(order=22)
@pytest.mark.parametrize("fcls, dt, buff_size, file_size", [
    (DummyFile, 'download.html', 1024 * 16, 0),
    (DummyFile, 'genindex-all.html', 1024 * 16, 0),
    (DummyFile, 'searchindex.js', 1024 * 16, 0),
    (DummyFile, 'library.pdf', 1024 * 16, 0),
    (fernetfile.FernetFile, 'download.html', 1024 * 16, 0),
    (fernetfile.FernetFile, 'genindex-all.html', 1024 * 16, 0),
    (fernetfile.FernetFile, 'searchindex.js', 1024 * 16, 0),
    (fernetfile.FernetFile, 'library.pdf', 1024 * 16, 0),
    (NaclFile, 'download.html', 1024 * 16, 0),
    (NaclFile, 'genindex-all.html', 1024 * 16, 0),
    (NaclFile, 'searchindex.js', 1024 * 16, 0),
    (NaclFile, 'library.pdf', 1024 * 16, 0),
    (AesFile, 'download.html', 1024 * 16, 0),
    (AesFile, 'genindex-all.html', 1024 * 16, 0),
    (AesFile, 'searchindex.js', 1024 * 16, 0),
    (AesFile, 'library.pdf', 1024 * 16, 0),
    # ~ (fernetfile.FernetFile, 'rand', 1024 * 16, 1024 * 1024 * 1),
    # ~ (fernetfile.FernetFile, 'rand', 1024 * 16, 1024 * 1024 * 10),
    # ~ (fernetfile.FernetFile, 'rand', 1024 * 16, 1024 * 1024 * 100),
    (Bz2FernetFile, 'download.html', 1024 * 16, 0),
    (Bz2FernetFile, 'genindex-all.html', 1024 * 16, 0),
    (Bz2FernetFile, 'searchindex.js', 1024 * 16, 0),
    (Bz2FernetFile, 'library.pdf', 1024 * 16, 0),
    # ~ (Bz2FernetFile, 'rand', 1024 * 16, 1024 * 1024 * 1),
    # ~ (Bz2FernetFile, 'rand', 1024 * 16, 1024 * 1024 * 10),
    # ~ (Bz2FernetFile, 'rand', 1024 * 16, 1024 * 1024 * 100),
    (LzmaFernetFile, 'download.html', 1024 * 16, 0),
    (LzmaFernetFile, 'genindex-all.html', 1024 * 16, 0),
    (LzmaFernetFile, 'searchindex.js', 1024 * 16, 0),
    (LzmaFernetFile, 'library.pdf', 1024 * 16, 0),
    (ZstdFernetFile, 'download.html', 1024 * 16, 0),
    (ZstdFernetFile, 'genindex-all.html', 1024 * 16, 0),
    (ZstdFernetFile, 'searchindex.js', 1024 * 16, 0),
    (ZstdFernetFile, 'library.pdf', 1024 * 16, 0),
    (ZstdNaclFile, 'download.html', 1024 * 16, 0),
    (ZstdNaclFile, 'genindex-all.html', 1024 * 16, 0),
    (ZstdNaclFile, 'searchindex.js', 1024 * 16, 0),
    (ZstdNaclFile, 'library.pdf', 1024 * 16, 0),
    (ZstdAesFile, 'download.html', 1024 * 16, 0),
    (ZstdAesFile, 'genindex-all.html', 1024 * 16, 0),
    (ZstdAesFile, 'searchindex.js', 1024 * 16, 0),
    (ZstdAesFile, 'library.pdf', 1024 * 16, 0),
    # ~ (ZstdFernetFile, 'rand', 1024 * 16, 1024 * 1024 * 1),
    # ~ (ZstdFernetFile, 'rand', 1024 * 16, 1024 * 1024 * 10),
    # ~ (ZstdFernetFile, 'rand', 1024 * 16, 1024 * 1024 * 100),
    # ~ (fernetfile.FernetFile, b'a', 1024 * 16, 1024 * 1024 * 1),
    # ~ (fernetfile.FernetFile, b'b', 1024 * 16, 1024 * 1024 * 10),
    # ~ (fernetfile.FernetFile, b'c', 1024 * 16, 1024 * 1024 * 100),
    # ~ (Bz2FernetFile, b'd', 1024 * 16, 1024 * 1024 * 1),
    # ~ (Bz2FernetFile, b'e', 1024 * 16, 1024 * 1024 * 10),
    # ~ (Bz2FernetFile, b'f', 1024 * 16, 1024 * 1024 * 100),
    # ~ (ZstdFernetFile, b'g', 1024 * 16, 1024 * 1024 * 1),
    # ~ (ZstdFernetFile, b'h', 1024 * 16, 1024 * 1024 * 10),
    # ~ (ZstdFernetFile, b'i', 1024 * 16, 1024 * 1024 * 100),
    (DummyFile, 'download.html', 1024 * 64, 0),
    (DummyFile, 'genindex-all.html', 1024 * 64, 0),
    (DummyFile, 'searchindex.js', 1024 * 64, 0),
    (DummyFile, 'library.pdf', 1024 * 64, 0),
    (fernetfile.FernetFile, 'download.html', 1024 * 64, 0),
    (fernetfile.FernetFile, 'genindex-all.html', 1024 * 64, 0),
    (fernetfile.FernetFile, 'searchindex.js', 1024 * 64, 0),
    (fernetfile.FernetFile, 'library.pdf', 1024 * 64, 0),
    (NaclFile, 'download.html', 1024 * 64, 0),
    (NaclFile, 'genindex-all.html', 1024 * 64, 0),
    (NaclFile, 'searchindex.js', 1024 * 64, 0),
    (NaclFile, 'library.pdf', 1024 * 64, 0),
    (AesFile, 'download.html', 1024 * 64, 0),
    (AesFile, 'genindex-all.html', 1024 * 64, 0),
    (AesFile, 'searchindex.js', 1024 * 64, 0),
    (AesFile, 'library.pdf', 1024 * 64, 0),
    (Bz2FernetFile, 'download.html', 1024 * 64, 0),
    (Bz2FernetFile, 'genindex-all.html', 1024 * 64, 0),
    (Bz2FernetFile, 'searchindex.js', 1024 * 64, 0),
    (Bz2FernetFile, 'library.pdf', 1024 * 64, 0),
    (LzmaFernetFile, 'download.html', 1024 * 64, 0),
    (LzmaFernetFile, 'genindex-all.html', 1024 * 64, 0),
    (LzmaFernetFile, 'searchindex.js', 1024 * 64, 0),
    (LzmaFernetFile, 'library.pdf', 1024 * 64, 0),
    (ZstdFernetFile, 'download.html', 1024 * 64, 0),
    (ZstdFernetFile, 'genindex-all.html', 1024 * 64, 0),
    (ZstdFernetFile, 'searchindex.js', 1024 * 64, 0),
    (ZstdFernetFile, 'library.pdf', 1024 * 64, 0),
    (ZstdNaclFile, 'download.html', 1024 * 64, 0),
    (ZstdNaclFile, 'genindex-all.html', 1024 * 64, 0),
    (ZstdNaclFile, 'searchindex.js', 1024 * 64, 0),
    (ZstdNaclFile, 'library.pdf', 1024 * 64, 0),
    (ZstdAesFile, 'download.html', 1024 * 64, 0),
    (ZstdAesFile, 'genindex-all.html', 1024 * 64, 0),
    (ZstdAesFile, 'searchindex.js', 1024 * 64, 0),
    (ZstdAesFile, 'library.pdf', 1024 * 64, 0),
    (DummyFile, 'download.html', 1024 * 256, 0),
    (DummyFile, 'genindex-all.html', 1024 * 256, 0),
    (DummyFile, 'searchindex.js', 1024 * 256, 0),
    (DummyFile, 'library.pdf', 1024 * 256, 0),
    (fernetfile.FernetFile, 'download.html', 1024 * 256, 0),
    (fernetfile.FernetFile, 'genindex-all.html', 1024 * 256, 0),
    (fernetfile.FernetFile, 'searchindex.js', 1024 * 256, 0),
    (fernetfile.FernetFile, 'library.pdf', 1024 * 256, 0),
    (NaclFile, 'download.html', 1024 * 256, 0),
    (NaclFile, 'genindex-all.html', 1024 * 256, 0),
    (NaclFile, 'searchindex.js', 1024 * 256, 0),
    (NaclFile, 'library.pdf', 1024 * 256, 0),
    (AesFile, 'download.html', 1024 * 256, 0),
    (AesFile, 'genindex-all.html', 1024 * 256, 0),
    (AesFile, 'searchindex.js', 1024 * 256, 0),
    (AesFile, 'library.pdf', 1024 * 256, 0),
    # ~ (fernetfile.FernetFile, 'rand', 1024 * 256, 1024 * 1024 * 1),
    # ~ (fernetfile.FernetFile, 'rand', 1024 * 256, 1024 * 1024 * 10),
    # ~ (fernetfile.FernetFile, 'rand', 1024 * 256, 1024 * 1024 * 100),
    (Bz2FernetFile, 'download.html', 1024 * 256, 0),
    (Bz2FernetFile, 'genindex-all.html', 1024 * 256, 0),
    (Bz2FernetFile, 'searchindex.js', 1024 * 256, 0),
    (Bz2FernetFile, 'library.pdf', 1024 * 256, 0),
    (LzmaFernetFile, 'download.html', 1024 * 256, 0),
    (LzmaFernetFile, 'genindex-all.html', 1024 * 256, 0),
    (LzmaFernetFile, 'searchindex.js', 1024 * 256, 0),
    (LzmaFernetFile, 'library.pdf', 1024 * 256, 0),
    # ~ (Bz2FernetFile, 'rand', 1024 * 256, 1024 * 1024 * 1),
    # ~ (Bz2FernetFile, 'rand', 1024 * 256, 1024 * 1024 * 10),
    # ~ (Bz2FernetFile, 'rand', 1024 * 256, 1024 * 1024 * 100),
    (ZstdFernetFile, 'download.html', 1024 * 256, 0),
    (ZstdFernetFile, 'genindex-all.html', 1024 * 256, 0),
    (ZstdFernetFile, 'searchindex.js', 1024 * 256, 0),
    (ZstdFernetFile, 'library.pdf', 1024 * 256, 0),
    (ZstdNaclFile, 'download.html', 1024 * 256, 0),
    (ZstdNaclFile, 'genindex-all.html', 1024 * 256, 0),
    (ZstdNaclFile, 'searchindex.js', 1024 * 256, 0),
    (ZstdNaclFile, 'library.pdf', 1024 * 256, 0),
    (ZstdAesFile, 'download.html', 1024 * 256, 0),
    (ZstdAesFile, 'genindex-all.html', 1024 * 256, 0),
    (ZstdAesFile, 'searchindex.js', 1024 * 256, 0),
    (ZstdAesFile, 'library.pdf', 1024 * 256, 0),
    # ~ (ZstdFernetFile, 'rand', 1024 * 256, 1024 * 1024 * 1),
    # ~ (ZstdFernetFile, 'rand', 1024 * 256, 1024 * 1024 * 10),
    # ~ (ZstdFernetFile, 'rand', 1024 * 256, 1024 * 1024 * 100),
    # ~ (fernetfile.FernetFile, b'a', 1024 * 256, 1024 * 1024 * 1),
    # ~ (fernetfile.FernetFile, b'b', 1024 * 256, 1024 * 1024 * 10),
    # ~ (fernetfile.FernetFile, b'c', 1024 * 256, 1024 * 1024 * 100),
    # ~ (Bz2FernetFile, b'd', 1024 * 256, 1024 * 1024 * 1),
    # ~ (Bz2FernetFile, b'e', 1024 * 256, 1024 * 1024 * 10),
    # ~ (Bz2FernetFile, b'f', 1024 * 256, 1024 * 1024 * 100),
    # ~ (ZstdFernetFile, b'g', 1024 * 256, 1024 * 1024 * 1),
    # ~ (ZstdFernetFile, b'h', 1024 * 256, 1024 * 1024 * 10),
    # ~ (ZstdFernetFile, b'i', 1024 * 256, 1024 * 1024 * 100),
    (DummyFile, 'download.html', 1024 * 1024, 0),
    (DummyFile, 'genindex-all.html', 1024 * 1024, 0),
    (DummyFile, 'searchindex.js', 1024 * 1024, 0),
    (DummyFile, 'library.pdf', 1024 * 1024, 0),
    (fernetfile.FernetFile, 'download.html', 1024 * 1024, 0),
    (fernetfile.FernetFile, 'genindex-all.html', 1024 * 1024, 0),
    (fernetfile.FernetFile, 'searchindex.js', 1024 * 1024, 0),
    (fernetfile.FernetFile, 'library.pdf', 1024 * 1024, 0),
    (NaclFile, 'download.html', 1024 * 1024, 0),
    (NaclFile, 'genindex-all.html', 1024 * 1024, 0),
    (NaclFile, 'searchindex.js', 1024 * 1024, 0),
    (NaclFile, 'library.pdf', 1024 * 1024, 0),
    (AesFile, 'download.html', 1024 * 1024, 0),
    (AesFile, 'genindex-all.html', 1024 * 1024, 0),
    (AesFile, 'searchindex.js', 1024 * 1024, 0),
    (AesFile, 'library.pdf', 1024 * 1024, 0),
    (Bz2FernetFile, 'download.html', 1024 * 1024, 0),
    (Bz2FernetFile, 'genindex-all.html', 1024 * 1024, 0),
    (Bz2FernetFile, 'searchindex.js', 1024 * 1024, 0),
    (Bz2FernetFile, 'library.pdf', 1024 * 1024, 0),
    (LzmaFernetFile, 'download.html', 1024 * 1024, 0),
    (LzmaFernetFile, 'genindex-all.html', 1024 * 1024, 0),
    (LzmaFernetFile, 'searchindex.js', 1024 * 1024, 0),
    (LzmaFernetFile, 'library.pdf', 1024 * 1024, 0),
    (ZstdFernetFile, 'download.html', 1024 * 1024, 0),
    (ZstdFernetFile, 'genindex-all.html', 1024 * 1024, 0),
    (ZstdFernetFile, 'searchindex.js', 1024 * 1024, 0),
    (ZstdFernetFile, 'library.pdf', 1024 * 1024, 0),
    (ZstdNaclFile, 'download.html', 1024 * 1024, 0),
    (ZstdNaclFile, 'genindex-all.html', 1024 * 1024, 0),
    (ZstdNaclFile, 'searchindex.js', 1024 * 1024, 0),
    (ZstdNaclFile, 'library.pdf', 1024 * 1024, 0),
    (ZstdAesFile, 'download.html', 1024 * 1024, 0),
    (ZstdAesFile, 'genindex-all.html', 1024 * 1024, 0),
    (ZstdAesFile, 'searchindex.js', 1024 * 1024, 0),
    (ZstdAesFile, 'library.pdf', 1024 * 1024, 0),
])
def test_benchmark_general(random_path, fcls, dt, buff_size, file_size):
    if fcls == NaclFile or fcls == ZstdNaclFile:
        params = {
            'secret_key': utils.random(SecretBox.KEY_SIZE)
        }
    elif fcls == AesFile or fcls == ZstdAesFile:
        params = {
            'aes_key': get_random_bytes(16),
        }
    elif fcls == DummyFile:
        params = {
        }
    else:
        params = {
            'fernet_key': Fernet.generate_key()
        }
    if dt == 'rand':
        data = randbytes(file_size)
    elif '.pdf' in dt:
        fff = os.path.join('docs-pdf', dt)
        with open(fff,'rb') as ff:
            data = ff.read()
        file_size = os.path.getsize(fff)
    elif '.html' in dt or '.js' in dt:
        fff = os.path.join('python-3.13-docs-html', dt)
        with open(fff,'rb') as ff:
            data = ff.read()
        file_size = os.path.getsize(fff)
    else:
        data = dt * file_size
    dataf = os.path.join(random_path, 'test.frnt')
    time_start = time.time()
    print(fcls, params)
    with fcls(dataf, mode='wb', chunk_size=buff_size, **params) as ff:
        ff.write(data)
    time_write = time.time()
    with fcls(dataf, "rb", **params) as ff:
        datar = ff.read()
    time_read = time.time()
    assert data == datar
    comp_size = os.path.getsize(dataf)
    with open('BENCHMARK.md','at') as ff:
        ff.write("| %-20s | %-20s | %11.0f |  %10.0f | %10.0f | %10.2f%% | %6.2f | %6.2f |\n" % (("%s" % fcls).split('.')[-1][:-2], dt, buff_size / 1024, file_size / 1024, comp_size / 1024, comp_size / file_size * 100, time_write - time_start, time_read - time_write))

# ~ @pytest.mark.skip("Manual test")
@pytest.mark.skipif(not DO, reason="requires the pytest_ordering package")
@pytest.mark.run(order=23)
@pytest.mark.parametrize("fcls, dt, buff_size, file_size", [
    (TarBz2FernetFile, 'html,js and pdf', 1024 * 16, 0),
    (TarBz2FernetFile, 'html,js and pdf', 1024 * 256, 0),
    (TarBz2FernetFile, 'html,js and pdf', 1024 * 1024, 0),
    (TarZstdNaclFile, 'html,js and pdf', 1024 * 16, 0),
    (TarZstdNaclFile, 'html,js and pdf', 1024 * 256, 0),
    (TarZstdNaclFile, 'html,js and pdf', 1024 * 1024, 0),
    (TarZstdAesFile, 'html,js and pdf', 1024 * 16, 0),
    (TarZstdAesFile, 'html,js and pdf', 1024 * 256, 0),
    (TarZstdAesFile, 'html,js and pdf', 1024 * 1024, 0),
    (TarZstdFernetFile, 'html,js and pdf', 1024 * 16, 0),
    (TarZstdFernetFile, 'html,js and pdf', 1024 * 256, 0),
    (TarZstdFernetFile, 'html,js and pdf', 1024 * 1024, 0),
    (TarLzmaFernetFile, 'html,js and pdf', 1024 * 16, 0),
    (TarLzmaFernetFile, 'html,js and pdf', 1024 * 256, 0),
    (TarLzmaFernetFile, 'html,js and pdf', 1024 * 1024, 0),
    (tarfile.TarFile, 'html,js and pdf', 0, 0),
])
def test_benchmark_tar(random_path, fcls, dt, buff_size, file_size):
    if fcls == TarZstdNaclFile:
        params = {
            'secret_key': utils.random(SecretBox.KEY_SIZE),
            'chunk_size': buff_size,
        }
    elif fcls == tarfile.TarFile:
        params = { }
    elif fcls == TarZstdAesFile:
        params = {
            'aes_key': get_random_bytes(16),
            'chunk_size': buff_size,
        }
    else:
        params = {
            'fernet_key': Fernet.generate_key(),
            'chunk_size': buff_size,
        }
    dataf = os.path.join(random_path, 'test.frnt')
    time_start = time.time()
    with fcls(dataf, mode='w', **params) as ff:
        for tf in ['download.html', 'genindex-all.html', 'searchindex.js']:
            df = os.path.join('python-3.13-docs-html', tf)
            ff.add(df, tf)
            file_size += os.path.getsize(df)
        for tf in [ 'library.pdf']:
            df = os.path.join('docs-pdf', tf)
            ff.add(df, tf)
            file_size += os.path.getsize(df)
    time_write = time.time()
    with fcls(dataf, "r", **params) as ff:
        ff.extractall('extract_tar')
    time_read = time.time()
    # ~ assert data == datar
    comp_size = os.path.getsize(dataf)
    for tf in ['download.html', 'genindex-all.html', 'searchindex.js']:
        with open(os.path.join('python-3.13-docs-html', tf),'rb') as ff:
            data = ff.read()
        with open(os.path.join('extract_tar', tf),'rb') as ff:
            datar = ff.read()
        assert data == datar
    for tf in [ 'library.pdf']:
        with open(os.path.join('docs-pdf', tf),'rb') as ff:
            data = ff.read()
        with open(os.path.join('extract_tar', tf),'rb') as ff:
            datar = ff.read()
        assert data == datar
    with open('BENCHMARK.md','at') as ff:
        ff.write("| %-20s | %-20s | %11.0f |  %10.0f | %10.0f | %10.2f%% | %6.2f | %6.2f |\n" % (("%s" % fcls).split('.')[-1][:-2], dt, buff_size / 1024, file_size / 1024, comp_size / 1024, comp_size / file_size * 100, time_write - time_start, time_read - time_write))

@pytest.mark.skipif(not DO, reason="requires the pytest_ordering package")
@pytest.mark.run(order=30)
def test_benchmark_zstd_header(random_path):
    with open('BENCHMARK.md','at') as ff:
        ff.write("\n")
        ff.write("\n")
        ff.write("# Benchmarks ZstdFernetFile\n")
        ff.write("\n")
        ff.write("Tests with different compression level and workers\n")
        ff.write("\n")
        ff.write("| Class                | Data                 | Lvl | Wrks |  Orig size  | Crypt size |  Comp ratio | WTime  | Rtime  |\n")
        ff.write("|:---------------------|:---------------------|----:|-----:|------------:|-----------:|------------:|-------:|-------:|\n")
    if os.path.isfile('docpython.pdf.zip') is False:
        urllib.request.urlretrieve("https://docs.python.org/3/archives/python-3.13-docs-pdf-a4.zip", "docpython.pdf.zip")
        with zipfile.ZipFile('docpython.pdf.zip', 'r') as zip_ref:
            zip_ref.extractall('.')
    if os.path.isfile('docpython.html.zip') is False:
        urllib.request.urlretrieve("https://docs.python.org/3/archives/python-3.13-docs-html.zip", "docpython.html.zip")
        with zipfile.ZipFile('docpython.html.zip', 'r') as zip_ref:
            zip_ref.extractall('.')



# ~ @pytest.mark.skip("Manual test")
@pytest.mark.skipif(not DO, reason="requires the pytest_ordering package")
@pytest.mark.run(order=31)
@pytest.mark.parametrize("fcls, dt, lvl, wrks", [
    (ZstdFernetFile, 'genindex-all.html', 9, 2),
    (ZstdFernetFile, 'genindex-all.html', 9, 8),
    (ZstdFernetFile, 'genindex-all.html', 9, 12),
    (ZstdFernetFile, 'genindex-all.html', 19, 2),
    (ZstdFernetFile, 'genindex-all.html', 19, 8),
    (ZstdFernetFile, 'genindex-all.html', 19, 12),
    (ZstdFernetFile, 'searchindex.js', 9, 2),
    (ZstdFernetFile, 'searchindex.js', 9, 8),
    (ZstdFernetFile, 'searchindex.js', 9, 12),
    (ZstdFernetFile, 'searchindex.js', 19, 2),
    (ZstdFernetFile, 'searchindex.js', 19, 8),
    (ZstdFernetFile, 'searchindex.js', 19, 12),
    (ZstdFernetFile, 'library.pdf', 9, 2),
    (ZstdFernetFile, 'library.pdf', 9, 8),
    (ZstdFernetFile, 'library.pdf', 9, 12),
    (ZstdFernetFile, 'library.pdf', 19, 2),
    (ZstdFernetFile, 'library.pdf', 19, 8),
    (ZstdFernetFile, 'library.pdf', 19, 12),
])
def test_benchmark_zstd_tar(random_path, fcls, dt, lvl, wrks):
    key = Fernet.generate_key()
    dataf = os.path.join(random_path, 'test.frnt')
    time_start = time.time()
    level_or_option = {
        CParameter.compressionLevel : lvl,
        CParameter.nbWorkers : wrks
    }
    key = Fernet.generate_key()
    if dt == 'rand':
        data = randbytes(file_size)
    elif '.pdf' in dt:
        fff = os.path.join('docs-pdf', dt)
        with open(fff,'rb') as ff:
            data = ff.read()
        file_size = os.path.getsize(fff)
    elif '.html' in dt or '.js' in dt:
        fff = os.path.join('python-3.13-docs-html', dt)
        with open(fff,'rb') as ff:
            data = ff.read()
        file_size = os.path.getsize(fff)
    else:
        data = dt * file_size
    dataf = os.path.join(random_path, 'test.frnt')
    time_start = time.time()
    with fcls(dataf, mode='wb', fernet_key=key, level_or_option=level_or_option) as ff:
        ff.write(data)
    time_write = time.time()
    level_or_option = {
        # ~ DParameter.windowLogMax : 0,
    }
    with fcls(dataf, "rb", fernet_key=key, level_or_option=level_or_option) as ff:
    # ~ with fcls(dataf, "rb", fernet_key=key) as ff:
        datar = ff.read()
    time_read = time.time()
    assert data == datar
    comp_size = os.path.getsize(dataf)
    with open('BENCHMARK.md','at') as ff:
        ff.write("| %-20s | %-20s | %3.0f | %4.0f |  %10.0f | %10.0f | %10.2f%% | %6.2f | %6.2f |\n" % (("%s" % fcls).split('.')[-1][:-2], dt, lvl, wrks, file_size / 1024, comp_size / 1024, comp_size / file_size * 100, time_write - time_start, time_read - time_write))

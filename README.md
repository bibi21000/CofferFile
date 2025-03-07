[![CircleCI](https://dl.circleci.com/status-badge/img/gh/bibi21000/CofferFile/tree/main.svg?style=shield)](https://dl.circleci.com/status-badge/redirect/gh/bibi21000/CofferFile/tree/main)
[![CodeQL](https://github.com/bibi21000/CofferFile/actions/workflows/codeql.yml/badge.svg)](https://github.com/bibi21000/CofferFile/actions/workflows/codeql.yml)
[![codecov](https://codecov.io/gh/bibi21000/CofferFile/graph/badge.svg?token=4124GIOJAK)](https://codecov.io/gh/bibi21000/CofferFile)
![PyPI - Downloads](https://img.shields.io/pypi/dm/cofferfile)

# CofferFile

A python xxxFile like (ie TarFile, GzipFile, BZ2File, pyzstd.ZstdFile, ...)
for encrypting files with Fernet, Nacl, ...

 - encrypting / decrypting data using chunks to reduce memory footprint
 - chainable with other python xxxFile interfaces (stream mode)
 - interface to compress/encrypt and decrypt/decompress (with pyzstd) in stream mode
 - look at BENCHMARK.md ... and chain :)

If you're looking for a more powerfull storage for your sensible datas,
look at PyCoffer : https://github.com/bibi21000/PyCoffer.

This is the main library.
Look at https://github.com/bibi21000/NaclFile, https://github.com/bibi21000/FernetFile,
https://github.com/bibi21000/TinkFile or https://github.com/bibi21000/AesFile for implementations with cryptograhics tools.

Look at documentation : https://bibi21000.github.io/CofferFile.


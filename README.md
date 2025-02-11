[![CircleCI](https://dl.circleci.com/status-badge/img/gh/bibi21000/CofferFile/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/bibi21000/CofferFile/tree/main)
[![codecov](https://codecov.io/gh/bibi21000/CofferFile/graph/badge.svg?token=4124GIOJAK)](https://codecov.io/gh/bibi21000/CofferFile)
![PyPI - Downloads](https://img.shields.io/pypi/dm/cofferfile)

# CofferFile

A python xxxFile like (ie TarFile, GzipFile, BZ2File, pyzstd.ZstdFile, ...)
for encrypting files with Fernet, Nacl, ...

 - encrypting / decrypting data using chunks to reduce memory footprint
 - chainable with other python xxxFile interfaces (stream mode)
 - interface to compress/encrypt and decrypt/decompress (with pyzstd) in stream mode
 - look at BENCHMARK.md ... and chain :)
 - look at tests for examples

This is the main library.
Look at https://github.com/bibi21000/NaclFile and https://github.com/bibi21000/FernetFile.

Look at documentation : https://bibi21000.github.io/CofferFile.


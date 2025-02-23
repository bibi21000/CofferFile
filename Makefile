#!/usr/bin/make -f
-include makefile.local

ifndef PYTHON
PYTHON:=python3
endif

.PHONY: venv tests

venv:
	${PYTHON} -m venv venv
	./venv/bin/pip install -e .
	./venv/bin/pip install .[test]
	./venv/bin/pip install .[build]
	./venv/bin/pip install .[doc]
#~ 	./venv/bin/pip install .[zstd]
#~ 	./venv/bin/pip install .[store]
#~ 	./venv/bin/pip install .[fernet]
#~ 	./venv/bin/pip install .[pynacl]
#~ 	./venv/bin/pip install .[aes]
#~ 	./venv/bin/pip install .[cli]
	./venv/bin/pip install ../FernetFile -e .
	./venv/bin/pip install ../NaclFile -e .
	./venv/bin/pip install ../AesFile -e .
	./venv/bin/pip install ../TinkFile -e .
	./venv/bin/pip install ../PyCoffer -e .

build:
	rm -rf dist
	./venv/bin/python3 -m build

testpypi:
	./venv/bin/python3 -m twine upload --repository testpypi --verbose dist/*

doc:
	./venv/bin/pdoc --output-directory docs cofferfile/decorator.py cofferfile/zstd.py cofferfile/__init__.py

pypi:
	./venv/bin/python3 -m twine upload --repository pypi --verbose dist/*

ruff:
	./venv/bin/ruff check cofferfile/

bandit:
	./venv/bin/bandit -r cofferfile

#~ tests: tests/test_cofferfile_fernet.py tests/test_naclfile_fernet.py
tests:
	./venv/bin/pytest  --random-order -n auto --ignore=tests/test_benchmark.py tests/

benchmark:
#~ 	./venv/bin/pip install .[benchmark]
	./venv/bin/pytest tests/test_benchmark.py

tests/test_fernetfile_fernet.py:
	cd tests && ln -s ../../FernetFile/tests/test_fernet.py test_fernetfile_fernet.py
	cd tests && ln -s ../../FernetFile/tests/test_cryptor.py test_fernetfile_cryptor.py
	cd tests && ln -s ../../FernetFile/tests/test_tar.py test_fernetfile_tar.py
	cd tests && ln -s ../../FernetFile/tests/test_zstd.py test_fernetfile_zstd.py
	cd tests && ln -s ../../FernetFile/tests/test_small_files.py test_fernetfile_small_files.py

tests/test_naclfile_pynacl.py:
	cd tests && ln -s ../../NaclFile/tests/test_pynacl.py test_naclfile_pynacl.py
	cd tests && ln -s ../../NaclFile/tests/test_cryptor.py test_naclfile_cryptor.py
	cd tests && ln -s ../../NaclFile/tests/test_tar.py test_naclfile_tar.py
	cd tests && ln -s ../../NaclFile/tests/test_zstd.py test_naclfile_zstd.py
	cd tests && ln -s ../../NaclFile/tests/test_small_files.py test_naclfile_small_files.py

tests/test_aesfile_aes.py:
	cd tests && ln -s ../../AesFile/tests/test_aes.py test_aesfile_aes.py
	cd tests && ln -s ../../AesFile/tests/test_cryptor.py test_aesfile_cryptor.py
	cd tests && ln -s ../../AesFile/tests/test_tar.py test_aesfile_tar.py
	cd tests && ln -s ../../AesFile/tests/test_zstd.py test_aesfile_zstd.py
	cd tests && ln -s ../../AesFile/tests/test_small_files.py test_aesfile_small_files.py

tests/test_tinkfile_tink.py:
	cd tests && ln -s ../../TinkFile/tests/test_tink.py test_tinkfile_tink.py
	cd tests && ln -s ../../TinkFile/tests/test_cryptor.py test_tinkfile_cryptor.py
	cd tests && ln -s ../../TinkFile/tests/test_tar.py test_tinkfile_tar.py
	cd tests && ln -s ../../TinkFile/tests/test_zstd.py test_tinkfile_zstd.py
	cd tests && ln -s ../../TinkFile/tests/test_small_files.py test_tinkfile_small_files.py

tests/test_pycoffer_market.py:
	cd tests && ln -s ../../PyCoffer/tests/test_market.py test_pycoffer_market.py
	cd tests && ln -s ../../PyCoffer/tests/test_bank.py test_pycoffer_bank.py
	cd tests && ln -s ../../PyCoffer/tests/test_store.py test_pycoffer_store.py
	cd tests && ln -s ../../PyCoffer/tests/test_coffer.py test_pycoffer_coffer.py

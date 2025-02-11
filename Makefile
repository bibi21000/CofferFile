#!/usr/bin/make -f
.PHONY: venv tests

venv:
	python3.12 -m venv venv
	./venv/bin/pip install -e .
	./venv/bin/pip install .[test]
	./venv/bin/pip install .[build]
	./venv/bin/pip install .[doc]
	./venv/bin/pip install .[zstd]
	./venv/bin/pip install .[store]
	./venv/bin/pip install .[pynacl]
	./venv/bin/pip install .[aes]
	./venv/bin/pip install .[cli]
	./venv/bin/pip install ../FernetFile -e .
	./venv/bin/pip install ../NaclFile -e .
	./venv/bin/pip install ../PyCoffer -e .

build:
	rm -rf dist
	./venv/bin/python3 -m build

testpypi:
	./venv/bin/python3 -m twine upload --repository testpypi --verbose dist/*

doc:
	./venv/bin/pdoc --output-directory docs cofferfile/aes.py cofferfile/decorator.py cofferfile/__init__.py

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
	./venv/bin/pip install .[benchmark]
	./venv/bin/pytest tests/test_benchmark.py

tests/test_fernetfile_fernet.py:
	cd tests && ln -s ../../FernetFile/tests/test_fernet.py test_fernetfile_fernet.py
	cd tests && ln -s ../../FernetFile/tests/test_tar.py test_fernetfile_tar.py
	cd tests && ln -s ../../FernetFile/tests/test_zstd.py test_fernetfile_zstd.py

tests/test_naclfile_fernet.py:
	cd tests && ln -s ../../NaclFile/tests/test_fernet.py test_nacl_fernet.py
	cd tests && ln -s ../../NaclFile/tests/test_tar.py test_nacl_tar.py
	cd tests && ln -s ../../NaclFile/tests/test_zstd.py test_nacl_zstd.py

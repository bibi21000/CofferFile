# -*- encoding: utf-8 -*-
import pytest

from cofferfile import EncryptFile, Cryptor

# ~ @pytest.fixture
class DummyFile(EncryptFile):

    @classmethod
    def cryptor_factory(self, name=None):
        """"""
        return Cryptor

    def __repr__(self):
        """"""
        s = repr(self.myfileobj)
        return '<DummyFile ' + s[1:-1] + ' ' + hex(id(self)) + '>'


@pytest.fixture
def random_path():
    """Create and return temporary directory"""
    import tempfile
    tmpdir = tempfile.TemporaryDirectory()
    yield tmpdir.name
    tmpdir.cleanup()

@pytest.fixture
def random_name():
    """Return a random string that can be used as filename"""
    import random
    import string
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

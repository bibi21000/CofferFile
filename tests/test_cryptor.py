# -*- encoding: utf-8 -*-
"""Test module

"""
import os
import io

from cofferfile import Cryptor

import pytest


def test_cryptor(random_path, random_name):
    cryptor = Cryptor()
    derive = cryptor.derive('test')

def test_cryptor_bad(random_path, random_name):
    cryptor = Cryptor()

    with pytest.raises(TypeError):
        derive = cryptor.derive(None)

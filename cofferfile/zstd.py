# *-* encoding: utf-8 *-*
"""Tools for zstd

"""
__author__ = 'bibi21000 aka Sébastien GALLET'
__email__ = 'bibi21000@gmail.com'

from pyzstd import CParameter, DParameter

def clean_level_or_option(level_or_option, mode='r'):
    if level_or_option is None:
        return
    ret = {}
    if 'r' in mode:
        for i in level_or_option:
            if not isinstance(i, DParameter):
                continue
            ret[i] = level_or_option[i]
    else:
        for i in level_or_option:
            if not isinstance(i, CParameter):
                continue
            ret[i] = level_or_option[i]

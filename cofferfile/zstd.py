# *-* encoding: utf-8 *-*
"""Tools for zstd

"""
__author__ = 'bibi21000 aka Sébastien GALLET'
__email__ = 'bibi21000@gmail.com'

import tarfile
from pyzstd import ZstdFile, CParameter, DParameter # noqa E401

class ZstdTarFile(tarfile.TarFile):
    def __init__(self, name, mode='r', fileobj=None, level_or_option=None, zstd_dict=None, **kwargs):

        self.zstd_file = ZstdFile(name, mode,
                                  level_or_option=clean_level_or_option(level_or_option, mode),
                                  zstd_dict=zstd_dict)
        try:
            super().__init__(fileobj=self.zstd_file, mode=mode.replace('b', ''), **kwargs)
        except Exception:
            self.zstd_file.close()
            raise

    def close(self):
        try:
            super().close()
        finally:
            self.zstd_file.close()


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
    if len(ret) == 0:
        return
    return ret

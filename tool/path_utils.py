import os
import posixpath
from pathlib import Path


def get_cygwin_path(path: Path):
    path_str = str(path)
    path_str = path_str.replace(os.sep, posixpath.sep)
    path_str = path_str.replace(':', '')

    return '/cygdrive/%s' % path_str

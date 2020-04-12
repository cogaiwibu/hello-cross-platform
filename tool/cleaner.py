import os
import shutil
from pathlib import Path

BUILD_DIR = ['build', '.cxx', '.gradle', 'CMakeFiles']


class Cleaner:
    def __init__(self, source_directory):
        self.source_directory = source_directory

    def clean_all(self):
        for directory in BUILD_DIR:
            self.clean(directory)

    def clean(self, regex):
        directory = list(Path(self.source_directory).rglob(regex))
        for sub_path in directory:
            self.clean_path(sub_path)

    def clean_path(self, path: Path):
        if path.is_dir():
            shutil.rmtree(str(path))
        elif path.exists():
            os.remove(str(path))

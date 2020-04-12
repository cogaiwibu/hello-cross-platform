import subprocess
from pathlib import Path

from cmake_utils import get_cmake_executable
from path_utils import get_cygwin_path
from project_generator import ProjectGenerator


class CygwinProjectGenerator(ProjectGenerator):
    def generate(self, source_directory: Path, build_directory: Path, profile: str):
        args = [get_cmake_executable(), get_cygwin_path(source_directory),
                '-DCMAKE_BUILD_TYPE=%s' % profile, '-B%s' % get_cygwin_path(Path(build_directory, 'unix'))]

        args += self.get_cmake_args()
        exit_code = subprocess.call(" ".join(args), shell=True, cwd=str(source_directory))
        if exit_code != 0:
            raise Exception("%s" % args)

    def get_cmake_args(self):
        return ['-DCMAKE_CXX_COMPILER_WORKS=TRUE', '-G', '"CodeBlocks - Unix Makefiles"']

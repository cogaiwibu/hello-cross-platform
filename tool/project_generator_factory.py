from pathlib import Path

from android_project_generator import AndroidProjectGenerator
from cygwin_project_generator import CygwinProjectGenerator
from ios_project_generator import IOSProjectGenerator
from unix_project_generator import UnixProjectGenerator


class ProjectGeneratorFactory:

    def generate(self, platform: str, source_directory: Path, build_directory: Path, profile: str):
        if platform == 'android':
            project_generator = AndroidProjectGenerator()
        elif platform == 'ios':
            project_generator = IOSProjectGenerator()
        elif platform == 'windows':
            project_generator = CygwinProjectGenerator()
        elif platform == 'osx' or platform == 'linux':
            project_generator = UnixProjectGenerator()
        else:
            raise Exception('Unsupported platform %s' % platform)

        project_generator.generate(source_directory, build_directory, profile)

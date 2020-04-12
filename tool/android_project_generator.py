import os
import shutil
from pathlib import Path

from jinja2 import Template

from project_generator import ProjectGenerator

CMAKE_LIST_FILE = 'CMakeLists.txt'
CMAKE_CONFIG = '"-DPLATFORM=ANDROID"'

JINJA2_EXTENSION = 'jinja2'


class AndroidProjectGenerator(ProjectGenerator):
    def __init__(self):
        self.sub_directory = 'android'

    def generate(self, source_directory: Path, build_directory: Path, profile: str):
        android_directory = Path(build_directory, self.sub_directory)
        if android_directory.exists():
            return

        self.clone_project(android_directory)
        self.write_template(android_directory, source_directory)

    def clone_project(self, android_directory):
        current_path = os.path.abspath(os.path.join(os.path.realpath(__file__), '..'))
        shutil.copytree(str(Path(current_path, self.sub_directory)), str(android_directory))

    def write_template(self, android_directory, source_directory: Path):
        jinja2_files = list(android_directory.rglob('*%s' % JINJA2_EXTENSION))
        for jinja2_file in jinja2_files:
            self.generate_jinja2(jinja2_file, source_directory)

    def generate_jinja2(self, jinja2_file: Path, source_directory: Path):
        template = Template(jinja2_file.read_text())

        output_content = template.render(
            cmake_list_path='%r' % str(Path(source_directory, CMAKE_LIST_FILE)),
            cmake_configuration=CMAKE_CONFIG
        )

        output = Path(str(jinja2_file).replace('.%s' % JINJA2_EXTENSION, ''))
        output.write_text(output_content)
        os.remove(str(jinja2_file))

import logging
from pathlib import Path

from build_executor import BuildExecutor
from gradle import Gradle


class AndroidBuildExecutor(BuildExecutor):
    def __init__(self, source_directory: Path):
        self.source_directory = source_directory
        self.build_directory = Path(source_directory, 'build')
        self.gradle = Gradle(Path(self.build_directory, 'android'))
        self.logger = logging.getLogger(__name__)

    def build(self, profile: str):
        self.gradle.run_task('assemble%s' % profile)

        output_apks = list(self.build_directory.rglob('exampleapp*%s*apk' % profile.lower()))
        if len(output_apks) != 1:
            raise Exception('Oop! Something went wrong')
        self.logger.info('Build completed, output %s', Path(output_apks[0]))

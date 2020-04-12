from abc import abstractmethod
from pathlib import Path


class ProjectGenerator:
    @abstractmethod
    def generate(self, source_directory: Path, build_directory: Path, profile: str):
        pass

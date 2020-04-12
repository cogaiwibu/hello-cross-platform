from abc import abstractmethod


class BuildExecutor:
    @abstractmethod
    def build(self, profile: str):
        pass

import importlib.metadata

class VersionUtil:
    @staticmethod
    def get_version():
        try:
            return importlib.metadata.version("lib-version")
        except importlib.metadata.PackageNotFoundError:
            return "dev"

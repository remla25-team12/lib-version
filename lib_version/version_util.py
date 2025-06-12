import importlib.metadata

class VersionUtil:
    _app_version = None

    @staticmethod
    def set_version(version):
        VersionUtil._app_version = version

    @staticmethod
    def get_version():
        if VersionUtil._app_version is not None:
            return VersionUtil._app_version

        try:
            return importlib.metadata.version("lib-version-remla25-team12")
        except importlib.metadata.PackageNotFoundError:
            return "dev"
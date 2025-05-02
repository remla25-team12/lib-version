from lib_version.version_util import VersionUtil

def test_version_returns_string():
    version = VersionUtil.get_version()
    assert isinstance(version, str)

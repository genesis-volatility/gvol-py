from gvol import GVol, __version__


def test_version():
    assert __version__ == "0.1.0"


def test_client_initialization():
    _ = GVol("gvol_api_key")

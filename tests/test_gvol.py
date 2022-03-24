from pathlib import Path

import toml
from gvol import GVol, __version__


def test_version():
    pyproject_path = Path(__file__).resolve().parents[1] / "pyproject.toml"

    with open(pyproject_path) as f:
        pyproject = toml.load(f)

    pyproject_version = pyproject["tool"]["poetry"]["version"]
    assert __version__ == pyproject_version


def test_client_initialization():
    _ = GVol("header", "gvol_api_key")

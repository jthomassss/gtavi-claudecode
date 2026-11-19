"""Every script must be valid Python with no byte-order mark."""
import ast
from pathlib import Path

import pytest

SCRIPTS = sorted((Path(__file__).resolve().parent.parent / "scripts").glob("*.py"))


def test_scripts_found():
    assert SCRIPTS, "no scripts found"


@pytest.mark.parametrize("path", SCRIPTS, ids=lambda p: p.name)
def test_script_parses_without_bom(path):
    raw = path.read_bytes()
    assert not raw.startswith(b"\xef\xbb\xbf"), f"{path.name} starts with a UTF-8 BOM"
    ast.parse(raw.decode("utf-8"), filename=str(path))

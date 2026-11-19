import sys
from pathlib import Path

# The scripts import each other as top-level modules (e.g. `from common import ...`).
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

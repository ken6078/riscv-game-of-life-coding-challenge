import subprocess
import sys
from pathlib import Path
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "game_of_life.py"


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )


def test_cli_no_show_success():
    cp = run_cli("--no-show", "--gens", "1", "--seed", "1")
    assert cp.returncode == 0
    assert "+" in cp.stdout
    assert "Alive:" in cp.stdout


def test_cli_invalid_rows_fails():
    cp = run_cli("--rows", "0", "--no-show")
    assert cp.returncode == 1
    assert "rows/cols must be > 0" in cp.stderr


def test_cli_invalid_prob_fails():
    cp = run_cli("--prob", "2", "--no-show")
    assert cp.returncode == 1
    assert "prob must be in [0, 1]" in cp.stderr

"""
Build student-analytics-platform.zip from the project directory.
Excludes caches, virtualenvs, local user data, and the output zip itself.
"""
from __future__ import annotations

import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent

SKIP_DIR_NAMES = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    "node_modules",
}

SKIP_FILE_NAMES = {
    "student_data.json",
    "users.json",
    "student-analytics-platform.zip",
}

SKIP_SUFFIXES = (".pyc", ".pyo")


def _skip(path: Path) -> bool:
    if any(part in SKIP_DIR_NAMES for part in path.parts):
        return True
    if path.name in SKIP_FILE_NAMES:
        return True
    if path.suffix in SKIP_SUFFIXES:
        return True
    return False


def create_project_zip(output_name: str = "student-analytics-platform.zip") -> Path:
    """Write a zip of the project next to this script. Returns the output path."""
    output_path = ROOT / output_name
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in ROOT.rglob("*"):
            if not path.is_file():
                continue
            try:
                rel = path.relative_to(ROOT)
            except ValueError:
                continue
            if _skip(path):
                continue
            zf.write(path, arcname=rel.as_posix())
    return output_path


if __name__ == "__main__":
    out = create_project_zip()
    print(f"Created {out} ({out.stat().st_size} bytes)")

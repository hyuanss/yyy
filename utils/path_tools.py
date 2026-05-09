from pathlib import Path


def get_abs_path(relative_path: str) -> str:
    """Resolve a project-relative path to an absolute path."""
    root = Path(__file__).resolve().parents[1]
    return str((root / relative_path).resolve())

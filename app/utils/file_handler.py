"""
Deprecated module.
Please import from top-level `utils` instead of `app.utils`.
This file is kept for backward compatibility.
"""
from utils.file_handler import (  # noqa: F401
    get_file_md5_hex,
    listdir_with_allowed_type,
    csv_loader,
    pdf_loader,
    txt_loader,
)

__all__ = [
    "get_file_md5_hex",
    "listdir_with_allowed_type",
    "csv_loader",
    "pdf_loader",
    "txt_loader",
]

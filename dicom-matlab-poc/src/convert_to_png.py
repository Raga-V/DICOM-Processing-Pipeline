"""Convert DICOM pixel array into PNG image."""

from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image


def convert_to_png(pixel_array: object, png_path: str | Path) -> Path:
    """Normalize pixel array to uint8 and write PNG."""
    if pixel_array is None:
        raise ValueError("Pixel data is required for PNG conversion.")

    target = Path(png_path)
    target.parent.mkdir(parents=True, exist_ok=True)

    arr = np.asarray(pixel_array, dtype=np.float64)
    if arr.size == 0:
        raise ValueError("Pixel array is empty.")

    # Reduce singleton dimensions and normalize common DICOM layouts.
    arr = np.squeeze(arr)
    if arr.ndim == 1:
        side = int(np.sqrt(arr.size))
        if side * side == arr.size:
            arr = arr.reshape((side, side))
        else:
            arr = arr.reshape((1, arr.size))
    elif arr.ndim == 3:
        if arr.shape[-1] not in (3, 4) and arr.shape[0] in (3, 4):
            arr = np.moveaxis(arr, 0, -1)
        elif arr.shape[-1] not in (3, 4):
            arr = arr[0]
    elif arr.ndim > 3:
        raise ValueError(f"Unsupported pixel array dimensions: {arr.shape}")

    min_val = float(arr.min())
    max_val = float(arr.max())

    if max_val == min_val:
        normalized = np.zeros_like(arr, dtype=np.uint8)
    else:
        normalized = ((arr - min_val) / (max_val - min_val) * 255.0).astype(np.uint8)

    try:
        image = Image.fromarray(normalized)
        image.save(target)
    except Exception as exc:  # pylint: disable=broad-except
        raise RuntimeError(f"Failed to write PNG {target}: {exc}") from exc

    return target

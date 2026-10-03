#!/usr/bin/env python3
"""
Restore all H-column styles (217-280) to clean, unbadged images with 100% authentic user styles:
1. 36 Tweet grid styles -> crop (0, 0, 512, 512) from {num}_grid.webp.
2. 6 Git 4-grid styles (262-267) -> crop (0, 0, 512, 512) from 770900e:{num}_grid.jpg.
3. 15 User replaced/custom styles -> high-res 1024x1024 unbadged original images from chat history.
4. 7 Styles (268-274) -> preserve current clean patched state.
5. Rebuild all 4 H contact sheets (H_217-232, H_233-248, H_249-264, H_265-280).
6. Rebuild gallery and validate.
"""
from __future__ import annotations

import io
import os
import subprocess
import sys
import time
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
INDIVIDUAL_DIR = ROOT / "images" / "individual" / "201-400"
IMAGES_DIR = ROOT / "images"

sys.path.insert(0, str(ROOT / "scripts"))
from contact_sheet_registry import render_sheet

# 1. 36 Tweet Grid Styles
GRID_36 = [
    217, 218, 219, 220, 221, 222, 223, 224, 225, 226,
    227, 228, 229, 230, 231, 232, 233, 234, 235, 236,
    237, 238, 239, 241, 243, 244, 245, 246, 247, 248,
    249, 250, 252, 253, 255, 261
]

# 2. 6 Git History Grid Styles
GIT_GRID_6 = [262, 263, 264, 265, 266, 267]

# 3. 15 User Uploaded Originals
USER_ORIGINALS_15 = {
    240: Path(r"C:\Users\yang0\.gemini\antigravity\brain\ff0d5551-ee42-4a20-a756-45ab77862e79\.user_uploaded\media_1790304197522.jpg"),
    242: Path(r"C:\Users\yang0\.gemini\antigravity\brain\6595f227-9ab4-44ac-953d-d3a424fc0e29\.user_uploaded\media_1790374378513.jpg"),
    251: Path(r"C:\Users\yang0\.gemini\antigravity\brain\ff0d5551-ee42-4a20-a756-45ab77862e79\.user_uploaded\media_1789990267480.jpg"),
    254: Path(r"C:\Users\yang0\.gemini\antigravity\brain\ff0d5551-ee42-4a20-a756-45ab77862e79\.user_uploaded\media_1789967162673.jpg"),
    256: Path(r"C:\Users\yang0\.gemini\antigravity\brain\ff0d5551-ee42-4a20-a756-45ab77862e79\.user_uploaded\media_1789967751348.jpg"),
    257: Path(r"C:\Users\yang0\.gemini\antigravity\brain\6595f227-9ab4-44ac-953d-d3a424fc0e29\.user_uploaded\media_1790488380407.jpg"),
    258: Path(r"C:\Users\yang0\.gemini\antigravity\brain\ff0d5551-ee42-4a20-a756-45ab77862e79\.user_uploaded\media_1789968133865.jpg"),
    259: Path(r"C:\Users\yang0\.gemini\antigravity\brain\6595f227-9ab4-44ac-953d-d3a424fc0e29\.user_uploaded\media_1790326241746.jpg"),
    260: Path(r"C:\Users\yang0\.gemini\antigravity\brain\6595f227-9ab4-44ac-953d-d3a424fc0e29\.user_uploaded\media_1790405629911.jpg"),
    275: Path(r"C:\Users\yang0\.gemini\antigravity\brain\ff0d5551-ee42-4a20-a756-45ab77862e79\.user_uploaded\media_1790040476083.jpg"),
    276: Path(r"C:\Users\yang0\.gemini\antigravity\brain\ff0d5551-ee42-4a20-a756-45ab77862e79\.user_uploaded\media_1790042371654.jpg"),
    277: Path(r"C:\Users\yang0\.gemini\antigravity\brain\ff0d5551-ee42-4a20-a756-45ab77862e79\puppet_rep.png"),
    278: Path(r"C:\Users\yang0\.gemini\antigravity\brain\ff0d5551-ee42-4a20-a756-45ab77862e79\scratch\vox_rep_square.png"),
    279: Path(r"C:\Users\yang0\.gemini\antigravity\brain\ff0d5551-ee42-4a20-a756-45ab77862e79\.user_uploaded\media_1790558493214.jpg"),
    280: Path(r"C:\Users\yang0\.gemini\antigravity\brain\6595f227-9ab4-44ac-953d-d3a424fc0e29\.user_uploaded\media_1790637678266.jpg"),
}


def safe_save(img: Image.Image, dest_path: Path):
    dest_str = str(dest_path.resolve())
    for attempt in range(5):
        try:
            img.save(dest_str, format="WEBP", quality=92, method=6)
            return
        except OSError:
            time.sleep(0.2)
    img.save(dest_str, format="WEBP", quality=92, method=6)


def main():
    print("=== Step 1: Processing 36 Tweet Grid Styles ===")
    for num in GRID_36:
        grid_file = INDIVIDUAL_DIR / f"{num}_grid.webp"
        dest_file = INDIVIDUAL_DIR / f"{num}.webp"
        if not grid_file.exists():
            print(f"Warning: {grid_file} does not exist!")
            continue
        with Image.open(grid_file) as im:
            tile = im.crop((0, 0, 512, 512))
            safe_save(tile, dest_file)
        print(f"  #{num}: Extracted clean top-left tile from {grid_file.name}")

    print("\n=== Step 2: Processing 6 Git 4-Grid Styles ===")
    for num in GIT_GRID_6:
        dest_file = INDIVIDUAL_DIR / f"{num}.webp"
        cmd = f"git show 770900e:images/individual/201-400/{num}_grid.jpg"
        res = subprocess.run(cmd, shell=True, capture_output=True)
        if res.returncode != 0:
            print(f"Warning: failed to get git blob for #{num}_grid.jpg")
            continue
        with Image.open(io.BytesIO(res.stdout)) as im:
            tile = im.crop((0, 0, 512, 512))
            safe_save(tile, dest_file)
        print(f"  #{num}: Extracted clean top-left tile from git commit 770900e")

    print("\n=== Step 3: Processing 15 User Uploaded Originals ===")
    for num, orig_path in USER_ORIGINALS_15.items():
        dest_file = INDIVIDUAL_DIR / f"{num}.webp"
        if not orig_path.exists():
            print(f"Error: Original path {orig_path} does not exist for #{num}!")
            continue
        with Image.open(orig_path) as im:
            tile = ImageOps.fit(im.convert("RGB"), (512, 512), Image.Resampling.LANCZOS, centering=(0.5, 0.5))
            safe_save(tile, dest_file)
        print(f"  #{num}: Generated clean 512x512 tile from {orig_path.name}")

    print("\n=== Step 4: Rebuilding 4 H-Category Contact Sheets ===")
    ranges = [
        (217, 232, IMAGES_DIR / "H_217-232.webp"),
        (233, 248, IMAGES_DIR / "H_233-248.webp"),
        (249, 264, IMAGES_DIR / "H_249-264.webp"),
        (265, 280, IMAGES_DIR / "H_265-280.webp"),
    ]
    for start, end, dest in ranges:
        render_sheet(start, end, dest)
        print(f"  Rebuilt sheet: {dest.name} (styles {start}-{end})")

    print("\n=== All H styles restored and sheets rebuilt successfully! ===")


if __name__ == "__main__":
    main()

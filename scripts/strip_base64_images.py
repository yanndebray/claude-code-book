#!/usr/bin/env python3
"""Strip base64-encoded images from Markdown files exported by Google Docs.

Replaces [imageN]: <data:image/...> references with readable placeholders
and keeps all other content intact. Writes to <original>.stripped.md.
"""
import re
import sys
from pathlib import Path


def strip_base64_images(filepath: Path) -> Path:
    text = filepath.read_text(encoding="utf-8")

    # Replace inline base64 image references: [imageN]: <data:image/png;base64,...>
    text = re.sub(
        r'^\[image(\d+)\]:\s*<data:image/[^>]+>',
        r'[image\1]: <!-- base64 image removed for AI processing -->',
        text,
        flags=re.MULTILINE,
    )

    # Replace any remaining inline base64 data URIs in image tags
    text = re.sub(
        r'!\[([^\]]*)\]\(data:image/[^)]+\)',
        r'![\1](<!-- base64 image removed -->)',
        text,
    )

    out = filepath.with_suffix(".stripped.md")
    out.write_text(text, encoding="utf-8")
    print(f"Stripped: {filepath} -> {out} ({filepath.stat().st_size:,} -> {out.stat().st_size:,} bytes)")
    return out


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 strip_base64_images.py <file.md> [file2.md ...]")
        sys.exit(1)
    for arg in sys.argv[1:]:
        strip_base64_images(Path(arg))

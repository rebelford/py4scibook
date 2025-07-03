import os
from pathlib import Path

# Settings
book_root = Path.cwd()
content_root = book_root / "content"
toc_path = book_root / "_toc.yml"

# Collect files
chapters = []
for dirpath, dirnames, filenames in os.walk(content_root):
    rel_dir = Path(dirpath).relative_to(content_root)
    # Sort files to control order
    notebooks = sorted([f for f in filenames if f.endswith(('.ipynb', '.md')) and not f.startswith('.')])
    for nb in notebooks:
        file_path = rel_dir / Path(nb).stem
        chapters.append(str(file_path).replace("\\", "/"))  # Windows compatibility

# Write TOC
with open(toc_path, "w") as f:
    f.write("format: jb-book\n")
    if "intro" in [Path(ch).stem for ch in chapters]:
        f.write("root: content/intro\n")
    else:
        f.write(f"root: {chapters[0]}\n")
    f.write("chapters:\n")
    for ch in chapters:
        if ch == "content/intro":
            continue
        f.write(f"  - file: content/{ch}\n")

print(f"✅ _toc.yml regenerated with {len(chapters)} entries.")

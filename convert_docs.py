import os
import subprocess
import re
from pathlib import Path

# Thư mục gốc chứa toàn bộ file docx
BASE_DIR = Path(r"C:\Users\NGUYEN THANH TAM\my-docs\Proxmox VE")
IMAGES_DIR = BASE_DIR / "images"
IMAGES_DIR.mkdir(exist_ok=True)

def convert_docx_to_md(docx_path):
    md_path = docx_path.with_suffix(".md")
    # chạy pandoc để convert
    subprocess.run([
        "pandoc", str(docx_path),
        "-t", "gfm",
        "-o", str(md_path),
        "--extract-media", str(IMAGES_DIR)
    ])
    print(f"✅ Converted: {docx_path.name} → {md_path.name}")
    return md_path

def fix_image_links(md_path):
    text = md_path.read_text(encoding="utf-8")

    # sửa link kiểu ./images/abc/image1.png → ./images/image1.png
    text = re.sub(r"!\[\]\((?:\.\./)*images[/\\][^)]*\)",
                  lambda m: "![](./images/" + os.path.basename(m.group(0).split("/")[-1]) + ")", text)

    md_path.write_text(text, encoding="utf-8")
    print(f"🔗 Fixed image links in: {md_path.name}")

def main():
    for root, _, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(".docx"):
                docx_path = Path(root) / file
                md_path = convert_docx_to_md(docx_path)
                fix_image_links(md_path)

if __name__ == "__main__":
    main()

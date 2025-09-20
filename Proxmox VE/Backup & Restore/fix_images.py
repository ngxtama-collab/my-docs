import os
import re

# Thư mục chứa các file Markdown
DOCS_DIR = "."

# Regex để bắt các đường dẫn ảnh kiểu Windows tuyệt đối
pattern = re.compile(r'src=".*?images\\media\\([^"]+)"')

def fix_markdown_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Thay bằng đường dẫn tương đối đến images/media
    new_content = pattern.sub(r'src="../../images/media/\1"', content)

    # Loại bỏ style inline (GitHub Markdown không support)
    new_content = re.sub(r'style="[^"]+"', '', new_content)

    if content != new_content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"✅ Fixed: {filepath}")
    else:
        print(f"✔ No change: {filepath}")

def main():
    for root, _, files in os.walk(DOCS_DIR):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                fix_markdown_file(filepath)

if __name__ == "__main__":
    main()

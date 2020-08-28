import os
import re
import shutil
from pathlib import Path
from typing import List

import fire


def main():
    """poetry run leetcode convert code.py codes"""
    fire.Fire({"convert": convert, "make_readme": make_readme, "make_code": make_code})


def convert(from_file: str = "code.py", to_dir="codes"):
    """code.pyを分解してファイルを作成

    :param from_file: 対象ファイル, defaults to "code.py"
    :param to_dir: 出力先, defaults to "codes"
    """
    os.makedirs(to_dir, exist_ok=True)
    if not Path(from_file).exists():
        print(f"Not found {from_file}")
        return
    with open(from_file) as fp:
        lines = fp.read().splitlines()
    pre, num, title = 0, 0, ""
    for i, line in enumerate(lines):
        if not re.search(r"^#\s*%%", line):
            continue
        if num:
            add_file(num, title, lines[pre:i], to_dir)
        pre, num, title = i, 0, ""
        m = re.match(r"#\s*%*\s*\[(\d+)\.\s*([^]]+)\]\([^)]+\)\s*", line)
        if m:
            pre, num, title = i, int(m.group(1)), m.group(2)
    if num:
        add_file(num, title, lines[pre:], to_dir)
    make_readme(to_dir)


def add_file(num: int, title: str, lines: List[str], to_dir: str):
    title = re.sub(r"[^a-zA-Z0-9 ]", "", title).strip()
    fnam = f"{to_dir}/{num:04}_{title.replace(' ', '_')}.py"
    n = len(lines)
    while n and not lines[n - 1]:
        n -= 1
    with open(fnam, "w", encoding="utf-8") as fp:
        fp.write("\n".join(lines[: n + 1]))


def make_readme(from_dir):
    """ディレクトリ内のファイルからREADMEを作成

    :param from_dir: 入力先
    """
    shutil.copy(".README.md", "README.md")
    with open("README.md", "a", encoding="utf-8") as fp:
        for fnam in sorted(Path(from_dir).glob("*")):
            with fnam.open(encoding="utf-8") as gp:
                line = gp.readline()
            if m := re.match(r"#\s*%*\s*\[(\d+)\.\s*([^]]+)\]\(([^)]+)\)\s*", line):
                s = f"{int(m.group(1)):04} {m.group(2)}"
                u = str(fnam).replace("\\", "/")
                fp.write(f"- [{s}]({u}) - ([leetcode.com]({m.group(3)}))\n")


def make_code(from_file: str, to_file: str = "code.py", drop_4spaces=False):
    """from_file→to_file"""
    if not (pth := Path(from_file)).exists():
        print(f"Not found {from_file}")
        return
    with open(to_file, "w") as fp:
        for line in pth.read_text().splitlines():
            if m := re.match(r"\[\**(\d+)\.\s*([^]\*]+)\**\]\(([^)]+)\)\s*", line):
                fp.write(f"# %% [{m.group(1)}. {m.group(2)}]({m.group(3)})\n")
            elif drop_4spaces and line.startswith("    "):
                fp.write(line[4:] + "\n")
            else:
                fp.write(line + "\n")

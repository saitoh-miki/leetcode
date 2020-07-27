import os
import re
import shutil
from pathlib import Path
from typing import List

import fire


def main():
    """poetry run leetcode convert code__.py codes_"""
    fire.Fire({"convert": convert, "make": make})


def convert(file: str = "code.py", dir_="codes"):
    """code.pyを分解してファイルを作成

    :param file: 対象ファイル, defaults to "code.py"
    :param dir_: 出力先, defaults to "codes"
    """
    os.makedirs(dir_, exist_ok=True)
    if not Path(file).exists():
        print(f"Not found {file}")
        return
    with open(file) as fp:
        lines = fp.read().splitlines()
    pre, num, title = 0, 0, ""
    for i, line in enumerate(lines):
        if not re.search(r"^#\s*%%", line):
            continue
        if num:
            add_file(num, title, lines[pre:i], dir_)
        pre, num, title = i, 0, ""
        m = re.match(r"#\s*%*\s*\[(\d+)\.\s*([^]]+)\]\([^)]+\)\s*", line)
        if m:
            pre, num, title = i, int(m.group(1)), m.group(2)
    if num:
        add_file(num, title, lines[pre:], dir_)
    shutil.copy(".README.md", "README.md")
    with open("README.md", "a", encoding="utf-8") as fp:
        for fnam in sorted(Path(dir_).glob("*")):
            with fnam.open(encoding="utf-8") as gp:
                line = gp.readline()
            if m := re.match(r"#\s*%*\s*\[(\d+)\.\s*([^]]+)\]\(([^)]+)\)\s*", line):
                s = f"{int(m.group(1)):04} {m.group(2)}"
                fp.write(f"- [{s}]({fnam}) - ([leetcode.com]({m.group(3)}))\n")


def add_file(num: int, title: str, lines: List[str], dir_: str):
    title = re.sub(r"[^a-zA-Z0-9 ]", "", title).strip()
    fnam = f"{dir_}/{num:04}_{title.replace(' ', '_')}.py"
    with open(fnam, "w", encoding="utf-8") as fp:
        fp.write("\n".join(lines))


def make(file: str):
    if not (pth := Path(file)).exists():
        print(f"Not found {file}")
        return
    with open("code_.py", "w") as fp:
        for line in pth.read_text().splitlines():
            if m := re.match(r"\[\**(\d+)\.\s*([^]\*]+)\**\]\(([^)]+)\)\s*", line):
                fp.write(f"# %% [{m.group(1)}. {m.group(2)}]({m.group(3)})\n")
            elif line.startswith("    "):
                fp.write(line[4:] + "\n")
            else:
                fp.write(line + "\n")

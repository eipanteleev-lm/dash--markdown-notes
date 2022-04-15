import os
import shutil

import utils


def template(name: str) -> str:
    fullpath = os.path.join("templates", f"{name}.md")

    with open(fullpath, encoding='utf-8') as f:
        md = f.read()

    return md
    
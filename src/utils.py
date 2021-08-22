import base64
import os
from typing import List
from urllib.parse import unquote

import config


def webpath_to_list(path: str) -> List[str]:
    return unquote(path).strip('/').split('/')


def webpath_to_notepath(path: str) -> str:
    pathlist = webpath_to_list(path)
    return os.path.join(config.NOTES_PATH, *pathlist)


def webpath_bread_crumps(path: str) -> list:
    bread_crumps = [("root", "/")]

    pathlist = webpath_to_list(path)
    href = ''
    for link in pathlist:
        href += '/' + link
        bread_crumps.append((link, href))

    return bread_crumps


def parse_note_file(contents, filename):
    _, content_string = contents.split(',')

    if filename.split('.')[-1] == 'md':
        return base64.b64decode(content_string)

    return None


def parse_file(contents):
    content_string = contents.split(',')[0]
    return base64.b64decode(content_string)

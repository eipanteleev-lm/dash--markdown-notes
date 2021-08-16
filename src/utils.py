import base64
import os
from urllib.parse import unquote

import config


def webpath_to_notepath(path: str) -> str:
    pathlist = unquote(path).strip('/').split('/')
    return os.path.join(config.NOTES_PATH, *pathlist)


def web_path_bread_crumps(path: str) -> list:
    bread_crumps = [("root", "/")]

    pathlist = unquote(path).strip('/').split('/')
    href = ''
    for link in pathlist:
        href += '/' + link
        bread_crumps.append((link, href))

    return bread_crumps


def parse_note_file(contents, filename):
    _, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)

    if filename.split('.')[-1] == 'md':
        return decoded.decode('utf-8')

    return None


def parse_file(contents):
    content_string = contents.split(',')[0]
    return base64.b64decode(content_string)

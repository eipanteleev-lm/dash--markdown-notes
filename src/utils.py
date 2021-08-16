import base64
import os

import config


def webpath_to_notepath(path: str) -> str:
    pathlist = path.strip('/').split('/')
    return os.path.join(config.NOTES_PATH, *pathlist)


def parse_note_file(contents, filename):
    _, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)

    if filename.split('.')[-1] == 'md':
        return decoded.decode('utf-8')

    return None


def parse_file(contents):
    content_string = contents.split(',')[0]
    return base64.b64decode(content_string)

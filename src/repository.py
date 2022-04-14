import os
import shutil

import utils


def note(path: str) -> str:
    fullpath = os.path.join(utils.webpath_to_notepath(path), "note.md")

    if not os.path.exists(fullpath):
        return None

    with open(fullpath, encoding='utf-8') as f:
        md = f.read()

    return md


def template(name: str) -> str:
    fullpath = os.path.join("templates", f"{name}.md")

    with open(fullpath, encoding='utf-8') as f:
        md = f.read()

    return md


def notes_tree(path: str='notes') -> list:
    return [
        (entry.name, notes_tree(entry.path))
        for entry in os.scandir(path)
        if entry.is_dir()
    ]


def files_list(path: str) -> list:
    fullpath = utils.webpath_to_notepath(path)
    return [
        filename
        for filename in os.listdir(fullpath)
        if (
            os.path.isfile(os.path.join(fullpath, filename))
            and filename != "note.md"
        )
    ]



def add_note_directory(path: str, name: str) -> str:
    fullpath = os.path.join(utils.webpath_to_notepath(path), name)

    if os.path.exists(fullpath):
        return None

    os.mkdir(fullpath)
    return path + '/' + name


def add_note(path: str, md: str):
    fullpath = os.path.join(utils.webpath_to_notepath(path), "note.md")

    with open(fullpath, 'wb') as f:
        f.write(md)

    return path


def add_file(path: str, contents: str, filename: str) -> str:
    fullpath = os.path.join(utils.webpath_to_notepath(path), filename)

    with open(fullpath, 'wb') as f:
        f.write(contents)

    return path


def clear_note(path: str) -> str:
    fullpath = os.path.join(utils.webpath_to_notepath(path), "note.md")

    if not os.path.exists(fullpath):
        return None

    os.remove(fullpath)
    return path


def delete_note(path: str) -> str:
    fullpath = os.path.join(utils.webpath_to_notepath(path))

    shutil.rmtree(fullpath)
    return path


def archive_folder(path: str) -> str:
    fullpath = os.path.join(utils.webpath_to_notepath(path))
    shutil.make_archive("notes", "zip", fullpath)
    return os.path.join("notes.zip")
    
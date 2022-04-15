import os
import shutil

from engines.base import BaseEngine

import utils


class FilesystemEngine(BaseEngine):

    def __init__(self, folder: str = "notes"):
        self.folder = folder

    def webpath_to_notepath(self, path: str):
        pathlist = utils.webpath_to_list(path)
        return os.path.join(self.folder, *pathlist)

    def note(self, path: str) -> str:
        fullpath = os.path.join(self.webpath_to_notepath(path), "note.md")

        if not os.path.exists(fullpath):
            return None

        with open(fullpath, encoding='utf-8') as f:
            md = f.read()

        return md

    def notes_tree(self, path: str='notes') -> list:
        return [
            (entry.name, self.notes_tree(entry.path))
            for entry in os.scandir(path)
            if entry.is_dir()
        ]

    def files_list(self, path: str) -> list:
        fullpath = self.webpath_to_notepath(path)
        return [
            filename
            for filename in os.listdir(fullpath)
            if (
                os.path.isfile(os.path.join(fullpath, filename))
                and filename != "note.md"
            )
        ]

    def add_note_directory(self, path: str, name: str) -> str:
        fullpath = os.path.join(self.webpath_to_notepath(path), name)

        if os.path.exists(fullpath):
            return None

        os.mkdir(fullpath)
        return path + '/' + name

    def add_note(self, path: str, md: str):
        fullpath = os.path.join(self.webpath_to_notepath(path), "note.md")

        with open(fullpath, 'wb') as f:
            f.write(md)

        return path

    def add_file(self, path: str, contents: str, filename: str) -> str:
        fullpath = os.path.join(self.webpath_to_notepath(path), filename)

        with open(fullpath, 'wb') as f:
            f.write(contents)

        return path

    def clear_note(self, path: str) -> str:
        fullpath = os.path.join(self.webpath_to_notepath(path), "note.md")

        if not os.path.exists(fullpath):
            return None

        os.remove(fullpath)
        return path

    def delete_note(self, path: str) -> str:
        fullpath = os.path.join(self.webpath_to_notepath(path))

        shutil.rmtree(fullpath)
        return path

    def archive_folder(self, path: str) -> str:
        fullpath = os.path.join(self.webpath_to_notepath(path))
        shutil.make_archive("notes", "zip", fullpath)
        return os.path.join("notes.zip")

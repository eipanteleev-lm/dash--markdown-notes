import json
import os
import shutil
from typing import List, Optional

from engines.base import BaseEngine, BaseEngineSettings

import models

import utils


class FilesystemEngineSettings(BaseEngineSettings):
    pass


class FilesystemEngine(BaseEngine):

    def __init__(self, settings: FilesystemEngineSettings):
        self.settings = settings

    def webpath_to_notepath(self, path: str) -> str:
        pathlist = utils.webpath_to_list(path)
        return os.path.join(self.settings.folder, *pathlist)

    def note(self, path: str) -> str:
        fullpath = os.path.join(
            self.webpath_to_notepath(path),
            self.settings.note_filename
        )

        if not os.path.exists(fullpath):
            return None

        with open(fullpath, encoding='utf-8') as f:
            md = f.read()

        return md

    def notes_tree(self, path: str=None) -> list:
        if path is None:
            path = self.settings.folder

        return [
            (entry.name, self.notes_tree(entry.path))
            for entry in os.scandir(path or self.settings.folder)
            if entry.is_dir()
        ]

    def files(self, path: str) -> List[str]:
        fullpath = self.webpath_to_notepath(path)
        return [
            filename
            for filename in os.listdir(fullpath)
            if (
                os.path.isfile(os.path.join(fullpath, filename))
                and filename not in (
                    self.settings.note_filename,
                    self.settings.metadata_filename
                )
            )
        ]

    def metadata(self, path: str) -> models.Metadata:
        fullpath = os.path.join(
            self.webpath_to_notepath(path),
            self.settings.metadata_filename
        )

        if not os.path.exists(fullpath):
            return models.Metadata()

        with open(fullpath) as f:
            metadata = models.Metadata(**json.load(f))

        return metadata

    def add_metadata(
        self,
        path: str,
        metadata: Optional[models.Metadata] = None
    ) -> models.Metadata:
        fullpath = os.path.join(
            self.webpath_to_notepath(path),
            self.settings.metadata_filename
        )

        metadata = metadata or models.Metadata()
        with open(fullpath, "w") as f:
            json.dump(metadata.dict(), f)

        return metadata

    def tags(self, path: str) -> List[str]:
        metadata = self.metadata(path)
        return metadata.tags

    def add_tag(self, path: str, tag: str) -> None:
        metadata = self.metadata(path)
        metadata.tags.append(tag)
        return self.add_metadata(path, metadata)

    def add_note_directory(self, path: str, name: str) -> str:
        fullpath = os.path.join(self.webpath_to_notepath(path), name)

        if os.path.exists(fullpath):
            return None

        os.mkdir(fullpath)
        return path + '/' + name

    def add_note(self, path: str, md: str):
        fullpath = os.path.join(
            self.webpath_to_notepath(path),
            self.settings.note_filename
        )

        with open(fullpath, 'wb') as f:
            f.write(md)

        return path

    def add_file(self, path: str, contents: str, filename: str) -> str:
        fullpath = os.path.join(self.webpath_to_notepath(path), filename)

        with open(fullpath, 'wb') as f:
            f.write(contents)

        return path

    def clear_note(self, path: str) -> str:
        fullpath = os.path.join(
            self.webpath_to_notepath(path),
            self.settings.note_filename
        )

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
        shutil.make_archive(
            self.settings.notes_archive_name,
            "zip",
            fullpath
        )

        return os.path.join(f"{self.settings.notes_archive_name}.zip")

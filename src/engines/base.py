from abc import ABCMeta, abstractmethod
from typing import List

import models

from pydantic import BaseSettings


class BaseEngineSettings(BaseSettings):
    folder: str = "notes"
    note_filename: str = "note.md"
    metadata_filename: str = "metadata.json"
    notes_archive_name: str = "notes"


class BaseEngine(metaclass=ABCMeta):

    def __init__(self, settings: BaseEngineSettings):
        self.settings = settings

    @abstractmethod
    def webpath_to_notepath(path: str):
        pass

    @abstractmethod
    def note(self, path: str) -> str:
        pass

    @abstractmethod
    def notes_tree(self, path: str):
        pass

    @abstractmethod
    def files(self, path: str) -> List[str]:
        pass

    @abstractmethod
    def metadata(self, path: str) -> models.Metadata:
        pass

    @abstractmethod
    def add_metadata(self, path: str) -> models.Metadata:
        pass

    @abstractmethod
    def tags(self, path: str) -> models.Tag:
        pass

    @abstractmethod
    def add_tag(self, path: str) -> models.Tag:
        pass

    @abstractmethod
    def delete_tag(self, tag: str) -> models.Tag:
        pass

    @abstractmethod
    def add_note_directory(self, path: str, name: str):
        pass

    @abstractmethod
    def add_note(self, path: str, md: str):
        pass

    @abstractmethod
    def add_file(self, path: str, contents: str, filename: str):
        pass

    @abstractmethod
    def clear_note(self, path: str):
        pass

    @abstractmethod
    def delete_note(self, path: str):
        pass

    @abstractmethod
    def archive_folder(self, path: str):
        pass

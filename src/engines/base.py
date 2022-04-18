from typing import List

from pydantic import BaseSettings


class BaseEngineSettings(BaseSettings):
    folder: str = "notes"
    note_filename: str = "note.md"
    metadata_filename: str = "metadata.json"
    notes_archive_name: str = "notes"


class BaseEngine:

    def __init__(self, settings: BaseEngineSettings):
        self.settings = settings

    def webpath_to_notepath(path: str):
        pass

    def note(self, path: str) -> str:
        pass

    def notes_tree(self, path: str):
        pass

    def files(self, path: str) -> List[str]:
        pass

    def add_note_directory(self, path: str, name: str):
        pass

    def add_note(self, path: str, md: str):
        pass

    def add_file(self, path: str, contents: str, filename: str):
        pass

    def clear_note(self, path: str):
        pass

    def delete_note(self, path: str):
        pass

    def archive_folder(self, path: str):
        pass

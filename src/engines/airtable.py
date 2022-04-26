from engines.base import BaseEngine, BaseEngineSettings
from engines.filesystem import FilesystemEngine


class AirtableEngineSettings(BaseEngineSettings):
    x_api_key: str = ...
    database_id: str = ...
    table_id: str = ...


class AirtableEngine(FilesystemEngine):

    def __init__(self, settings: AirtableEngineSettings):
        self.settings = settings
    
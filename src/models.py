from typing import List

from pydantic import BaseModel


class Tag(BaseModel):
    name: str = ...
    color: str = "secondary"


class Metadata(BaseModel):
    tags: List[Tag] = []

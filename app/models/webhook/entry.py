from pydantic import BaseModel
from typing import List
from .messaging import Messaging
class Entry(BaseModel):
    time: int
    id: str
    messaging: List[Messaging]
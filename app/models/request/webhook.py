from pydantic import BaseModel 
from typing import  List , Optional
from app.models.webhook.entry import Entry
class RequestBody(BaseModel):
    object: Optional[str] = None
    entry: List[Entry] 
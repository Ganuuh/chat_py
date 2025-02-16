from pydantic import    BaseModel
from typing import Optional

class Payload(BaseModel):
    url: str
    sticker_id: Optional[str] = None
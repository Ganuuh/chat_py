from pydantic import BaseModel
from .payload import Payload
class Attachment(BaseModel):
    type: str
    payload: Payload
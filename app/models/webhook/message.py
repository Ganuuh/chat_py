from pydantic import BaseModel
from  typing import Optional , List
from .attachment import Attachment
from .reply_to import ReplyTo
class Message(BaseModel):       
    mid: str
    text: Optional[str] = None
    attachments: Optional[List[Attachment]] = None
    reply_to: Optional[ReplyTo] = None
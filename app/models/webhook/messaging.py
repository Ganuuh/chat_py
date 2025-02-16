from pydantic import BaseModel
from .sender import Sender
from .recipient import Recipient
from typing import Optional
from .message import Message
from .postback import Postback
class Messaging(BaseModel):
    sender: Sender
    recipient: Recipient
    timestamp: int
    message: Optional[Message] = None
    postback: Optional[Postback] = None
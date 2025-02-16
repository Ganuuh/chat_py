from pydantic import BaseModel
class Postback(BaseModel):
    title: str
    payload: str
    mid: str
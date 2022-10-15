from pydantic import BaseModel
import json
import os

class Message(BaseModel):
    type: str | None = None
    msg: str
    color: str | None = None
    t_error: str | None = None
    
def make_message(msg: str, color: str | None = None, type: str | None = None, t_error: str | None = None) -> Message:
    return Message(type=type, msg=msg, color=color, t_error=t_error)

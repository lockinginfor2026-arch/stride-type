from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str

    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: Optional[str] = None


class RaceCreate(BaseModel):
    wpm: float 
    accuracy: float
    mode: str = "prose"

class RaceOut(RaceCreate):
    id: int
    timestamp: datetime
    user_id: int 

    model_config = ConfigDict(from_attributes=True)

class RaceStart(BaseModel):
    text: str
    bot_wpm: float
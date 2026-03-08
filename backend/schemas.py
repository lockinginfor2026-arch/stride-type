from pydantic import BaseModel, EmailStr
from typing import List, Optional

class UserCreate(BaseModel):
    username: str
    password: str

Class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
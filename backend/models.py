from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

class Race(Base):
    __tablename__  = "races"
    id = Column(Integer, primary_key=True, index=True)
    wpm = Column(Float)
    accuracy = Column(Float)
    mode = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="races")
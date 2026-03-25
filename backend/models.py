from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship, declarative_base, Mapped, mapped_column, MappedAsDataclass
from datetime import datetime, timezone
from sqlalchemy.sql import func
from backend.database import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))

    races: Mapped[list["Race"]] = relationship(back_populates="owner")
class Race(Base):
    __tablename__  = "races"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    wpm: Mapped[float] = mapped_column()
    accuracy: Mapped[float] = mapped_column()
    mode: Mapped[str] = mapped_column(default="prose")
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    owner: Mapped["User"] = relationship(back_populates="races")
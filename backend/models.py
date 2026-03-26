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
    last_equipped_skin: Mapped[str] = mapped_column(String(50), server_default="default")

    matches: Mapped[list["Match"]] = relationship(back_populates="player")

class Track(Base):
    __tablename__  = "tracks"
    
    #Both
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    content: Mapped[str] = mapped_column(Text)

    #separator
    mode: Mapped[str] = mapped_column(default="standard")

    #coding
    language: Mapped[str] = mapped_column(String(50), nullable=True)
    problem_number: Mapped[int] = mapped_column(nullable=True)
    title: Mapped[str] = mapped_column(String(255), nullable=True)
    difficulty: Mapped[str] = mapped_column(String(50), nullable=True)
    time_complexity: Mapped[str] = mapped_column(String(100), nullable=True)
    space_complexity: Mapped[str] = mapped_column(String(100), nullable=True)
    problem_type: Mapped[str] = mapped_column(String(100), nullable=True)

    match_history: Mapped[list["Match"]] = relationship(back_populates="track")

class Match(Base):
    __tablename__ = "matches"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    wpm: Mapped[float] = mapped_column()
    accuracy: Mapped[float] = mapped_column()
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    track_id: Mapped[int] = mapped_column(ForeignKey("tracks.id"))

    player: Mapped["User"] = relationship(back_populates="matches")
    track: Mapped["Track"] = relationship(back_populates="match_history")
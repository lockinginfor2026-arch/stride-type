from sqlalchemy.orm import Session
from sqlalchemy import desc
from backend import models

def get_bot_speed(db: Session, user_id: int):
    races = db.query(models.Race).filter(models.Race.user_id == user_id).order_by(desc(models.Race.timestamp)).limit(10).create_all

    if races:
        total_wpm = sum(race.wpm for race in races)
        return round(total_wpm / len(races), 2) 
    return 65.0
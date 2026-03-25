from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy import select
from backend import models, database, schemas, utils, auth, crud
from backend.database import engine, get_db
import time

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Stride Type API")

@app.get("/")
def hello():
    return {"Hello": "World"}

@app.post(("/signup"), response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    t0 = time.time()
    stmt = select(models.User).where(models.User.username == user.username)
    db_user = db.scalar(stmt)
    t1 = time.time()
    print(f"DEBUG: 1. DB Lookup took {t1 - t0:.4f}s")
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_pwd = utils.hash_password(user.password)
    t2 = time.time()
    print(f"DEBUG: 2. Hashing took {t2 - t1:.4f}s")
    new_user = models.User(username=user.username, hashed_password=hashed_pwd)
    db.add(new_user)
    db.commit()
    t3 = time.time()
    print(f"DEBUG: 3. DB Commit took {t3 - t2:.4f}s")
    db.refresh(new_user)
    t4 = time.time()
    print(f"DEBUG: 4. DB Refresh took {t4 - t3:.4f}s")
    
    print(f"DEBUG: TOTAL INTERNAL TIME: {t4 - t0:.4f}s")
    return new_user

@app.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    stmt = select(models.User).where(models.User.username == form_data.username)
    db_user = db.scalar(stmt)

    if not db_user or not utils.verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    
    access_token = auth.create_access_token(data={"sub": str(db_user.id)})
    return {"access_token": access_token, "token_type": "bearer"}

'''
@app.get("/race/start", response_model=schemas.RaceStart)
def start_new_race(db: Session = Depends(get_db), current_user: models.User = Depends(auth.get_current_user)):
    bot_wpm = crud.get_bot_speed(db, user_id=current_user.id)
    
    sample_text = "The quick brown fox jumps over the lazy dog."
    
    return {
        "text": sample_text,
        "bot_wpm": bot_wpm
    }

@app.post("/race/results", response_model=schemas.RaceOut)
def record_race_result(race_data: schemas.RaceCreate, db: Session = Depends(get_db), current_user: models.User = Depends(auth.get.current_user)):
    new_race = model.Race(wpm=race_data.wpm, accuracy=race_data.accuracy, mode=race_data.mode, user_id=current_user.id)
    db.add(new_race)
    db.commit()
    db.refresh(new_race)
    return new_race
'''
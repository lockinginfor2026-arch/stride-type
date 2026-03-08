from fastapi import FastAPI

app = FastAPI(title="Stride Type API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Race API!", "status": "online"}
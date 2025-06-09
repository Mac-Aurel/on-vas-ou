from fastapi import FastAPI
from app.db.init_db import init_db

app = FastAPI(
    title="On va où ? API",
    description="API backend pour l'application iOS sociale 'On va où ?'",
    version="1.0.0"
)

init_db()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API On va où ? 👋"}

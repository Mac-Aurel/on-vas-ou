from fastapi import FastAPI
from app.api import user_routes

app = FastAPI(title="On va où ? API")

app.include_router(user_routes.router, prefix="/users", tags=["Users"])

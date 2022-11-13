from fastapi import FastAPI
from api.routes import users

app = FastAPI()

app.include_router(
    users.router,
)

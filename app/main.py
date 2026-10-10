from fastapi import FastAPI

from app.database import Base, engine
from app import models
from app.routers import users, projects, tasks


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TaskFlow API",
    description="A project and task management backend API",
    version="1.0.0"
)

app.include_router(users.router)
app.include_router(projects.router)
app.include_router(tasks.router)


@app.get("/")
def home():
    return {
        "message": "TaskFlow API is running"
    }
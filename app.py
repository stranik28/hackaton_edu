from fastapi import FastAPI

from routers.university import router as university_router

app = FastAPI()

app.include_router(university_router)

from fastapi import FastAPI

from routers.university import router as university_router
from routers.type_question import router as type_question_router
from routers.answer import router as answer_router
from routers.question import router as question_router

app = FastAPI()

app.include_router(university_router)
app.include_router(type_question_router)
app.include_router(answer_router)
app.include_router(question_router)

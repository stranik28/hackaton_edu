from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app_bank import app2

from routers.university import router as university_router
from routers.address import router as address_router
from routers.speciality import router as speciality_router
from routers.ranked_list import router as ranked_list_router
from routers.user import router as user_router
from routers.ege import router as ege_router
from routers.exam import router as exam_router
from routers.type_question import router as type_question_router
from routers.answer import router as answer_router
from routers.question import router as question_router
from credits.nastya import router as front_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(university_router)
app.include_router(address_router)
app.include_router(speciality_router)
app.include_router(ranked_list_router)
app.include_router(user_router)
app.include_router(ege_router)
app.include_router(exam_router)
app.include_router(type_question_router)
app.include_router(answer_router)
app.include_router(question_router)
app.include_router(front_router)

app2.add_middleware(
    CORSMiddleware,
    allow_origins=['localhost, 194.31.174.209'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/bank", app2)

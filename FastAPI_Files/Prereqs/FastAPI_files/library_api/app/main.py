from fastapi import FastAPI
from app.controllers import book_controller

app = FastAPI(title="Library API")
app.include_router(book_controller.router)
from fastapi import FastAPI
from controllers import book_controller
from middleware.cors import add_cors_middleware

app = FastAPI(title="Library API")

#Add CORS middleware to the application
add_cors_middleware(app)

app.include_router(book_controller.router)  
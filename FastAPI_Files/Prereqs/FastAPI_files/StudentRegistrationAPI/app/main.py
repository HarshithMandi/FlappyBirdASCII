from fastapi import FastAPI
from routes import student_routes

app= FastAPI(title="Student Registration API", version="1.0.0")

@app.get("/")
def landing_page():
    return {"message": "Welcome to the Student Registration API!"}
app.include_router(student_routes.router)



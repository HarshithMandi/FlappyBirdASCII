from fastapi import FastAPI

from controllers.auth_controller import router as auth_router
from controllers.order_controller import router as order_router
from controllers.product_controller import router as product_router
from controllers.user_controller import router as user_router
from core.database import Database
from middleware.cors import add_cors


app = FastAPI()

add_cors(app)


@app.on_event("startup")
def startup():
    Database.connect()


@app.on_event("shutdown")
def shutdown():
    Database.disconnect()


# Routers already define their prefixes (e.g. /users, /products, /orders, /auth)
app.include_router(user_router)
app.include_router(product_router)
app.include_router(order_router)
app.include_router(auth_router)
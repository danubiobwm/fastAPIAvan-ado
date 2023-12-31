from fastapi import FastAPI
from app.routes.category_routes import router as category_routes

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World2"}

app.include_router(category_routes)
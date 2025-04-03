from fastapi import FastAPI
from src.api.contacts import router as contacts_router

app = FastAPI()

app.include_router(contacts_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Contact API"}

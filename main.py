from fastapi import FastAPI
from routers import router

app = FastAPI()

@app.get('/home')
def home():
    return {'message':'Hi'}

app.include_router(router)
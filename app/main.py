from fastapi import FastAPI
from app.image import img_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def hello_world():
    return {"msg": "Hai Domo~ Vitual youtuber Kizuna AI Desu!"}

app.include_router(img_router)
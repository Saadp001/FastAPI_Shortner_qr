from fastapi import FastAPI
from src.database import Base, engine
from src.routers import shortener, redirect
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# Create tables 
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(shortener.router)
app.include_router(redirect.router)

app.mount("/qr", StaticFiles(directory="qr_codes"), name="qr")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all domains for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"],
)

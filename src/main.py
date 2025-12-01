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

# app.mount("/qr", StaticFiles(directory="qr_codes"), name="qr")
from fastapi.responses import FileResponse

@app.get("/qr/{file_name}")
def get_qr(file_name: str):
    file_path = f"qr_codes/{file_name}"
    return FileResponse(path=file_path, media_type="image/png")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all domains for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"],
)

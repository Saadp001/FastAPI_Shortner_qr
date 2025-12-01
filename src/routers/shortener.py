from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import URL
from src.schemas import URLCreate, URLResponse, URLEdit
from src.utils import generate_short_code, generate_qr

router = APIRouter(prefix="/shorten", tags=["URL Shortener"])

@router.post("/", response_model=URLResponse)
def create_short_url(payload: URLCreate, db: Session = Depends(get_db)):

    long_url = payload.long_url

    # 1. Generate short code
    short = generate_short_code(long_url)
     
    # 2. Check if it already exists
    existing = db.query(URL).filter(URL.short_url == short).first()
    if existing:
        return existing

    # 3. Generate QR
    qr_path = generate_qr(short)

    # 4. Save to DB
    new_url = URL(
        long_url=long_url,
        short_url=short,
        qr_code=qr_path
    )

    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return new_url

@router.put("/{short_url}", response_model=URLResponse)
def update_url(short_url: str, payload: URLEdit, db: Session = Depends(get_db)):

    # Find existing entry
    url_entry = db.query(URL).filter(URL.short_url == short_url).first()
    if not url_entry:
        raise HTTPException(status_code=404, detail="URL not found")

    # Generate new short code
    new_short = generate_short_code(payload.new_long_url)

    # Generate new QR
    new_qr = generate_qr(new_short)

    # Update entry
    url_entry.long_url = payload.new_long_url
    url_entry.short_url = new_short
    url_entry.qr_code = new_qr

    db.commit()
    db.refresh(url_entry)

    return url_entry


@router.delete("/{short_url}")
def delete_url(short_url: str, db: Session = Depends(get_db)):

    url_entry = db.query(URL).filter(URL.short_url == short_url).first()
    if not url_entry:
        raise HTTPException(status_code=404, detail="URL not found")

    db.delete(url_entry)
    db.commit()

    return {"message": "URL deleted successfully"}

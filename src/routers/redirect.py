from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from src.database import get_db
from src.models import URL

router = APIRouter()

@router.get("/{short_url}")
def redirect_to_long(short_url: str, db: Session = Depends(get_db)):

    url_entry = db.query(URL).filter(URL.short_url == short_url).first()

    if not url_entry:
        raise HTTPException(status_code=404, detail="URL not found")

    return RedirectResponse(url_entry.long_url)

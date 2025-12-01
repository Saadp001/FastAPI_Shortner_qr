from sqlalchemy import Column, Integer, String, DateTime, func
from src.database import Base


class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    long_url = Column(String(2000), nullable=False)
    short_url = Column(String, unique=True, index=True)
    qr_code = Column(String, unique=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


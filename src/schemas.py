from pydantic import BaseModel

class URLCreate(BaseModel):
    long_url: str

class URLResponse(BaseModel):
    id: int
    long_url: str
    short_url: str
    qr_code: str

    class Config:
        orm_mode = True

class URLEdit(BaseModel):
    new_long_url: str

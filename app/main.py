from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException
from fastapi.responses import RedirectResponse

from sqlalchemy.orm import Session

from app.database import Base
from app.database import engine
from app.database import get_db

from app.schemas import URLRequest
from app.schemas import URLResponse

from app import crud

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="URL Shortener API",
    version="1.0.0",
    description="Simple URL Shortener using FastAPI and PostgreSQL"
)


@app.get("/")
def root():
    return {
        "message": "URL Shortener API",
        "docs": "/docs"
    }


@app.post("/shorten", response_model=URLResponse)
def shorten_url(
    request: URLRequest,
    db: Session = Depends(get_db)
):
    return crud.create_short_url(db, request.url)


@app.get("/{short_code}")
def redirect(
    short_code: str,
    db: Session = Depends(get_db)
):
    url = crud.get_original_url(db, short_code)

    if not url:
        raise HTTPException(
            status_code=404,
            detail="Short URL not found"
        )

    return RedirectResponse(
        url=url,
        status_code=307
    )
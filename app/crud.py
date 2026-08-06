from sqlalchemy.orm import Session

from app.models import URL
from app.utils import generate_short_code
from app.config import BASE_URL


def create_short_url(db: Session, original_url: str):
    # Check if URL already exists
    existing = (
        db.query(URL)
        .filter(URL.original_url == str(original_url))
        .first()
    )

    if existing:
        return {
            "short_url": f"{BASE_URL}/{existing.short_code}",
            "short_code": existing.short_code,
        }

    # Generate a unique short code
    while True:
        code = generate_short_code()

        exists = (
            db.query(URL)
            .filter(URL.short_code == code)
            .first()
        )

        if not exists:
            break

    new_url = URL(
        original_url=str(original_url),
        short_code=code,
    )

    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return {
        "short_url": f"{BASE_URL}/{new_url.short_code}",
        "short_code": new_url.short_code,
    }


def get_original_url(db: Session, short_code: str):
    url = (
        db.query(URL)
        .filter(URL.short_code == short_code)
        .first()
    )

    if url:
        return url.original_url

    return None
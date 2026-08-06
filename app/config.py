from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:password@localhost:5432/url_shortener"
)

BASE_URL = os.getenv(
    "BASE_URL",
    "http://localhost:8000"
)
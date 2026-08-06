# URL Shortener API

A simple URL Shortener API built with FastAPI and PostgreSQL.

## Features

- Shorten long URLs
- Redirect using short URLs
- PostgreSQL database
- Automatic URL validation
- Duplicate URL handling
- Swagger documentation

---

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic

---

## Installation

### 1. Clone the project

```bash
git clone <repository-url>

cd url-shortener-api
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file.

Example

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/url_shortener
BASE_URL=http://localhost:8000
```

---

### 5. Start PostgreSQL

Using Docker

```bash
docker-compose up -d
```

or use your own PostgreSQL installation.

---

### 6. Run the application

```bash
uvicorn app.main:app --reload
```

---

## API Documentation

Swagger UI

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

## API Endpoints

### POST /shorten

Request

```json
{
  "url": "https://www.google.com"
}
```

Response

```json
{
  "short_url": "http://localhost:8000/AbC123",
  "short_code": "AbC123"
}
```

---

### GET /{short_code}

Example

```
GET /AbC123
```

Redirects to the original URL.

---

## Database Schema

Table: urls

| Column | Type |
|---------|------|
| id | Integer |
| original_url | Text |
| short_code | String |
| created_at | Timestamp |

## Screenshots

Swagger UI:

![alt text](docs/swagger-ui.png)

![alt text](docs/image-3.png)

![alt text](docs/image-4.png)


Database:

![alt text](docs/database.png)

---

## Author

Sonali Sharma
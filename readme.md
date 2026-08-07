# URL Shortener API

A simple and efficient URL Shortener API built using **FastAPI** and **PostgreSQL**. The API generates unique short URLs, redirects users to the original destination, and stores URL mappings in a PostgreSQL database.

## Features

* Generate short URLs from long URLs
* Redirect users using short URLs
* PostgreSQL database for persistent storage
* Automatic URL validation using Pydantic
* Duplicate URL handling (returns the existing short URL for previously shortened URLs)
* Interactive API documentation with Swagger UI and ReDoc
* URL analytics with click count and creation timestamp *(Bonus Feature)*

---

## Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic
* Docker & Docker Compose
* Uvicorn

---

## Project Structure

```text
url-shortener-api/
│
├── app/
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── utils.py
│
├── docs/
│   ├── swagger-ui.png
│   ├── postman.png
│   └── database.png
│
├── .env.example
├── .gitignore
├── docker-compose.yml
├── README.md
└── requirements.txt
```

---

# Installation

## 1. Clone the repository

```bash
git clone <repository-url>
cd url-shortener-api
```

---

## 2. Create a virtual environment

```bash
python -m venv venv
```

### Activate the environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure environment variables

Create a `.env` file in the project root.

Example:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/url_shortener
BASE_URL=http://localhost:8000
```

Alternatively, copy the provided `.env.example` file.

---

## 5. Start PostgreSQL

Using Docker:

```bash
docker-compose up -d
```

Or use your local PostgreSQL installation.

---

## 6. Run the application

```bash
uvicorn app.main:app --reload
```

---

# API Documentation

Once the server is running:

**Swagger UI**

```
http://localhost:8000/docs
```

**ReDoc**

```
http://localhost:8000/redoc
```

---

# API Endpoints

## POST `/shorten`

Creates a shortened URL.

### Request

```json
{
  "url": "https://www.google.com"
}
```

### Response

```json
{
  "short_url": "http://localhost:8000/AbC123",
  "short_code": "AbC123"
}
```

---

## GET `/{short_code}`

Redirects the client to the original URL associated with the given short code.

Example:

```
GET /AbC123
```

**Response**

```
307 Temporary Redirect
```

---

## GET `/stats/{short_code}` *(Additional Feature)*

Returns metadata for a shortened URL.

### Example Response

```json
{
  "original_url": "https://www.google.com",
  "short_code": "AbC123",
  "click_count": 5,
  "created_at": "2026-08-07T11:30:15"
}
```

---

# Database Schema

**Table:** `urls`

| Column       | Type      |
| ------------ | --------- |
| id           | Integer   |
| original_url | String    |
| short_code   | String    |
| created_at   | Timestamp |
| click_count  | Integer   |

---

# Notes

* Duplicate URLs return the existing short URL instead of creating a new record.
* Invalid URLs are automatically rejected using Pydantic validation.
* The `GET /{short_code}` endpoint performs an HTTP redirect (`307 Temporary Redirect`).
* When testing redirects in Swagger UI, some browsers may display a **"Failed to fetch"** message because redirects to external websites are restricted by browser CORS policies. The redirect endpoint can be verified by opening the generated short URL directly in a browser or by using Postman.

---

# Screenshots

Add the following screenshots inside the `docs/` folder and reference them here:

### Swagger UI

![Swagger UI](docs/swagger-ui.png)

### POST /shorten (Postman)

![Postman](docs/postman.png)

### GET /{short_code} (Postman)

![Postman](docs/getredirect.png)

### URL Statistics Endpoint

![Stats](docs/stats.png)

### PostgreSQL Database

![Database](docs/database.png)

---

# Future Improvements

* Custom short codes
* URL expiration
* QR code generation
* User authentication
* Click analytics dashboard
* Rate limiting
* REST API versioning

---


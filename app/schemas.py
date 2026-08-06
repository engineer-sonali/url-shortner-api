from pydantic import BaseModel, HttpUrl


class URLRequest(BaseModel):
    url: HttpUrl


class URLResponse(BaseModel):
    short_url: str
    short_code: str
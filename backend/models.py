from pydantic import BaseModel

class NoteRequest(BaseModel):
    content: str

class NoteResponse(BaseModel):
    summary: str
    keywords: list[str]
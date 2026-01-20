from fastapi import APIRouter
from ..models import NoteRequest, NoteResponse
from ..services.ai_notes import generate_summary, extract_keywords

router = APIRouter(prefix="/notes")

@router.post("/", response_model=NoteResponse)
async def create_notes(payload: NoteRequest):
    return NoteResponse(summary=generate_summary(payload.content), keywords=extract_keywords(payload.content))
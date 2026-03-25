from fastapi import APIRouter, Depends, HTTPException

from app.dependencies.service_dependency import get_participant_service
from app.schemas.participant_schema import ParticipantCreate, ParticipantResponse
from app.services.participant_service import ParticipantService

router = APIRouter(prefix="/participants", tags=["participants"])


@router.post("", response_model=ParticipantResponse, status_code=201)
def register_participant(
    payload: ParticipantCreate,
    service: ParticipantService = Depends(get_participant_service),
) -> ParticipantResponse:
    try:
        return service.register_participant(payload)
    except ValueError as exc:
        detail = str(exc)
        status_code = 404 if detail == "Event not found" else 400
        raise HTTPException(status_code=status_code, detail=detail)


@router.get("/{participant_id}", response_model=ParticipantResponse)
def get_participant(
    participant_id: int,
    service: ParticipantService = Depends(get_participant_service),
) -> ParticipantResponse:
    try:
        return service.get_participant(participant_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))

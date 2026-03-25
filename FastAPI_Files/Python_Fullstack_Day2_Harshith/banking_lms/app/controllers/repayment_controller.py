from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.application_repository import ApplicationRepository
from app.repositories.repayment_repository import RepaymentRepository
from app.schemas.repayment_schema import RepaymentCreate, RepaymentOut
from app.services.repayment_service import RepaymentService

router = APIRouter()


def get_service() -> RepaymentService:
    return RepaymentService(RepaymentRepository(), ApplicationRepository())


@router.post("", response_model=RepaymentOut)
def add_repayment(payload: RepaymentCreate, db: Session = Depends(get_db)):
    return get_service().add_repayment(db, payload)

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.application_repository import ApplicationRepository
from app.repositories.product_repository import ProductRepository
from app.repositories.repayment_repository import RepaymentRepository
from app.repositories.user_repository import UserRepository
from app.schemas.application_schema import LoanApplicationCreate, LoanApplicationOut, LoanApplicationStatusUpdate
from app.schemas.repayment_schema import RepaymentOut
from app.services.repayment_service import RepaymentService
from app.services.application_service import ApplicationService

router = APIRouter()


def get_service() -> ApplicationService:
    return ApplicationService(
        ApplicationRepository(),
        UserRepository(),
        ProductRepository(),
        RepaymentRepository(),
    )


def get_repayment_service() -> RepaymentService:
    return RepaymentService(RepaymentRepository(), ApplicationRepository())


@router.post("", response_model=LoanApplicationOut)
def create_application(payload: LoanApplicationCreate, db: Session = Depends(get_db)):
    return get_service().create_application(db, payload)


@router.get("/{application_id}", response_model=LoanApplicationOut)
def get_application(application_id: int, db: Session = Depends(get_db)):
    return get_service().get_application(db, application_id)


@router.get("", response_model=list[LoanApplicationOut])
def list_applications(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_service().list_applications(db, skip, limit)


@router.put("/{application_id}/status", response_model=LoanApplicationOut)
def update_application_status(
    application_id: int,
    payload: LoanApplicationStatusUpdate,
    db: Session = Depends(get_db),
):
    return get_service().update_status(db, application_id, payload)


@router.get("/{application_id}/repayments", response_model=list[RepaymentOut])
def list_repayments(application_id: int, db: Session = Depends(get_db)):
    return get_repayment_service().list_repayments(db, application_id)

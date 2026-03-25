from fastapi import APIRouter, Depends, HTTPException

from app.dependencies.loan_dependency import get_loan_service
from app.schemas.loan_schema import LoanCreate, LoanResponse, LoanStatusResponse
from app.services.loan_service import LoanService

router = APIRouter(prefix="/loans", tags=["loans"])


@router.post("", response_model=LoanResponse, status_code=201)
def submit_application(
    payload: LoanCreate,
    service: LoanService = Depends(get_loan_service),
) -> LoanResponse:
    try:
        return service.submit_application(payload)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@router.get("", response_model=list[LoanResponse])
def list_applications(
    service: LoanService = Depends(get_loan_service),
) -> list[LoanResponse]:
    return service.list_applications()


@router.get("/{loan_id}", response_model=LoanResponse)
def get_application(
    loan_id: int,
    service: LoanService = Depends(get_loan_service),
) -> LoanResponse:
    try:
        return service.get_application(loan_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))


@router.put("/{loan_id}/approve", response_model=LoanStatusResponse)
def approve_loan(
    loan_id: int,
    service: LoanService = Depends(get_loan_service),
) -> LoanStatusResponse:
    try:
        return service.approve(loan_id)
    except ValueError as exc:
        detail = str(exc)
        status_code = 404 if detail == "Loan application not found" else 400
        raise HTTPException(status_code=status_code, detail=detail)


@router.put("/{loan_id}/reject", response_model=LoanStatusResponse)
def reject_loan(
    loan_id: int,
    service: LoanService = Depends(get_loan_service),
) -> LoanStatusResponse:
    try:
        return service.reject(loan_id)
    except ValueError as exc:
        detail = str(exc)
        status_code = 404 if detail == "Loan application not found" else 400
        raise HTTPException(status_code=status_code, detail=detail)

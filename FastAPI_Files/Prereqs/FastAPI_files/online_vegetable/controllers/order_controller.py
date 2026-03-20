from fastapi import APIRouter, Depends, HTTPException
from schemas.order_schema import OrderCreate, OrderOut
from services.order_service import OrderService
from core.dependencies import get_order_service
from core.auth import get_current_user


router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/", response_model=OrderOut)
async def create_order(order: OrderCreate, service: OrderService = Depends(get_order_service), current_user = Depends(get_current_user)):
    order_id = await service.create_order(order)
    return {"id": order_id, **order.dict(), "status": "pending"}

@router.get("/{order_id}", response_model=OrderOut)
async def get_order(order_id: str, service: OrderService = Depends(get_order_service)):
    order = await service.get_order_by_id(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


    
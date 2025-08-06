from fastapi import APIRouter, Request
from pydantic import BaseModel, Field
from typing import Optional

router = APIRouter()

# PUBLIC_INTERFACE
class PaymentRequest(BaseModel):
    plan_id: str = Field(..., description="ID for subscription/plan")
    payment_method: str = Field(..., description="Payment method (card/paypal/etc)")

# PUBLIC_INTERFACE
class PaymentStatusResponse(BaseModel):
    status: str
    transaction_id: Optional[str]

@router.post("/subscribe", response_model=PaymentStatusResponse, summary="Start subscription payment")
def subscribe(data: PaymentRequest):
    """
    Initiate a payment for premium plan.
    """
    # (Stub: Would call third-party payment API)
    return PaymentStatusResponse(status="pending", transaction_id="fake-txn-123")

@router.post("/webhook", summary="Payment provider webhook (backend)")
async def payment_webhook(request: Request):
    """
    Listen for payment notifications from payment provider.
    """
    await request.body()
    # (Stub: Would validate signature, process event)
    return {"ok": True}

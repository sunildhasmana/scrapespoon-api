from fastapi import APIRouter, HTTPException
import stripe
import os

router = APIRouter()

stripe.api_key = os.environ.get("STRIPE_API_KEY")  # Set in env vars

@router.post("/create-checkout-session")
def create_checkout_session(email: str, plan: str):
    try:
        session = stripe.checkout.Session.create(
            customer_email=email,
            line_items=[{"price": plan, "quantity": 1}],
            mode="subscription",
            success_url="https://www.scrapespoon.com/dashboard?success=true",
            cancel_url="https://www.scrapespoon.com/dashboard?canceled=true"
        )
        return {"session_id": session.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


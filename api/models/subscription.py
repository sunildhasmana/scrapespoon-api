from pydantic import BaseModel
from datetime import datetime

class Subscription(BaseModel):
    user_id: str
    plan: str
    status: str = "inactive"
    stripe_subscription_id: str
    start_date: datetime
    end_date: datetime

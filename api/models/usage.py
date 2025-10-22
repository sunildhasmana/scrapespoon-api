from pydantic import BaseModel
from datetime import datetime

class Usage(BaseModel):
    user_id: str
    endpoint: str
    timestamp: datetime = datetime.utcnow()

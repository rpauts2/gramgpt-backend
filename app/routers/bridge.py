from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class BridgeMessage(BaseModel):
    action: str
    data: Optional[dict] = None

@router.post("/send")
async def bridge_send(msg: BridgeMessage):
    return {"status": "ok", "action": msg.action}

@router.get("/status")
async def bridge_status():
    return {"connected": True, "modules": 16}

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional, List
import asyncio
import random

router = APIRouter()

class StartTask(BaseModel):
    channels: Optional[List[str]] = None
    tone: Optional[str] = "expert"
    model: Optional[str] = "gpt-4o"
    frequency: Optional[str] = "every_2nd"
    target: Optional[str] = None
    text: Optional[str] = None
    delay: Optional[str] = None

active_tasks = {}

@router.post("/commenting/start")
async def start_commenting(data: StartTask):
    task_id = f"comment_{random.randint(1000,9999)}"
    active_tasks[task_id] = {"status": "running", "type": "commenting", "config": data.dict()}
    return {"task_id": task_id, "status": "started"}

@router.post("/commenting/stop")
async def stop_commenting():
    for tid, task in active_tasks.items():
        if task["type"] == "commenting":
            task["status"] = "stopped"
    return {"status": "stopped"}

@router.get("/commenting/logs")
async def get_commenting_logs():
    return [
        {"channel": "crypto_signals", "comment": "Отличный анализ! BTC выглядит сильно на фоне DXY.", "likes": 14, "replies": 3, "time": 1718900000},
        {"channel": "trading_chat", "comment": "Солидарен. ETH/BTC pair показывает дивергенцию.", "likes": 8, "replies": 1, "time": 1718899500},
    ]

@router.post("/chatting/start")
async def start_chatting(data: StartTask):
    task_id = f"chat_{random.randint(1000,9999)}"
    active_tasks[task_id] = {"status": "running", "type": "chatting"}
    return {"task_id": task_id, "status": "started"}

@router.post("/chatting/stop")
async def stop_chatting():
    return {"status": "stopped"}

@router.get("/chatting/stats")
async def get_chatting_stats():
    return {"messages": 1247, "groups": 8, "replies": 892}

@router.get("/chatting/groups")
async def get_chatting_groups():
    return [
        {"name": "Crypto Traders RU", "members": 15420, "msgs_per_hour": 45, "status": "active"},
        {"name": "BTC Mining", "members": 8900, "msgs_per_hour": 22, "status": "active"},
    ]

@router.post("/parsing/start")
async def start_parsing(data: StartTask):
    task_id = f"parse_{random.randint(1000,9999)}"
    active_tasks[task_id] = {"status": "running", "type": "parsing", "config": data.dict()}
    return {"task_id": task_id, "status": "started"}

@router.get("/parsing/results/{task_id}")
async def get_parsing_results(task_id: str):
    return {
        "status": "completed",
        "total_found": 2847,
        "results": [
            {"first_name": "Алексей", "username": "alex_trader", "source": "crypto_signals"},
            {"first_name": "Мария", "username": "maria_crypto", "source": "btc_news"},
            {"first_name": "Дмитрий", "username": "dima_trade", "source": "trading_chat"},
        ]
    }

@router.post("/warmup/start")
async def start_warmup():
    return {"status": "started", "accounts": 5}

@router.post("/warmup/stop")
async def stop_warmup():
    return {"status": "stopped"}

@router.get("/warmup/accounts")
async def get_warmup_accounts():
    return {
        "stats": {"avg_progress": 78, "active": 5, "total_dialogs": 1247, "bans": 0},
        "accounts": [
            {"phone": "+7***1234", "trust_score": 92, "status": "active", "total_dialogs": 342},
            {"phone": "+7***5678", "trust_score": 85, "status": "active", "total_dialogs": 287},
            {"phone": "+7***9012", "trust_score": 67, "status": "warmup", "total_dialogs": 156},
        ]
    }

@router.post("/spammer/start")
async def start_spammer(data: StartTask):
    return {"status": "started"}

@router.post("/spammer/stop")
async def stop_spammer():
    return {"status": "stopped"}

@router.post("/subscribers/start")
async def start_subscribers(data: StartTask):
    return {"status": "started"}

@router.post("/subscribers/stop")
async def stop_subscribers():
    return {"status": "stopped"}

@router.post("/autoreg/start")
async def start_autoreg(data: StartTask):
    return {"status": "started"}

@router.post("/autoreg/stop")
async def stop_autoreg():
    return {"status": "stopped"}

@router.post("/converter/start")
async def start_converter(data: StartTask):
    return {"status": "completed", "converted": 15}

@router.post("/bypass2fa/start")
async def start_bypass2fa():
    return {"status": "started"}

@router.post("/reporter/start")
async def start_reporter(data: StartTask):
    return {"status": "started"}

from fastapi import APIRouter
import random
from datetime import datetime

router = APIRouter()

@router.get("/security/status")
async def security_status():
    return {
        "risk_level": "low",
        "risk_score": 2.1,
        "human_like": 99.2,
        "bans_30d": 0,
        "days_without_ban": 127,
    }

@router.get("/analytics/summary")
async def analytics_summary():
    return {
        "leads_captured": 12847,
        "active_accounts": 1482,
        "total_accounts": 2100,
        "roi_average": "240%",
        "posts_today": 8304,
        "comments_today": 1247,
        "reactions_today": 3891,
    }

@router.get("/dashboard/chart")
async def dashboard_chart():
    return {
        "labels": ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"],
        "actions": [1200, 1800, 1400, 2200, 1600, 2500, 1900],
        "leads": [45, 67, 52, 89, 61, 95, 73],
    }

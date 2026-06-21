from fastapi import APIRouter
from typing import Optional

router = APIRouter()

@router.get("/list")
async def list_models():
    return [
        {"id": "gpt-4o", "name": "GPT-4o", "provider": "OpenAI", "speed": "fast", "quality": "high"},
        {"id": "gpt-4o-mini", "name": "GPT-4o Mini", "provider": "OpenAI", "speed": "very_fast", "quality": "medium"},
        {"id": "cerebras", "name": "Cerebras Llama", "provider": "Cerebras", "speed": "ultra_fast", "quality": "high"},
    ]

@router.get("/{model_id}")
async def get_model(model_id: str):
    models = {
        "gpt-4o": {"id": "gpt-4o", "name": "GPT-4o", "tokens_per_sec": 80},
        "gpt-4o-mini": {"id": "gpt-4o-mini", "name": "GPT-4o Mini", "tokens_per_sec": 150},
        "cerebras": {"id": "cerebras", "name": "Cerebras Llama", "tokens_per_sec": 210},
    }
    return models.get(model_id, {"error": "Model not found"})

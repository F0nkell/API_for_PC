from fastapi import APIRouter, Depends
from pydantic import BaseModel
from core.security import verify_api_key
from services.browser import browser_manager

# Передаем зависимости через list()
router = APIRouter(
    dependencies=list((Depends(verify_api_key),))
)

class NavigateRequest(BaseModel):
    url: str

@router.post("/goto")
async def navigate(req: NavigateRequest):
    return await browser_manager.goto(req.url)

@router.get("/content")
async def get_content():
    return await browser_manager.get_content()

@router.get("/screenshot")
async def take_screenshot():
    return await browser_manager.screenshot()
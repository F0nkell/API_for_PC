from fastapi import APIRouter, Depends
from pydantic import BaseModel
from core.security import verify_api_key
from services import files

router = APIRouter(
    dependencies=list((Depends(verify_api_key),))
)

class WriteRequest(BaseModel):
    path: str
    content: str

@router.get("/read")
async def read_file(path: str):
    return await files.read_file(path)

@router.post("/write")
async def write_file(req: WriteRequest):
    return await files.write_file(req.path, req.content)

@router.get("/list")
async def list_directory(path: str = ""):
    # Если path пустой, покажет корень WORKSPACE_ROOT
    return await files.list_dir(path)
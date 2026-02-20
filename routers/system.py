from fastapi import APIRouter, Depends
from pydantic import BaseModel
from core.security import verify_api_key
from services.shell import execute_command
from services.workspace import open_in_vscode, git_status

router = APIRouter(dependencies=[Depends(verify_api_key)])

class CommandRequest(BaseModel):
    command: str
    cwd: str | None = None
    timeout: int = 30

@router.post("/execute")
async def run_shell_command(req: CommandRequest):
    return await execute_command(req.command, req.cwd, req.timeout)

@router.post("/vscode/open")
async def vscode_open(project_name: str):
    return await open_in_vscode(project_name)

@router.get("/git/status")
async def get_git_status(project_name: str):
    return await git_status(project_name)
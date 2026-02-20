from services.shell import execute_command
from core.config import settings
import os

async def open_in_vscode(project_name: str):
    target_path = os.path.join(settings.WORKSPACE_ROOT, project_name)
    if not os.path.exists(target_path):
        return {"error": f"Path {target_path} does not exist."}
    
    # Вызываем VS Code CLI
    return await execute_command(f"code {target_path}")

async def git_status(project_name: str):
    target_path = os.path.join(settings.WORKSPACE_ROOT, project_name)
    return await execute_command("git status", cwd=target_path)
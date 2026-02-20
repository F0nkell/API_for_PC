import os
from core.config import settings

def resolve_path(relative_path: str):
    # Защита: бот не сможет выйти за пределы WORKSPACE_ROOT используя "../"
    base = os.path.abspath(settings.WORKSPACE_ROOT)
    target = os.path.abspath(os.path.join(base, relative_path))
    
    if not target.startswith(base):
        raise ValueError("Security Error: Access denied outside WORKSPACE_ROOT")
    return target

async def read_file(file_path: str):
    try:
        target = resolve_path(file_path)
        with open(target, "r", encoding="utf-8") as f:
            content = f.read()
        return dict(status="success", content=content)
    except Exception as e:
        return dict(status="error", detail=str(e))

async def write_file(file_path: str, content: str):
    try:
        target = resolve_path(file_path)
        # Создаем папки, если их нет
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "w", encoding="utf-8") as f:
            f.write(content)
        return dict(status="success")
    except Exception as e:
        return dict(status="error", detail=str(e))

async def list_dir(dir_path: str):
    try:
        target = resolve_path(dir_path)
        items = os.listdir(target)
        return dict(status="success", items=list(items))
    except Exception as e:
        return dict(status="error", detail=str(e))
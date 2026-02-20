import asyncio
import subprocess
from typing import Dict, Any

async def execute_command(command: str, cwd: str = None, timeout: int = 30) -> Dict:
    """Выполняет shell команду с таймаутом."""
    try:
        process = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd=cwd
        )
        
        stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=timeout)
        
        return {
            "status": "success" if process.returncode == 0 else "error",
            "return_code": process.returncode,
            "stdout": stdout.decode().strip(),
            "stderr": stderr.decode().strip()
        }
    except asyncio.TimeoutError:
        process.kill()
        return {"status": "error", "return_code": -1, "stdout": "", "stderr": f"Command timed out after {timeout}s"}
    except Exception as e:
        return {"status": "error", "return_code": -1, "stdout": "", "stderr": str(e)}
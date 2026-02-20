<div align="center">

# 🦁 OpenClaw Local API Core

**The Missing Link Between LLMs and Your Operating System.**  
*Production-Ready, Async, Secure Gateway for AI Agents.*

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Playwright](https://img.shields.io/badge/Playwright-Enabled-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)](https://playwright.dev/)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Security](#-security-architecture)

</div>

---

## ⚡ What is OpenClaw API?

OpenClaw API is a **local, high-performance middleware** designed to give AI Agents (like GPT-4, Claude, or local LLMs) controlled access to your computer. 

Most agents are trapped in a chat window. **OpenClaw gives them hands and eyes.** It allows an LLM to:
1.  **See:** Browse the web, take screenshots, and read DOM elements via Playwright.
2.  **Touch:** Create files, manage project structures, and edit code safely.
3.  **Act:** Execute shell commands, run Git operations, and open VS Code projects.

> **Warning:** This is a powerful tool. It provides a bridge between AI and your shell. While we have implemented strict sandboxing, use it responsibly.

---

## 🚀 Features

### 🌐 Web Module (The Eyes)
Powered by **Playwright** (Chromium), not Selenium.
- **Persistent Context:** Logs in once, keeps cookies/sessions forever. Your agent can access private GitHub repos or Jira tickets.
- **Computer Vision Ready:** `/screenshot` endpoint returns Base64 images for multimodal LLMs.
- **Stealth Mode:** Uses real browser signatures to avoid bot detection.

### 💻 System Module (The Hands)
- **Shell Execution:** Async subprocess management with strict **Timeouts (Circuit Breaker)** to prevent freezing.
- **VS Code Integration:** Open projects instantly via CLI.
- **Git Awareness:** Check status and manage repositories.

### 📂 File System (The Memory)
- **Sandboxed CRUD:** Strict `WORKSPACE_ROOT` confinement.
- **Path Traversal Protection:** Prevents access to system files (e.g., `../../Windows/System32` is blocked).
- **Smart Writes:** Automatically creates directory structures on write.

---

## 🛠️ Architecture

We don't play around. This project is built with **FAANG-level standards**:

*   **Core:** Python 3.11+ & FastAPI (Async/Await).
*   **Server:** Uvicorn with `ProactorEventLoop` (Windows IOCP support).
*   **Validation:** Pydantic models for strict data typing.
*   **Documentation:** Auto-generated OpenAPI (Swagger) schema for LLM consumption.
*   **Audit:** Middleware logging system (`openclaw_audit.log`) tracks *every* AI action.

---

## 📦 Installation

### Prerequisites
- Python 3.10+
- Git

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/openclaw-api.git
cd openclaw-api
2. Set up Virtual Environment
code
Bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
3. Install Dependencies
code
Bash
pip install -r requirements.txt
playwright install chromium
4. Configure Environment
Create a .env file in the root directory:
code
Env
API_KEY=your_super_secret_key
HOST=127.0.0.1
PORT=8000
WORKSPACE_ROOT=C:/Path/To/Your/Projects
🎮 Usage
Start the Server:
code
Bash
python main.py
Open Swagger UI:
Go to http://127.0.0.1:8000/docs.
Authorize:
Click the "Authorize" button and enter your API_KEY.
Connect your AI Agent:
Feed the http://127.0.0.1:8000/openapi.json schema to your LLM (OpenAI/Anthropic) as a "Tool Definition".
🔒 Security Architecture
Network Isolation: Binds strictly to 127.0.0.1. No external access possible.
Auth: Bearer Token authentication required for ALL endpoints.
Sandboxing: File operations utilize a resolve_path algorithm that physically prevents escaping the WORKSPACE_ROOT.
Audit Trail: Every request is logged to openclaw_audit.log with timestamps and status codes.
🗺️ Roadmap

Core API (System, Web, Files)

Security Sandboxing

Playwright Integration

Docker Support

WebSocket Stream for Real-time Terminal Output

OCR Integration
<div align="center">
Built with ❤️ and ☕ by [Your Name]
</div>
```

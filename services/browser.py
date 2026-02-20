from playwright.async_api import async_playwright
import os
import base64
from core.config import settings

class BrowserManager:
    def __init__(self):
        self.playwright = None
        self.browser_context = None
        self.page = None
        self.user_data_dir = os.path.join(settings.WORKSPACE_ROOT, "browser_data")

    async def start(self):
        # Запускаем Playwright только если он еще не запущен
        if not self.playwright:
            self.playwright = await async_playwright().start()
        
        # Поднимаем браузер с сохранением сессии (куки, пароли)
        if not self.browser_context:
            self.browser_context = await self.playwright.chromium.launch_persistent_context(
                user_data_dir=self.user_data_dir,
                headless=False,  # Окно будет видимым для тебя
                args=list(("--start-maximized",)) # Используем list() вместо скобок
            )
            
            # Получаем первую открытую вкладку через итератор (без скобок)
            pages = self.browser_context.pages
            self.page = next(iter(pages), None)
            
            if not self.page:
                self.page = await self.browser_context.new_page()

    async def goto(self, url: str):
        await self.start()
        await self.page.goto(url)
        return dict(status="success", url=self.page.url)

    async def get_content(self):
        await self.start()
        content = await self.page.content()
        return dict(status="success", length=len(content))

    async def screenshot(self):
        await self.start()
        # Делаем скриншот и кодируем в Base64 для передачи ИИ
        buffer = await self.page.screenshot(type="jpeg", quality=70)
        b64_str = base64.b64encode(buffer).decode("utf-8")
        return dict(status="success", image_base64=b64_str)

# Экземпляр-одиночка
browser_manager = BrowserManager()
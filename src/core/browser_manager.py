from __future__ import annotations

from playwright.async_api import (
    Browser,
    BrowserContext,
    Playwright,
    async_playwright,
)

from config.settings import DEFAULT_TIMEOUT, HEADLESS


class BrowserManager:
    """
    Manages the Playwright browser lifecycle.
    """

    def __init__(self) -> None:
        self._playwright: Playwright | None = None
        self._browser: Browser | None = None

    async def start(self) -> None:
        """Start Playwright and launch Chromium."""

        self._playwright = await async_playwright().start()

        self._browser = await self._playwright.chromium.launch(
            headless=HEADLESS,
        )

    async def new_context(self, **kwargs) -> BrowserContext:
        """
        Create a new browser context.
        """

        if self._browser is None:
            raise RuntimeError("Browser has not been started.")

        context = await self._browser.new_context(**kwargs)

        context.set_default_timeout(DEFAULT_TIMEOUT)

        return context

    async def close(self) -> None:
        """Close browser and Playwright."""

        if self._browser:
            await self._browser.close()

        if self._playwright:
            await self._playwright.stop()
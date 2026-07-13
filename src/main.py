import asyncio

from core.browser_manager import BrowserManager


async def main() -> None:
    browser = BrowserManager()

    await browser.start()

    context = await browser.new_context()

    page = await context.new_page()

    await page.goto("https://www.amazon.in")

    print(await page.title())

    await context.close()

    await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
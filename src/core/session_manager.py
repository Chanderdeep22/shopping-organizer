session = SessionManager(browser)

context = await session.load_context(
    "amazon",
)
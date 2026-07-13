from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

STATE_DIR = PROJECT_ROOT / "state"
LOG_DIR = PROJECT_ROOT / "logs"
SCREENSHOT_DIR = PROJECT_ROOT / "screenshots"

STATE_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)
SCREENSHOT_DIR.mkdir(exist_ok=True)

HEADLESS = False

DEFAULT_TIMEOUT = 30_000

AMAZON_STATE = STATE_DIR / "amazon.json"
"""
Keep the Streamlit Community Cloud app awake.
Opens the site in headless Chromium (a real browser, so the WebSocket connects
and the app actually starts) and clicks the wake-up button if it's sleeping.

Usage:  python scripts/keepalive.py https://dynamicsolutionsplus.streamlit.app
Setup:  pip install playwright && playwright install --with-deps chromium
"""
import sys
from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

WAKE_BUTTON = "button:has-text('get this app back up')"


def wake(url: str) -> bool:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url, wait_until="domcontentloaded", timeout=60_000)
        try:
            page.locator(WAKE_BUTTON).click(timeout=15_000)
            print(f"WAKE  {url}  (was sleeping, clicked wake button)")
            page.wait_for_timeout(60_000)  # give it time to boot
        except PWTimeout:
            print(f"OK    {url}  (already awake)")
            page.wait_for_timeout(15_000)  # stay long enough to count as a visit
        browser.close()
    return True


if __name__ == "__main__":
    urls = sys.argv[1:]
    if not urls:
        sys.exit("Pass one or more app URLs.")
    failed = 0
    for u in urls:
        try:
            wake(u)
        except Exception as e:
            failed += 1
            print(f"FAIL  {u}  {e}")
    sys.exit(1 if failed else 0)

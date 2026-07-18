"""
One-time login helper.

Run this once (and again any time your session expires) to open
CanvasWorkspace in a real browser window, log in manually, and save
your session so watcher.py doesn't need you to log in every time.

Usage:
    python login_setup.py
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

STATE_FILE = Path(__file__).parent / "storage_state.json"
CANVAS_URL = "https://canvasworkspace.brother.com/"


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(CANVAS_URL)

        print("\nA browser window has opened.")
        print("1. Log in to your CanvasWorkspace account.")
        print("2. Make sure your account is linked to your ScanNCut DX.")
        print("3. Once you're fully logged in and see your dashboard,")
        print("   come back to this terminal.")
        input("Press ENTER once you're logged in... ")

        context.storage_state(path=str(STATE_FILE))
        print(f"Session saved to {STATE_FILE}")
        browser.close()


if __name__ == "__main__":
    main()

"""
Watches a folder for new cut files and sends each one to CanvasWorkspace,
which relays it wirelessly to your linked ScanNCut DX.

Run login_setup.py once before using this.

Usage:
    python watcher.py
"""
import json
import time
from pathlib import Path

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from playwright.sync_api import sync_playwright

BASE_DIR = Path(__file__).parent
CONFIG_FILE = BASE_DIR / "config.json"
STATE_FILE = BASE_DIR / "storage_state.json"
CANVAS_URL = "https://canvasworkspace.brother.com/"
VALID_EXTENSIONS = {".fcm", ".svg", ".dxf"}

if not CONFIG_FILE.exists():
    raise SystemExit(
        "config.json not found. Copy config.example.json to config.json "
        "and fill it in first."
    )

with open(CONFIG_FILE) as f:
    CONFIG = json.load(f)

WATCH_FOLDER = Path(CONFIG["watch_folder"])


def send_file_to_machine(filepath: Path):
    print(f"New file detected: {filepath.name}")

    if not STATE_FILE.exists():
        print("No saved session found. Run login_setup.py first.")
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state=str(STATE_FILE))
        page = context.new_page()
        page.goto(CANVAS_URL)

        try:
            selectors = CONFIG["selectors"]
            page.click(selectors["import_button"])
            page.set_input_files(selectors["file_input"], str(filepath))
            page.wait_for_timeout(3000)  # let the import finish rendering
            page.click(selectors["send_to_machine_button"])
            page.wait_for_timeout(2000)
            print(f"Sent {filepath.name} to the machine queue.")
        except Exception as e:
            print(f"Automation failed on {filepath.name}: {e}")
            print(
                "The site layout may not match the selectors in "
                "config.json — see README 'Finding selectors'."
            )
        finally:
            # Refresh the saved session so it stays valid longer.
            context.storage_state(path=str(STATE_FILE))
            browser.close()


class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        path = Path(event.src_path)
        if path.suffix.lower() in VALID_EXTENSIONS:
            time.sleep(2)  # let the file finish writing to disk
            send_file_to_machine(path)


def main():
    WATCH_FOLDER.mkdir(parents=True, exist_ok=True)
    print(f"Watching {WATCH_FOLDER} for new cut files (.fcm, .svg, .dxf)...")
    print("Leave this window open. Press Ctrl+C to stop.")

    handler = NewFileHandler()
    observer = Observer()
    observer.schedule(handler, str(WATCH_FOLDER), recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()

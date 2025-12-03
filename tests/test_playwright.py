from playwright.sync_api import sync_playwright
from pathlib import Path
import os
import datetime

root_dir = Path(__file__).parent.parent.absolute()

def test_google():

    with sync_playwright() as p:
        # Launch browser (headless like Selenium)
        browser = p.chromium.launch(headless=True)

        # Create context (equivalent to Chrome options)
        context = browser.new_context()

        # Open new page (equivalent to driver)
        page = context.new_page()

        # Go to Google
        page.goto("https://www.google.com")

        # Assert page title
        title = page.title()
        assert "Google" in title
        print(f"Page title is: {title}")

        # Take screenshot
        save_dir = f"{root_dir}/screenshots"
        take_screenshot(page, "google_homepage", save_dir)

        print(f"root_dir ----- {root_dir}")

        # Read file
        with open(f"{root_dir}/tests/screenshots/ss.txt", "r", encoding="utf-8") as f:
            data = f.read()
            print(f"fhjdfjhdfd --- {data}")

        # Close everything
        context.close()
        browser.close()


def take_screenshot(page, name_prefix, save_dir):
    # Create folder
    os.makedirs(save_dir, exist_ok=True)

    # Timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # File path
    file_path = os.path.join(save_dir, f"{name_prefix}_{timestamp}.png")

    # Screenshot
    page.screenshot(path=file_path)
    print(f"✅ Screenshot saved: {file_path}")
    print("newwwww")

    return file_path

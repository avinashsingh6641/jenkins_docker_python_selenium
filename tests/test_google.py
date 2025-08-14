# tests/test_google.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path
import os
import datetime
root_dir = Path(__file__).parent.parent.absolute()
def test_google():
    # Set up Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")  # Remove if you want visible browser

    # Create Chrome driver using locally installed Selenium + ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # Open Google
    driver.get("https://www.google.com")

    # Assert page title contains "Google"
    assert "Google" in driver.title
    print(f"Page title is: {driver.title}")
    take_screenshot(driver,"google_homepage",f"{root_dir}/screenshots")
    print(f"vroot_dir ----- {root_dir}")
    with open(f"{root_dir}/screenshots/ss.txt", "r", encoding="utf-8") as f:
        data = f.read()
        print(f"fhjdfjhdfd --- {data}")

    # Quit browser
    driver.quit()

def take_screenshot(driver,name_prefix, save_dir):
    # Create folder if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)

    # Timestamp for unique file names
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    # Full path for screenshot file
    file_path = os.path.join(save_dir, f"{name_prefix}_{timestamp}.png")

    # Take screenshot
    driver.save_screenshot(file_path)
    print(f"✅ Screenshot saved: {file_path}")

    return file_path

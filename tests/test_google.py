# tests/test_google.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_google():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options
    )

    # Open Google
    driver.get("https://www.google.com")

    # Assert page title contains "Google"
    assert "Google" in driver.title
    print(f"hjhjdfhjdf {driver.title}")

    # Quit browser
    driver.quit()

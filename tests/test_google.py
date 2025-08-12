# tests/test_google.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_google():
    # Setup Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Open Google
    driver.get("https://www.google.com")

    # Assert page title contains "Google"
    assert "Google" in driver.title
    print(f"hjhjdfhjdf {driver.title}")

    # Quit browser
    driver.quit()

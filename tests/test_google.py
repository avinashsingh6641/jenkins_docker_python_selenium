# tests/test_google.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


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

    # Quit browser
    driver.quit()

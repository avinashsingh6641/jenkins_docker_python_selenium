from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Chrome options
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless=new")  # Remove this if you want to see browser

# Start Chrome directly
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.google.com")
    print("Page title:", driver.title)

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Hello from Selenium!")
    search_box.send_keys(Keys.RETURN)

    time.sleep(2)  # Let the results load
    print("New page title:", driver.title)

finally:
    driver.quit()

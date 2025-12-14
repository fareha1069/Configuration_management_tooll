from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

APP_URL = os.getenv("APP_URL", "http://localhost:3000")
WAIT_TIME = 40  

options = Options()
options.add_argument("--headless=new")           # REQUIRED for Jenkins
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-gpu")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    print(" Opening app:", APP_URL)
    driver.get(APP_URL)

    wait = WebDriverWait(driver, WAIT_TIME)

    print(" Waiting for 'Get Started' button...")

    get_started_btn = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[.//span[normalize-space()='Get Started']]")
        )
    )

    # Scroll + click safely
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", get_started_btn)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", get_started_btn)

    print(" 'Get Started' button clicked")

    time.sleep(2)
    print(" Current URL:", driver.current_url)

except Exception as e:
    print(" Test failed:", str(e))
    driver.save_screenshot("ui_test_failure.png")
    raise

finally:
    driver.quit()
    print(" Browser closed")

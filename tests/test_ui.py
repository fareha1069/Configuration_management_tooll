from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("http://localhost:3000/")  # React frontend URL
driver.maximize_window()

wait = WebDriverWait(driver, 20)

# Locate button
get_started_btn = wait.until(
    EC.presence_of_element_located((By.XPATH, "//button[.//span[text()='Get Started']]"))
)

# Scroll into view and click using JS
driver.execute_script("arguments[0].scrollIntoView(true);", get_started_btn)
time.sleep(0.5)
driver.execute_script("arguments[0].click();", get_started_btn)

print("✅ 'Get Started' button clicked!")

# Wait to see navigation
time.sleep(2)
print("Current URL after click:", driver.current_url)

driver.quit()
print("hello")

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Create a WebDriverWait instance
wait = WebDriverWait(driver, 30)  # Increase wait time

# Wait for the element to be clickable
try:
    get_started_btn = wait.until(
        EC.element_to_be_clickable((By.ID, "get-started-button"))
    )
    get_started_btn.click()  # If clickable, click the button
except TimeoutException:
    print("Element not found within the timeout period")
    driver.save_screenshot('error_screenshot.png')  # Capture a screenshot on error

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def login_to_site(driver, username, password):
    driver.get("https://the-internet.herokuapp.com/login")
    
    # Locate elements
    user_input = driver.find_element(By.ID, "username")
    pass_input = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    
    # Send login credentials
    user_input.send_keys(username)
    pass_input.send_keys(password)
    login_btn.click()

    time.sleep(1)  # Let page load

    # Check success message
    try:
        success_msg = driver.find_element(By.CSS_SELECTOR, ".flash.success")
        return True
    except:
        return False

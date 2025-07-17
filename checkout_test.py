import os
import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

# --- Configuration for SauceDemo ---
BASE_URL = "https://www.saucedemo.com/"
LOGIN_URL = f"{BASE_URL}" # Login page is the base URL
PRODUCTS_URL = f"{BASE_URL}inventory.html"
CART_URL = f"{BASE_URL}cart.html"
CHECKOUT_STEP_ONE_URL = f"{BASE_URL}checkout-step-one.html"
CHECKOUT_STEP_TWO_URL = f"{BASE_URL}checkout-step-two.html"
CHECKOUT_COMPLETE_URL = f"{BASE_URL}checkout-complete.html"

GLOBAL_WAIT_TIMEOUT = 20
SHORT_WAIT_TIMEOUT = 5

# Test Credentials and Data for SauceDemo
SAUCEDEMO_USERNAME = "standard_user"
SAUCEDEMO_PASSWORD = "secret_sauce"

CHECKOUT_INFO = {
    "first_name": "Amrit",
    "last_name": "Singh",
    "zip_code": "12345"
}

# --- Utility Functions (Generally reusable) ---
def setup_driver():
    """Initializes and returns a Chrome WebDriver instance."""
    print("Setting up Chrome WebDriver...")
    try:
        # service = Service(executable_path='/path/to/your/chromedriver') # Uncomment if chromedriver not in PATH
        driver = webdriver.Chrome()
        driver.maximize_window()
        return driver
    except WebDriverException as e:
        print(f"ERROR: Could not set up WebDriver. Ensure Chrome and Chromedriver are correctly installed and compatible: {e}")
        return None

def take_screenshot(driver, filename="error_screenshot.png"):
    """Takes a screenshot and saves it to the current directory."""
    if driver:
        try:
            screenshot_path = os.path.join(os.getcwd(), filename)
            driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved: {screenshot_path}")
        except Exception as e:
            print(f"WARNING: Could not save screenshot: {e}")

def initialize_excel_report():
    """Initializes a new Excel workbook for the test report."""
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "SauceDemo Checkout Report"
    sheet['A1'] = "Test Case"
    sheet['B1'] = "Status"
    sheet['C1'] = "Details"
    return wb, sheet

def save_excel_report(wb, filename="saucedemo_checkout_report.xlsx"):
    """Saves the Excel workbook."""
    try:
        report_path = os.path.join(os.getcwd(), filename)
        wb.save(report_path)
        print(f"📄 Excel report saved: {report_path}")
    except Exception as e:
        print(f"ERROR: Could not save Excel report: {e}")

# --- Main Test Script ---
def run_saucedemo_checkout_test():
    driver = None
    wb, sheet = initialize_excel_report()
    test_status = "Fail"
    test_details = ""

    try:
        driver = setup_driver()
        if not driver:
            raise Exception("WebDriver setup failed.")

        wait = WebDriverWait(driver, GLOBAL_WAIT_TIMEOUT)

        print("\n--- Starting SauceDemo Checkout Test ---")
        driver.get(LOGIN_URL)
        print(f"Navigated to login page: {LOGIN_URL}")

        # 🔑 Login
        print("Attempting to log in...")
        wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(SAUCEDEMO_USERNAME)
        driver.find_element(By.ID, "password").send_keys(SAUCEDEMO_PASSWORD)
        driver.find_element(By.ID, "login-button").click()
        print("Login credentials entered.")

        # Verify successful login by checking for products page URL
        wait.until(EC.url_to_be(PRODUCTS_URL))
        print("Successfully logged in and landed on products page.")

        # 🛍️ Add a product to cart (Sauce Labs Backpack)
        print("Adding 'Sauce Labs Backpack' to cart...")
        add_to_cart_backpack_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        add_to_cart_backpack_btn.click()
        print("Sauce Labs Backpack added to cart.")

        # 🛒 Go to cart
        print("Navigating to shopping cart...")
        shopping_cart_link = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        shopping_cart_link.click()
        wait.until(EC.url_to_be(CART_URL))
        print("Landed on shopping cart page.")

        # 👉 Proceed to checkout (from cart page)
        print("Proceeding to checkout from cart...")
        # --- DIAGNOSTIC PAUSE HERE ---
        print("DIAGNOSTIC PAUSE: Waiting for 5 seconds. Observe the 'Checkout' button on the cart page.")
        time.sleep(5) # Observe the button state

        # Let's try a more specific CSS selector if the ID is problematic, or ensure it's a button
        # Based on SauceDemo, it's typically <button id="checkout" ...>
        checkout_btn_locator = (By.ID, "checkout") # This should be correct
        # Alternatively, if 'checkout' ID is shared or problematic, try:
        # checkout_btn_locator = (By.CSS_SELECTOR, "button#checkout") # Specific for button with ID 'checkout'
        # checkout_btn_locator = (By.XPATH, "//button[@id='checkout']") # XPath alternative

        checkout_btn = wait.until(
            EC.element_to_be_clickable(checkout_btn_locator)
        )
        checkout_btn.click()
        wait.until(EC.url_to_be(CHECKOUT_STEP_ONE_URL))
        print("Landed on Checkout: Your Information page.")

        # 📝 Fill Your Information (Checkout Step One)
        print("Filling checkout information (Step 1)...")
        wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys(CHECKOUT_INFO["first_name"])
        driver.find_element(By.ID, "last-name").send_keys(CHECKOUT_INFO["last_name"])
        driver.find_element(By.ID, "postal-code").send_keys(CHECKOUT_INFO["zip_code"])
        print("Checkout information filled.")

        # Continue to Checkout Overview
        print("Continuing to Checkout Overview (Step 2)...")
        continue_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "continue"))
        )
        continue_btn.click()
        wait.until(EC.url_to_be(CHECKOUT_STEP_TWO_URL))
        print("Landed on Checkout: Overview page.")

        # 🧾 Confirm Order (Checkout Step Two - Overview)
        print("Confirming order on Overview page...")
        finish_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "finish"))
        )
        finish_btn.click()
        wait.until(EC.url_to_be(CHECKOUT_COMPLETE_URL))
        print("Order finished. Landed on Checkout: Complete! page.")

        # 🎉 Verify Order Confirmation
        print("Verifying order confirmation message...")
        confirmation_header = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
        )
        actual_message = confirmation_header.text.strip()

        expected_message = "Thank you for your order!"

        if expected_message in actual_message:
            test_status = "Pass"
            test_details = f"Order confirmed: '{actual_message}'"
            print(f"✅ SauceDemo Checkout Test Passed – {test_details}")
        else:
            test_status = "Fail"
            test_details = f"Unexpected confirmation message: '{actual_message}'. Expected: '{expected_message}'"
            print(f"❌ SauceDemo Checkout Test Failed – {test_details}")

    except TimeoutException as e:
        test_status = "Fail (Timeout)"
        test_details = f"Element not found within {GLOBAL_WAIT_TIMEOUT} seconds. Error: {e.msg}"
        print(f"❌ Test Failed: {test_details}")
        take_screenshot(driver, "timeout_error_screenshot.png")
    except NoSuchElementException as e:
        test_status = "Fail (Element Not Found)"
        test_details = f"An expected element was not found. Error: {e.msg}"
        print(f"❌ Test Failed: {test_details}")
        take_screenshot(driver, "element_not_found_screenshot.png")
    except WebDriverException as e:
        test_status = "Fail (WebDriver Error)"
        test_details = f"A WebDriver-related error occurred. Error: {e}"
        print(f"❌ Test Failed: {test_details}")
        take_screenshot(driver, "webdriver_error_screenshot.png")
    except Exception as e:
        test_status = "Fail (Unexpected Error)"
        test_details = f"An unexpected error occurred: {type(e).__name__} - {e}"
        print(f"❌ Test Failed: {test_details}")
        take_screenshot(driver, "unexpected_error_screenshot.png")
    finally:
        sheet.append(["SauceDemo Checkout Test", test_status, test_details])
        save_excel_report(wb)
        if driver:
            driver.quit()
            print("Browser closed.")
        print("\n--- SauceDemo Checkout Test Finished ---")

# --- Run the test ---
if __name__ == "__main__":
    run_saucedemo_checkout_test()
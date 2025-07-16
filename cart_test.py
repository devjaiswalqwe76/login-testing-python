from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl

# 🚀 Launch browser
driver = webdriver.Chrome()
driver.get("https://demowebshop.tricentis.com/141-inch-laptop")

# 🕒 Smart wait for page to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "add-to-cart-button-31"))  # Specific product ID
)

# 🛍️ Click 'Add to Cart'
add_to_cart_button = driver.find_element(By.ID, "add-to-cart-button-31")
add_to_cart_button.click()

# ⏳ Wait for success notification
try:
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".bar-notification.success"))
    )
    
    print("🧾 Message Text:", success_message.text.strip())  # Debug message

    assert "added to your shopping cart" in success_message.text.lower()
    print("✅ Cart Test Passed – Item added successfully")
    test_status = "Pass"

except Exception as e:
    print("❌ Cart Test Failed – No confirmation or unexpected message")
    test_status = "Fail"

# 📊 Create Excel report
wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = 'Test Case'
sheet['B1'] = 'Status'
sheet.append(['Cart Test', test_status])
wb.save("cart_test_report.xlsx")
print("📄 Excel report saved: cart_test_report.xlsx")

# 🚪 Close browser
driver.quit()

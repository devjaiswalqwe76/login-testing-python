from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
import time

# 🚀 Launch browser
driver = webdriver.Chrome()
driver.get("https://demowebshop.tricentis.com/")

# 🔍 Wait for search bar to appear
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "small-searchterms"))
)

# 🧪 Enter search keyword
search_box.send_keys("laptop")

# 🖱️ Click search button
driver.find_element(By.CSS_SELECTOR, "input[value='Search']").click()

# ⏱️ Wait for products to load
time.sleep(2)

# 📦 Get product results
results = driver.find_elements(By.CLASS_NAME, "product-item")

# 📊 Excel setup
wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = 'Test Case'
sheet['B1'] = 'Status'

# ✅ Test assertion
try:
    assert len(results) > 0
    print("✅ Search Test Passed – Products Found")
    sheet.append(['Search Test', 'Pass'])
except AssertionError:
    print("❌ Search Test Failed – No Products Found")
    sheet.append(['Search Test', 'Fail'])

# 💾 Save Excel file
wb.save("search_test_report.xlsx")
print("📄 Excel report saved: search_test_report.xlsx")

# 🚪 Close browser
driver.quit()

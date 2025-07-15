from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl  # ✅ Import openpyxl

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

# 🔐 Login Details
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()

# ✅ Assertion Block with Feedback
try:
    assert "Logged In Successfully" in driver.page_source
    print("✅ Login Test Passed")

    # 📊 Excel Logging Block - paste yahan (inside try block)
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet['A1'] = 'Test Case'
    sheet['B1'] = 'Status'
    sheet.append(['Login Test', 'Pass'])
    wb.save('login_test_report.xlsx')
    print("📄 Excel report saved: login_test_report.xlsx")

except AssertionError:
    print("❌ Login Test Failed")

    # 📊 Logging 'Fail' result as well (inside except block)
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet['A1'] = 'Test Case'
    sheet['B1'] = 'Status'
    sheet.append(['Login Test', 'Fail'])
    wb.save('login_test_report.xlsx')
    print("📄 Excel report saved: login_test_report.xlsx")

finally:
    driver.quit()

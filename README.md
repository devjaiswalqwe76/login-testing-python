🧪 Login Functionality Testing with Python + Selenium

A beginner-friendly project that simulates **manual login test cases** using `Python`, `Selenium`, and `Excel reporting`. This repo helps learners practice real-world QA workflows including input validation, test result logging, and browser automation.

📦 Technologies & Libraries Used

Python 3.11+
Selenium WebDriver – browser automation
OpenPyXL – Excel reporting
ChromeDriver – to launch Chrome for testing
Git & GitHub – version control and portfolio sharing

 ✅ Features

- Valid and invalid login test case coverage
- Real-time assertion using Python `try-except`
- Automatic Excel report generation
- No external frameworks—just clean Python logic
- Step-by-step execution for manual-style testing

 🔧 Setup Instructions

 1. Clone the repository

```bash
git clone https://github.com/devjaiswalqwe76/login-testing-python.git
cd login-testing-python


2. Search Functionality Testing with Python + Selenium

This module tests the product search feature on a demo e-commerce site using `Selenium` and logs results using `OpenPyXL`. It simulates how users search for items and helps validate that results appear based on keyword input.

Technologies Used

Python 3.11+
Selenium WebDriver – browser automation
WebDriverWait – reliable element detection
OpenPyXL– Excel report generation
ChromeDriver – to launch Chrome browser
Git & GitHub – for version control and portfolio sharing

✅ Test Features

- Search for product using dynamic keywords like `"laptop"` or `"camera"`
- Assert visibility of product listing
- Log Pass/Fail status in Excel file (`search_test_report.xlsx`)
- Uses wait logic for better page reliability

Setup Instructions

1. Clone the repository

bash
git clone https://github.com/devjaiswalqwe76/login-testing-python.git
cd login-testing-python


## 🛒 Cart Functionality Testing with Python + Selenium

This module tests the "Add to Cart" feature on a demo e-commerce site, ensuring that products can be added successfully. The script uses Selenium for browser automation and OpenPyXL for Excel-based result tracking, mimicking real-world QA workflows.

---

### ✅ Features

- Adds product to cart using precise element locators
- Smart waiting with `WebDriverWait` for stable test execution
- Asserts presence of confirmation message
- Logs Pass/Fail result in `cart_test_report.xlsx`
- Screenshot optional for cart popup or browser state

---

### 🧪 Technologies Used

- `Python 3.11+`
- `Selenium WebDriver` – browser control
- `OpenPyXL` – Excel report logging
- `WebDriverWait` – reliable element detection
- `ChromeDriver` – launching Chrome browser


#How to Run

```bash
python cart_test.py


## 🧾 SauceDemo Checkout Functionality Test with Python + Selenium

This module performs an end-to-end checkout test on [SauceDemo](https://www.saucedemo.com/), simulating a user flow from login to purchase confirmation. It includes structured step logging, screenshot pauses, and Excel-based result tracking—ideal for showcasing real-world QA workflows.

---

### ✅ Features

- Automates full checkout flow:
  - Login
  - Add product to cart
  - Checkout (User Info, Overview, Confirmation)
- Logs each step in terminal for visibility
- Asserts final confirmation message: `"Thank you for your order!"`
- Records Pass/Fail status in Excel
- Saves report as `saucedemo_checkout_report.xlsx` for manual-style tracking

---

### 🛠️ Tools Used

| Tool             | Purpose                         |
|------------------|----------------------------------|
| Python (3.11+)   | Core scripting language          |
| Selenium         | Browser automation               |
| `WebDriverWait`  | Stable interaction handling      |
| OpenPyXL         | Excel report generation          |
| ChromeDriver     | Launch Chrome for tests          |

---

### ▶️ How to Run

```bash
python checkout_test.py


# 🧪 Login Testing with Selenium + PyTest

Automated testing project built with **Python**, **Selenium WebDriver**, and **PyTest** — demonstrating login validation across multiple input scenarios using `@pytest.mark.parametrize`. Designed for clean execution, modular structure, and scalable reporting.

---

## 📍 Demo Site

Testing is performed on [The Internet HerokuApp – Login Page](https://the-internet.herokuapp.com/login), a reliable public demo for automation workflows.

---

## ✅ Features

- 🔐 **Login flow validation** using Selenium
- 🧬 **Parametrize-based test cases** for multiple input combinations
- 🛠️ Modular helpers in `utils/`
- 🌐 Browser automation via `ChromeDriver`
- 📦 Managed using `PyTest` fixtures from `conftest.py`
- 🖼️ Error screenshots (optional) and HTML reporting support

---

## 🗂️ Project Structure


---

## 🔍 Parametrize Logic

```python
@pytest.mark.parametrize("username,password,expected", [
    ("tomsmith", "SuperSecretPassword!", True),
    ("wronguser", "SuperSecretPassword!", False),
    ("tomsmith", "wrongpass", False),
    ("", "", False),
    ("admin", "admin123", False)
])
def test_login_parametrize(driver, username, password, expected):
    result = login_to_site(driver, username, password)
    assert result == expected


# Task link: https://www.saucedemo.com/

## Task 1 (**Web Automation with Selenium**)

# You are tasked with automating the following actions on a demo e-commerce website:
# URL: https://www.saucedemo.com/
# 1. **Login Automation**
#     Automate the login process for the website using provided test credentials.

# 2. **Product Search Verification**
#     Navigate to the products page after login, and verify the presence of specific product names.
# ---
# 1. **Login to the Website**
#     - Navigate to https://www.saucedemo.com/.
#     - Locate and interact with the login form:
#         - Enter the username: `standard_user`.
#         - Enter the password: `secret_sauce`.
#         - Click the "Login" button.
#     - Verify that you have successfully logged in by checking the presence of the products page title or elements.
# 2. **Verify Specific Product**
#     - After logging in, locate and verify the presence of the following product:
#         - Product Name: **"Sauce Labs Backpack"**.
#     - Assert that the product name is displayed on the page.

## ============== Task 2 (Parameterization and Fixtures) ===========================

# Now, enhance your login script to include parameterization and create a driver fixture.
# Make sure to test all the usernames available on https://www.saucedemo.com

#======================== TASK-2 ==========================
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com/"


# =========================================================
# Test Data (All Available Users)
# =========================================================

test_users = [
    ("standard_user", "secret_sauce"),
    ("locked_out_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
    ("visual_user", "secret_sauce"),
]


# =========================================================
# Driver Fixture
# =========================================================

@pytest.fixture
def driver():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)

    yield driver

    print("Closing browser...")
    driver.quit()


# =========================================================
# Verify Login Page
# =========================================================

def test_login_page(driver):

    wait = WebDriverWait(driver, 10)

    logo: WebElement = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "login_logo"))
    )

    assert logo.text == "Swag Labs"

    print("Login page verified")


# =========================================================
# Parameterized Login Test
# =========================================================

@pytest.mark.parametrize("username,password", test_users)
def test_login(driver, username, password):

    wait = WebDriverWait(driver, 10)

    # =====================================================
    # Enter Username
    # =====================================================

    username_input: WebElement = wait.until(
        EC.element_to_be_clickable((By.ID, "user-name"))
    )
    username_input.clear()
    username_input.send_keys(username)

    # =====================================================
    # Enter Password
    # =====================================================

    password_input: WebElement = wait.until(
        EC.element_to_be_clickable((By.ID, "password"))
    )
    password_input.clear()
    password_input.send_keys(password)

    # =====================================================
    # Click Login
    # =====================================================

    login_button: WebElement = wait.until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )
    login_button.click()

    # =====================================================
    # Validation
    # =====================================================

    if username == "locked_out_user":

        error_message: WebElement = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "h3[data-test='error']")
            )
        )

        assert "locked out" in error_message.text.lower()

        print(f"Correctly blocked login for: {username}")

    else:

        title: WebElement = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "title"))
        )

        assert title.text == "Products"

        print(f"Login successful for: {username}")


# =========================================================
# Verify Specific Product
# =========================================================

def test_verify_product(driver):

    wait = WebDriverWait(driver, 10)

    # =====================================================
    # Login with standard_user
    # =====================================================

    driver.find_element(By.ID, "user-name").send_keys("standard_user")

    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    driver.find_element(By.ID, "login-button").click()

    # =====================================================
    # Wait for Products
    # =====================================================

    products = wait.until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "inventory_item_name")
        )
    )

    product_names = [product.text for product in products]

    print("Available Products:")
    for item in product_names:
        print(item)

    # =====================================================
    # Verify Backpack Product
    # =====================================================

    assert "Sauce Labs Backpack" in product_names

    print("Sauce Labs Backpack found")
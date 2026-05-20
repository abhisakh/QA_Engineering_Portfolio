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

#======================== TASK-1 ==========================
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com/"


def get_driver() -> webdriver.Chrome:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)
    return driver


def test_login_and_verify_product():

    driver = get_driver()
    wait = WebDriverWait(driver, 10)

    try:
        # =====================================================
        # Verify Landing Page
        # =====================================================

        logo: WebElement = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "login_logo"))
        )

        assert logo.text == "Swag Labs"
        print("Login page loaded successfully")

        # =====================================================
        # Login
        # =====================================================

        username: WebElement = wait.until(
            EC.element_to_be_clickable((By.ID, "user-name"))
        )
        username.send_keys("standard_user")

        password: WebElement = wait.until(
            EC.element_to_be_clickable((By.ID, "password"))
        )
        password.send_keys("secret_sauce")

        login_button: WebElement = wait.until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        login_button.click()

        # =====================================================
        # Verify Successful Login
        # =====================================================

        title: WebElement = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "title"))
        )

        assert title.text == "Products"
        print("Login successful")

        # =====================================================
        # Verify Product Presence
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

        assert "Sauce Labs Backpack" in product_names
        print("Sauce Labs Backpack found")

    finally:
        print("Closing browser...")
        driver.quit()


if __name__ == "__main__":
    test_login_and_verify_product()
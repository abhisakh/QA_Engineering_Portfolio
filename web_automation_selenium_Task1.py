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
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

URL = "https://www.saucedemo.com/"

def get_driver(url=URL) -> webdriver.Chrome:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    return driver

driver = get_driver()

wait = WebDriverWait(driver, 10)

def test_login_page() -> bool:
    """Verifies that the landing page logo is rendered correctly."""
    logo: WebElement = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".login_logo"))
    )
    print(f"Landing Page Logo: {logo.text}")
    return logo.text == "Swag Labs"

def test_login() -> bool:
    """Automates user login credentials and verifies redirection."""
    username: WebElement = wait.until(EC.element_to_be_clickable((By.ID, "user-name")))
    username.send_keys("standard_user")

    password: WebElement = wait.until(EC.element_to_be_clickable((By.ID, "password")))
    password.send_keys("secret_sauce")

    button: WebElement = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    button.click()

    # Verification
    page_title: WebElement = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".title")))
    print(f"Dashboard Title: {page_title.text}")
    return page_title.text == "Products"

def test_present_specific_product() -> bool:
    """Finds and verifies the explicit presence of the required backpack item."""
    try:
        if test_login_page() and test_login():
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item_name")))
            products: list[WebElement] = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
            time.sleep(2)

            product_names = [item.text for item in products]
            print(f"Discovered items on page: {product_names}")
            time.sleep(2)

            is_backpack_present = "Sauce Labs Backpack" in product_names
            print(f"Is 'Sauce Labs Backpack' visible? -> {is_backpack_present}")
            time.sleep(2)

            assert is_backpack_present, "Target product 'Sauce Labs Backpack' was missing from the UI."
            return is_backpack_present

        return False

    finally:
        print("Terminating automation browser thread session...")
        driver.quit()

if __name__ == "__main__":
    test_present_specific_product()

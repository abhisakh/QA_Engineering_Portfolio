# Task link: https://www.saucedemo.com/

## ## ============== Task 1 ===========================(**Web Automation with Selenium**)

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

## ============== Task 3 (Register User)  ===========================

# Write a Selenium script that does the following:

# 1. Launch browser

# 2. Navigate to url ['http://automationexercise.com'](https://automationexercise.com/)

# 3. Verify that home page is visible successfully

# 4. Click on 'Signup / Login' button

# 5. Verify 'New User Signup!' is visible

# 6. Enter name and email address

# 7. Click 'Signup' button

# 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible

# 9. Fill details: Title, Name, Email, Password, Date of birth

# 10. Select checkbox 'Sign up for our newsletter!'

# 11. Select checkbox 'Receive special offers from our partners!'

# 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number

# 13. Click 'Create Account button'

# 14. Verify that 'ACCOUNT CREATED!' is visible

# 15. Click 'Continue' button

# 16. Verify that 'Logged in as username' is visible

# 17. Click 'Delete Account' button

# 18. Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button

#======================== TASK-3 ==========================
import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://automationexercise.com/"


def generate_email():
    return f"testuser{random.randint(1000,9999)}@gmail.com"


def get_driver():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)

    return driver


def handle_consent_popup(driver, wait):

    try:
        consent_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(., 'Consent')]"
                )
            )
        )

        consent_button.click()

        print("Consent popup handled")

    except:
        print("No consent popup appeared")


def test_register_user():

    driver = get_driver()

    wait = WebDriverWait(driver, 10)

    handle_consent_popup(driver, wait)

    try:

        # =====================================================
        # Verify Home Page
        # =====================================================

        home_page = wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, "body"))
        )

        assert home_page.is_displayed()

        print(" Home page visible")


        # =====================================================
        # Click Signup/Login
        # =====================================================

        signup_login = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(text(),'Signup / Login')]")
            )
        )

        signup_login.click()

        # =====================================================
        # Verify New User Signup
        # =====================================================

        signup_text = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h2[contains(text(),'New User Signup!')]")
            )
        )

        assert signup_text.is_displayed()

        print(" New User Signup visible")

        # =====================================================
        # Enter Name and Email
        # =====================================================

        name = "John Doe"
        email = generate_email()

        driver.find_element(By.NAME, "name").send_keys(name)

        driver.find_element(
            By.XPATH,
            "//input[@data-qa='signup-email']"
        ).send_keys(email)

        # =====================================================
        # Click Signup Button
        # =====================================================

        driver.find_element(
            By.XPATH,
            "//button[@data-qa='signup-button']"
        ).click()

        # =====================================================
        # Verify ENTER ACCOUNT INFORMATION
        # =====================================================

        account_info = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//b[contains(text(),'Enter Account Information')]")
            )
        )

        assert account_info.is_displayed()

        print(" Enter Account Information visible")

        # =====================================================
        # Fill Account Information
        # =====================================================

        driver.find_element(By.ID, "id_gender1").click()
        time.sleep(1) #--------<---------------------
        driver.find_element(By.ID, "password").send_keys("Test@123")
        time.sleep(1) #--------<---------------------
        # Date of Birth
        Select(driver.find_element(By.ID, "days")).select_by_visible_text("10")
        time.sleep(1) #--------<---------------------
        Select(driver.find_element(By.ID, "months")).select_by_visible_text("May")
        time.sleep(1) #--------<---------------------
        Select(driver.find_element(By.ID, "years")).select_by_visible_text("1998")

        # =====================================================
        # Checkboxes
        # =====================================================

        driver.find_element(By.ID, "newsletter").click()
        time.sleep(1) #--------<---------------------
        driver.find_element(By.ID, "optin").click()
        time.sleep(1) #--------<---------------------
        # =====================================================
        # Address Information
        # =====================================================

        driver.find_element(By.ID, "first_name").send_keys("John")
        time.sleep(1) #--------<---------------------
        driver.find_element(By.ID, "last_name").send_keys("Doe")
        time.sleep(1) #--------<---------------------
        driver.find_element(By.ID, "company").send_keys("OpenAI")
        time.sleep(1) #--------<---------------------
        driver.find_element(By.ID, "address1").send_keys("Berlin Street 101")
        time.sleep(1) #--------<---------------------
        driver.find_element(By.ID, "address2").send_keys("Apartment 12")
        time.sleep(1) #--------<---------------------
        Select(driver.find_element(By.ID, "country")).select_by_visible_text(
            "India"
        )

        driver.find_element(By.ID, "state").send_keys("Delhi")
        time.sleep(1) #--------<---------------------
        driver.find_element(By.ID, "city").send_keys("New Delhi")
        time.sleep(1) #--------<---------------------
        driver.find_element(By.ID, "zipcode").send_keys("110001")
        time.sleep(1) #--------<---------------------
        driver.find_element(By.ID, "mobile_number").send_keys("9876543210")

        # =====================================================
        # Create Account
        # =====================================================

        driver.find_element(
            By.XPATH,
            "//button[@data-qa='create-account']"
        ).click()

        # =====================================================
        # Verify ACCOUNT CREATED
        # =====================================================

        account_created = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//b[contains(text(),'Account Created!')]")
            )
        )

        assert account_created.is_displayed()

        print(" ACCOUNT CREATED!")

        # =====================================================
        # Continue Button
        # =====================================================

        driver.find_element(
            By.XPATH,
            "//a[@data-qa='continue-button']"
        ).click()

        # =====================================================
        # Verify Logged in as Username
        # =====================================================

        logged_in = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, f"//a[contains(text(),'Logged in as')]")
            )
        )

        assert logged_in.is_displayed()

        print(" Logged in successfully")

        # =====================================================
        # Delete Account
        # =====================================================

        delete_btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(text(),'Delete Account')]")
            )
        )

        driver.execute_script("arguments[0].click();", delete_btn)

        # =====================================================
        # Verify ACCOUNT DELETED
        # =====================================================

        account_deleted = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//*[contains(text(),'Account Deleted!')]"
                )
            )
        )

        assert account_deleted.is_displayed()

        print(" ACCOUNT DELETED!")

        # =====================================================
        # Continue After Delete
        # =====================================================

        driver.find_element(
            By.XPATH,
            "//a[@data-qa='continue-button']"
        ).click()

    finally:

        print("Closing browser...")
        time.sleep(2)

        driver.quit()


if __name__ == "__main__":
    test_register_user()

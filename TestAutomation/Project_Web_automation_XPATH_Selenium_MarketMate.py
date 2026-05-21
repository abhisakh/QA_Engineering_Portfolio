import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://grocerymate.masterschool.com/"

def get_driver():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(URL)

    return driver


def buy_item():
    driver = get_driver()
    wait = WebDriverWait(driver, 10)

    #================== LOAD HOME PAGE and ICON ==============
    home_page = wait.until(
        EC.visibility_of_element_located((By.TAG_NAME, "body"))
    )
    print(" Home page visible")
    #----------------- CLICK THE ICON ----------------------------
    human_icon = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='social-icon-cont']/div[1]")
        )
    )
    human_icon.click()
    time.sleep(1)
    #----------------- TYPE EMAIL --------------------------------
    email = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//input[@type='email']")
        )
    )
    email.send_keys("abhisakh_3@gmail.com")
    print("Email provided....")
    time.sleep(1)
    #----------------- TYPE PASSWORD --------------------------------
    password = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//input[@type='password']")
        )
    )
    password.send_keys("Falguni1982")
    print("Password provided....")
    time.sleep(1)
    #----------------- CLICK TO SIGN IN -----------------------------
    sign_in = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit']")
        )
    )
    sign_in.click()
    print("Sign in button clicked....")
    time.sleep(1)
    #----------------- CLICK TO SHOP  -----------------------------
    shop_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//ul[@class='anim-nav']//a[contains(@href, '/store')]"))
    )
    shop_button.click()
    print("Shop button clicked....")
    time.sleep(1)
    #----------------- CLICK TO CONFIRM MODAL BUTTON  -----------------------------
    confirm_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='modal-content']//button[text()='Confirm']"))
    )
    confirm_button.click()
    print("Confirm button clicked....")
    time.sleep(1)
    #----------------- TYPE ORAANGE QUANTITY INPUT--------------------------------
    quantity_input = wait.until(
    EC.presence_of_element_located((By.XPATH, "//p[text()='Oranges']/ancestor::div[@class='card']//input[@class='quantity']"))
    )
    quantity_input.clear()
    quantity_input.send_keys("3")
    print("Quantity field is filled...")
    time.sleep(1)
    #-----------------  Click "Add to Cart" for Oranges --------------------------------
    add_to_cart = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='Oranges']/ancestor::div[@class='card']//button[text()='Add to Cart']"))
    )
    add_to_cart.click()
    print("Product added to the cart..")
    time.sleep(1)

    #-----------------  "Add to Wish List"  --------------------------------
    wishlist_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='Oranges']/ancestor::div[@class='card']//button[contains(., '❤')]"))
    )
    wishlist_button.click()
    print("Product added to the wishlist..")
    time.sleep(5)

    #-----------------  QUIT  --------------------------------
    driver.quit()

def new_account():
    driver = get_driver()
    wait = WebDriverWait(driver, 10)
    #================== LOAD HOME PAGE and ICON ==============
    home_page = wait.until(
        EC.visibility_of_element_located((By.TAG_NAME, "body"))
    )
    print(" Home page visible")
    #----------------- CLICK THE ICON ----------------------------
    human_icon = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='social-icon-cont']/div[1]")
        )
    )
    human_icon.click()
    time.sleep(1)
    #----------------- CLICK TO CREATE A NEW ACCOUNT -----------------------------
    new_account = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='switch-link']")
        )
    )
    new_account.click()
    print("Create new account button clicked....")
    time.sleep(1)
    #----------------- TYPE FULL NAME --------------------------------
    name = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//input[@placeholder='Full Name']")
        )
    )
    name.send_keys("kbhi")
    print("Full name provided....")
    time.sleep(1)
    #----------------- NEW EMAIL ADDRESS --------------------------------
    new_email = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//input[@type='email']")
        )
    )
    new_email.send_keys("abhi@redit.com")
    print("New email provided....")
    time.sleep(1)
    #----------------- TYPE PASSWORD --------------------------------
    new_password = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//input[@type='password']")
        )
    )
    new_password.send_keys("Abhisakh123")
    print("New password provided....")
    time.sleep(1)
    #----------------- CLICK SIGN UP --------------------------------
    sign_up = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit']")
        )
    )
    sign_up.click()
    print("Sign up button clicked....")
    time.sleep(5)




    driver.quit()


if __name__ == "__main__":
    buy_item()
    #new_account()
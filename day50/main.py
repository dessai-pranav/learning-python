import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TINDER_URL = "https://tinder.com/"

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")


driver = webdriver.Chrome(options=chrome_options)


wait = WebDriverWait(driver, 2)


driver.get(TINDER_URL)

login = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Log in')]"))
)

login.click()
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

GYM_URL ="https://appbrewery.github.io/gym/"
ACCOUNT_EMAIL = "student@test.com"
ACCOUNT_PASS = "password123"
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service = Service("/usr/bin/chromedriver")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service,options=chrome_options)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
wait = WebDriverWait(driver, 2)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver.get(GYM_URL)
login_button = driver.find_element(by=By.ID,value="login-button")
login_button.click()
email = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "email-input"))
)
email.send_keys(ACCOUNT_EMAIL)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "password-input"))
)
password.send_keys(ACCOUNT_PASS)
submit_button = driver.find_element(By.ID,value="submit-button")
submit_button.click()


wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))
ok_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='OK']")))
ok_button.click()
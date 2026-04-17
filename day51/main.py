import os
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

PROMISED_DOWN = 150
PROMISED_UP = 10
service = Service("/usr/bin/chromedriver")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)

        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()

        time.sleep(30)

        try:
            self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
            time.sleep(30)
            self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text

            print(self.down)
            print(self.up)

        except Exception as e:
            print("Error:", e)


    def tweet_at_provider(self):
        self.driver.get("https://x.com/i/flow/login")
        time.sleep(3)

        go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()

        time.sleep(30)


speed = InternetSpeedTwitterBot()
speed.get_internet_speed()
speed.tweet_at_provider()
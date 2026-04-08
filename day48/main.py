from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("/usr/bin/chromedriver")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service,options=chrome_options)
driver.get("https://www.amazon.com")

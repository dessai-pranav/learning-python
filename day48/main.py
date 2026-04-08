from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service = Service("/usr/bin/chromedriver")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service,options=chrome_options)
driver.get("https://www.python.org/")

# price_Dollar = driver.find_element(By.CLASS_NAME,value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME,value="a-price-fraction")
# print(f"The price is rupees {price_Dollar.text}.{price_cents.text}")
# search_bar = driver.find_element(By.NAME,value="q")
# print(search_bar.get_attribute("placeholder"))
# button =driver.find_element(By.NAME,value="submit")
# print(button.size)
driver.quit()

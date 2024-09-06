from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, '#id')
driver.find_element(By.CSS_SELECTOR, '.class')
driver.find_element(By.CSS_SELECTOR, 'tag#id.class')
driver.find_element(By.CSS_SELECTOR, ".class[attr='xxx'][attr='xx']")
# partial match
driver.find_element(By.CSS_SELECTOR, ".class[href*='notif']")

## to check in browser console
# $$(".class")
# $$("#id")
# $$("tag#id.class")
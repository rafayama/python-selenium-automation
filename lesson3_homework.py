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

# 1. Find the most optimal locators for Create Account on amazon.com (Registration) page elements:

driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&prevRID=HT7YXKWHXNV7HE64THAE&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# Amazon logo
driver.find_element(By.CSS_SELECTOR, '.a-icon-logo')

# "Create account" string
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

# your name field
driver.find_element(By.ID, 'ap_customer_name')

# email field
driver.find_element(By.ID, 'ap_email')

# password field
driver.find_element(By.ID, 'ap_password')

# password description
driver.find_element(By.CSS_SELECTOR, '#ap_password_context_message_section .a-alert-inline-info')

# re-enter password field
driver.find_element(By.ID, 'ap_password_check')

# create you amazon account button
driver.find_element(By.ID, 'continue')

# conditions of use link
driver.find_element(By.XPATH, '//a[contains(href, "condition_of_use")]')

# privacy notice link
driver.find_element(By.XPATH, '//a[contains(href, "privacy_notice"]')

# Sign in link
driver.find_element(By.CSS_SELECTOR, '.a-link-emphasis')

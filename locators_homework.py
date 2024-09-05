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



# 1 Practice with locators
# # Amazon logo
# driver.find_element(By.XPATH, "//i[@class='a-icon-logo' and aria-label='Amazon']")
# # Email field
# driver.find_element(By.ID, 'ap_email')
# # Continue button
# driver.find_element(By.XPATH, "//input[@aria-labelledby='continue-announce']")
# # Conditions of use link
# driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF8&amp;nodeId=508088']")
# # Privacy Notice link
# driver.find_element(By.XPATH, "//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&amp;nodeId=468496']")
# # Need help link
# driver.find_element(By.XPATH, "//a[@data-action='a-expander-toggle']")
# # Forgot your password link
# driver.find_element(By.ID, 'auth-fpp-link-bottom')
# # Other issues with Sign-In link
# driver.find_element(By.ID, 'ap-other-signin-issues-link')
# # Create your Amazon account button
# driver.find_element(By.ID, 'createAccountSubmit')

# 2 Create a test case for the Sign in page using python and selenium script
driver.get('https://www.target.com/')

driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
sleep(2)
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
sleep(2)

actual_result = driver.find_element(By.XPATH, "//h1//span").text
expected_result = "Sign into your Target account"

assert  expected_result in actual_result, f"Expected {expected_result} but got {actual_result}"
print("'Sign into your Target account' is shown")

driver.find_element(By.ID, 'login')
print('login button is shown')
sleep(4)

# 3 Build a test case from scratch to search for a product on Target

driver.get('https://www.target.com/')

driver.find_element(By.XPATH, "//input[@data-test='@web/Search/SearchInput']").send_keys('lego')
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(2)

current_result = driver.find_element(By.XPATH, "//h1[@data-test='page-title']").text

actual_result = "LEGO"

assert current_result in actual_result, f"Expected {actual_result} but got {current_result}"

print("string is correct")
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

driver.get('https://www.target.com/')

# Search field > tea
driver.find_element(By.ID, 'search').send_keys('tea')

# Search button > click
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(5) # because target website is slow it needs to have a pause
# Verification
actual_result = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
expected_result = 'teafasfa' # incorrect string
# expected_result = 'tea' # correct string

assert expected_result in actual_result, f'Expected {expected_result} but got {actual_result}'
print('test case passed')

driver.quit()


# sleep(6)
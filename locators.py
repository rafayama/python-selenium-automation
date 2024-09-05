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

# open the url
driver.get('https://www.globo.com/')

# populate search field
# search = driver.find_element(By.NAME, 'q')

#locate element
# driver.find_element() # by,000, value=''

#to test in browser console
# $x("//tag[@attr='value']")
# $x("//a[text()='Best Sellers']")
# $x("//a[text()='Best Sellers' and @class='nav-a']")

# by id
driver.find_element(By.ID, 'banner_home3_container')
driver.find_element(By.ID, 'banner_home3')

#by xpath 1 attr
driver.find_element(By.XPATH, "//img[@alt='Ar de BH está 10 vezes mais poluído que OMS recomenda']")
driver.find_element(By.XPATH, "//input[@placeholder='Encontre na globo.com']")

#by xpath more than one attr
driver.find_element(By.XPATH, '//a[@class="homeui-tc-esporte" and @href="https://ge.globo.com/?utm_source=globo.com&amp;utm_medium=header" and @target="_self"]')

#by text
driver.find_element(By.XPATH, "//a[text()='globoplay']")

#by text or attr with any tag
driver.find_element(By.XPATH, "//*[text()='globoplay']")
driver.find_element(By.XPATH, "//*[text()='globoplay' and @class='header-title']")

#by text and attr
driver.find_element(By.XPATH, "//a[text()='globoplay' and @class='header-title']")

#by attr, parent
driver.find_element(By.XPATH, "//div[@id='nav-main'//a[text()='globoplay']")

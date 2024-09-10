from lib2to3.fixes.fix_input import context

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('Search for {product}')
def search_for_product(context, product):
    # add tea to search field
    context.driver.find_element(By.ID, 'search').send_keys(product)
    # Search button > click
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)


@then('Verify that correct search results shown for {product}')
def verify_results(context, product):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    # expected_result = 'teafasfa'  # incorrect string

    assert product in actual_result, f'Expected {product} but got {actual_result}'


# lesson 3 homework exercise 2
@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']").click()
    sleep(5)


@then('Verify that your cart is empty message is shown')
def verify_cart_empty(context):
    context.driver.find_element(By.XPATH, "//div[@data-test='boxEmptyMsg']")


# lesson 3 homework exercise 3

@when('Click Sign in')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
    sleep(2)


@when('From right side navigation menu, click Sign In')
def click_sign_in_sidebar(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
    sleep(5)


@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    context.driver.find_element(By.XPATH, "//h1//span[text()='Sign into your Target account']").click()
    context.driver.find_element(By.XPATH, "//form")

@then('Verify that header has {expected_amount} links')
def verify_header_links(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(By.CSS_SELECTOR, 'data-test*="@web/GlobalHeader"')
    print(links)
    assert len(links) == expected_amount, f'Expected {expected_amount} links, got {len(links)}'

@then('Verify that header is shown')
def verify_header(context):
    context.driver.find_element(By.CSS_SELECTOR, '[class*="utilityHeaderContainer"]')

@then('Verify that header has links')
def verify_header_links_shown(context):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    assert len(links) > 0

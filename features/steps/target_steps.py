from lib2to3.fixes.fix_input import context

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCart']")
LISTING_PRODUCT = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
LISTING_PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
LISTING_PRODUCT_IMAGE = (By.CSS_SELECTOR, "[data-test='@web/ProductCard/ProductCardImage/primary'] img")

@given('Open target main page')
def open_main(context):
    # context.driver.get('https://www.target.com/')
    context.app.main_page.open_main()

@given('Open Target Circle page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')


@given('Open Target Help page')
def open_target_circle(context):
    context.driver.get(' https://help.target.com/help ')


@when('Search for {product}')
def search_for_product(context, product):
    # # add tea to search field
    # context.driver.find_element(By.ID, 'search').send_keys(product)
    # # Search button > click
    # context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    context.app.header.search_product(product)

@then('Verify that correct search results shown for {product}')
def verify_results(context, product):
    # actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    # # expected_result = 'teafasfa'  # incorrect string
    # assert product in actual_result, f'Expected {product} but got {actual_result}'
    context.app.search_results_page.verify_results(product)

# lesson 3 homework exercise 2
@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']").click()


@then('Verify that your cart is empty message is shown')
def verify_cart_empty(context):
    context.driver.find_element(By.XPATH, "//div[@data-test='boxEmptyMsg']")


# lesson 3 homework exercise 3

@when('Click Sign in')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()


@when('From right side navigation menu, click Sign In')
def click_sign_in_sidebar(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()


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


@then('Verify that there are {benefit_cells} benefit cells')
def verify_benefit_cells(context, benefit_cells):
    main_cells = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='@web/slingshot-components/CellsComponent/Link']")

    assert len(main_cells) == int(benefit_cells)


@when('Click on product image')
def click_product(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/ProductCard/ProductCardImage']").click()
    sleep(5)


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(5)
    # Waits for target element to be loaded
    # context.driver.wait.until(EC.visibility_of_element_located(ADD_TO_CART_BTN))


@then('Verify that cart has items')
def verify_item(context):
    context.driver.get('https://www.target.com/cart')
    # sleep(5)
    cart_item = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='cartItem']")
    assert len(cart_item) > 0


@then('Verify that Help Title is shown')
def verify_help_title(context):
    # context.driver.find_element(By.XPATH, "//h2[text()='Target Help']")
    context.driver.find_element(By.CSS_SELECTOR, ".bio h2")


@then('Verify that Help search field is shown')
def verify_search_field(context):
    context.driver.find_element(By.XPATH, "//input[@placeholder='search help']")


@then('Verify that Help search icon is shown')
def verify_search_field(context):
    context.driver.find_element(By.CSS_SELECTOR, ".search-btn")


@then('Verify that there are {boxes} boxes in the What would you like to do')
def verify_boxes(context, boxes):
    amount = context.driver.find_elements(By.CSS_SELECTOR, '.col-lg-12 .grid_6')
    assert len(amount) == int(boxes), f'Expected {boxes} boxes, got {len(amount)}'


@then('Verify that there are {boxes} boxes under')
def verify_boxes_under(context, boxes):
    amount = context.driver.find_elements(By.CSS_SELECTOR, '.grid_4')
    assert len(amount) == int(boxes)


@then('Verify that Browse all Help pages title is shown')
def verify_browse_all_help_title(context):
    context.driver.find_element(By.XPATH, "//h2[text()='Browse all Help pages']")


@then('Verify that each result has a name and image')
def verify_result_name(context):
    # to see all listings
    context.driver.execute_script("window.scrollBy(0, 2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0, 2000)", "")

    results = context.driver.find_elements(*LISTING_PRODUCT)
    amount_of_results = len(results)
    print(amount_of_results)
    for result in results:
        title = result.find_element(*LISTING_PRODUCT_TITLE).text
        assert title != ''
        print(title)
        img = result.find_element(*LISTING_PRODUCT_IMAGE)
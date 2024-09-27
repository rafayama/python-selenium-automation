from behave import given, when, then


@given('Open sign in page')
def open_target_app(context):
    context.app.login_page.open_login_page()

@when('Click Target terms and conditions link')
def click_pp_link(context):
    context.app.login_page.click_tc_link()

@then('Verify Terms and Conditions page opened')
def verify_tc_opened(context):
    context.app.login_page.verify_tc_opened()


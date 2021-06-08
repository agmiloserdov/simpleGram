from behave import when, then


@when('I click to logout button')
def click_logout_button(context):
    context.browser.find_element_by_css_selector('#logout').click()


@then("Site redirect me to login page")
def should_be_at_login(context):
    assert context.browser.current_url == 'http://localhost:8000/accounts/login/?next=/'

from behave import given, when, then


@given('Open "login" page')
def open_login_page(context):
    context.browser.get('http://localhost:8000/accounts/login/')


@then("I see login page")
def should_be_at_login(context):
    assert context.browser.current_url == 'http://localhost:8000/accounts/login/?next=/'


@then('I see message text "{text}"')
def see_error_with_text(context, text):
    error = context.browser.find_element_by_css_selector('.form-text.text-danger')
    assert error.text == text

from behave import fixture
from django.contrib.auth.models import User


@fixture
def signup_to_app_as_root(context):
    context.browser.get('http://localhost:8000/accounts/login/')
    context.browser.find_element_by_name("username").send_keys("root")
    context.browser.find_element_by_name("password").send_keys("root")
    context.browser.find_element_by_css_selector('button').click()



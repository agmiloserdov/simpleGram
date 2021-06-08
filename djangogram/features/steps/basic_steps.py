import os
from time import sleep

from behave import when, given, use_fixture, step, then

from features.steps.fixtures.auth import signup_to_app_as_root


@when("I click to profile button")
def open_profile(context):
    button = context.browser.find_element_by_id("profile")
    button.click()


@when("I see profile page")
def should_be_at_profile(context):
    username = context.browser.find_element_by_class_name('username')
    assert username.text == 'root'


@when('I click to "{text}" button')
def click_by_link_text(context, text):
    sleep(3)
    button = context.browser.find_element_by_link_text(text)
    button.click()


@when('I upload image into field "{name}"')
def upload_image(context, name):
    field = context.browser.find_element_by_name(name)
    field.send_keys(os.path.abspath('features/steps/tmp_data/test_image.jpg'))


@given("I signed up and I on profile page")
def go_to_profile_page(context):
    use_fixture(signup_to_app_as_root, context)
    context.browser.find_element_by_id('profile').click()


@step('I see "{field_name}" field')
def should_see_field(context, field_name):
    field = context.browser.find_element_by_name(field_name)
    assert field


@step('I see "{text}" in "{selector}"')
def should_see_data(context, text, selector):
    fullname = context.browser.find_element_by_class_name(selector)
    sleep(2)
    assert fullname.text == text


@when("I see a post list")
def should_see_posts(context):
    assert context.browser.find_element_by_class_name('post')


@when('Input text "{text}" into field "{name}"')
def enter_text(context, text, name):
    field = context.browser.find_element_by_name(name)
    field.clear()
    field.send_keys(text)


@when('Submit the form')
def submit_form(context):
    context.browser.find_element_by_css_selector('button').click()


@then('I see main page')
def should_be_at_main(context):
    assert context.browser.current_url == 'http://localhost:8000/'


@given('I signed up and I on main page')
def open_main_page(context):
    use_fixture(signup_to_app_as_root, context)
    context.browser.get('http://localhost:8000/')


@given(u'I on main page')
def open_main_page(context):
    context.browser.get('http://localhost:8000/')


@when('I input text "{text}" into field "{selector}" by id')
def input_search_data(context, text, selector):
    context.browser.find_element_by_id(selector).send_keys(text)
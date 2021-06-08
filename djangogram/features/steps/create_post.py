import os
from time import sleep

from behave import *

from features.steps.fixtures.auth import signup_to_app_as_root


@then("I see create post page")
def should_be_at_new_post_page(context):
    assert context.browser.current_url == 'http://localhost:8000/posts/add'


@given("I signed up and I on create post page")
def open_post_create(context):
    use_fixture(signup_to_app_as_root, context)
    context.browser.get('http://localhost:8000/posts/add')


@then('I see post with title "{title}" and description "{description}"')
def should_see_new_post(context, title, description):
    post_title = context.browser.find_element_by_class_name('title_text')
    assert post_title.text == title
    assert context.browser.find_element_by_class_name('description').text == description


@step('I upload incorrect filetype "{file}" into field "{name}"')
def upload_incorrect_file(context, file, name):
    field = context.browser.find_element_by_name(name)
    field.send_keys(os.path.abspath(f'features/steps/tmp_data/{file}'))
    sleep(5)

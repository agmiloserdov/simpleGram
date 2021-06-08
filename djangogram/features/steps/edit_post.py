from time import sleep

from behave import *


@then('I see edit post page with heading "{text}"')
def should_see_correct_heading(context, text):
    sleep(2)
    heading = context.browser.find_element_by_id('post_modalLabel')
    assert heading.text == text


@step("I see edit form")
def check_edit_form(context):
    sleep(2)
    title = context.browser.find_element_by_name('title')
    description = context.browser.find_element_by_name('description')
    assert context.browser.find_element_by_tag_name('form')
    assert title.get_attribute('value') and description.get_attribute('value')

from behave import *
from selenium.webdriver import ActionChains

from features.steps.delete_post import PostTestObject

post_obj = PostTestObject()


@then("I see post page")
def should_be_at_post_page(context):
    url = context.browser.current_url
    assert url == post_obj.post_link


@when('I click to "{selector}" icon link')
def click_details_icon(context, selector):
    post = context.browser.find_element_by_class_name('profile-post')
    hover = ActionChains(context.browser).move_to_element(post)
    hover.perform()
    icon = context.browser.find_element_by_class_name(selector)
    post_obj.set_post_link(icon.get_attribute('href'))
    icon.click()

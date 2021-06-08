from time import sleep

from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from features.steps.fixtures.auth import signup_to_app_as_root


class PostTestObject:
    def set_post_id(self, post_id):
        self.id = post_id

    def set_post_link(self, post_link):
        self.post_link = post_link


post_test_obj = PostTestObject()


@when('I click to "{selector}" icon')
def click_delete_icon(context, selector):
    post = context.browser.find_element_by_class_name('profile-post')
    hover = ActionChains(context.browser).move_to_element(post)
    hover.perform()
    delete_icon = context.browser.find_element_by_class_name(selector)
    post_test_obj.set_post_id(delete_icon.get_attribute('id'))
    delete_icon.click()


@when('I see heading "{heading}"')
def should_see_title(context, heading):
    sleep(3)
    title = context.browser.find_element_by_id('modal_title').text
    assert title == heading


@when('I click "{button_id}" button')
def click_confirm_delete(context, button_id):
    confirm_delete = context.browser.find_element_by_id(button_id)
    confirm_delete.click()


@then("I see that post has been deleted")
def should_not_see_post(context):
    posts_not_found_message = ""
    try:
        context.browser.find_element_by_id(f'post_{post_test_obj.id}')
        posts_not_found_message = context.browser.find_element_by_id('post_empty').text
        post_not_found = False
    except NoSuchElementException:
        post_not_found = True
    assert post_not_found or posts_not_found_message == "Пользователь еще не опубликовал ни одной записи"

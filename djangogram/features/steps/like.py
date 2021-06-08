from time import sleep

from behave import *

use_step_matcher("re")


class Counter:
    def __init__(self):
        self.base_counter = ""
        self.new_counter = ""

    def set_new_counter(self, new_counter):
        self.new_counter = new_counter

    def set_base_counter(self, base_counter):
        self.base_counter = base_counter


counter = Counter()





@then("I click to like button")
def click_to_like(context):
    button = context.browser.find_element_by_class_name('like')
    sleep(2)
    like_counter = context.browser.find_element_by_css_selector('.counters .like .fa').text
    counter.set_base_counter(like_counter)
    button.click()


@step("I see that the counter has changed")
def counter_should_be_changed(context):
    sleep(2)
    like_counter = context.browser.find_element_by_css_selector('.counters .like .fa').text
    counter.set_new_counter(like_counter)
    assert counter.new_counter != counter.base_counter

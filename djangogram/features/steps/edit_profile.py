from time import sleep

from behave import *
from django.urls import reverse


class UserData:
    def set_user_id(self, user_id):
        self.user_id = user_id


user_data = UserData()


@then('I see edit profile page with "{selector}" form')
def should_i_see_form(context, selector):
    form = context.browser.find_element_by_class_name(selector)
    user_id = form.find_element_by_tag_name('form').get_attribute('id')
    user_data.set_user_id(user_id)
    assert form





@then("I see profile page")
def should_be_at_profile(context):
    current_url = reverse('insta:profile', kwargs={'pk': user_data.user_id})
    sleep(5)
    assert context.browser.current_url == 'http://localhost:8000' + current_url




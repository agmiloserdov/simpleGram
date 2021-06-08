from time import sleep

from behave import then


@then('I see link with "{text}" username in "{selector}"')
def view_search_result(context, text, selector):
    sleep(3)
    username = context.browser.find_element_by_id(selector).text
    assert username == text


@then('I see empty window with "{text}"')
def empty_result(context, text):
    sleep(3)
    result_text = context.browser.find_element_by_class_name('form-text')
    assert result_text.text == text

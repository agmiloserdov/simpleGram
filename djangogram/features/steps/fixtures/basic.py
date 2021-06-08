from behave import fixture
from selenium.webdriver import Chrome


@fixture
def browser_chrome(context):
    context.browser = Chrome('D:\\Python\\django\\tests_env\\chromedriver.exe')
    yield context.browser
    context.browser.quit()

from behave import use_fixture

from features.steps.fixtures.basic import browser_chrome


def before_all(context):
    use_fixture(browser_chrome, context)

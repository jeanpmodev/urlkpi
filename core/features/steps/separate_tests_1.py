from behave import *


@given('you installed Django Octo 1.')
def step_impl(context):
    pass


@when('you run specific test 1')
def step_impl(context):
    assert True is not False


@then('You test it in the administrative interface 1.')
def step_impl(context):
    assert context.failed is False

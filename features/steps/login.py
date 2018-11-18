from behave import given, when, then
import time

# correct_email = 'test@drugdev.com'
# correct_password = 'supers3cret'
# incorrect_email = 'test@drugdev.com'
# incorrect_password = 'supers3cret'


@given(u'the user has the correct credentials')
def step_impl(context):
    context.browser.visit()
    # context.browser.get('https://sprinkle-burn.glitch.me/')
    # context.assertEqual(correct_email,'test@drugdev.com','Not the correct email')
    # context.assertEqual(correct_password,'supers3cret','Not the correct password')
    # raise NotImplementedError(
    #     u'STEP: Given the user has the correct credentials')


@when(u"the user enters {theUsername} username")
def step_impl(context,theUsername):
    context.browser.find_by_id('#login-form > fieldset > div:nth-child(2) > input',theUsername)
    time.sleep(2)



@when(u'the user enters {thePassword} password')
def step_impl(context,thePassword):
    context.browser.find_by_id('#login-form > fieldset > div:nth-child(3) > input',thePassword)
    time.sleep(2)


@when(u'clicks Login')
def step_impl(context):
    context.browser.click_by_id("#login-form > fieldset > div.flex > button")
    time.sleep(2)




@then(u'the user is presented with a welcome message {wellcomeMessage}')
def step_impl(context,wellcomeMessage):
    context.browser.check_message(wellcomeMessage)


@given(u'the user has the incorrect credentials')
def step_impl(context):
    context.browser.visit()


@then(u'the user is presented with a error message {value}')
def step_impl(context,value):
    context.browser.credential_error("#login-error-box",value)
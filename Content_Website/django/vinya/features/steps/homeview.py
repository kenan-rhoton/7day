from behave import given, when, then
from test.factories.user import UserFactory

from selenium.common.exceptions import NoSuchElementException

INDEX_PAGE = '/site/'

@given(u'I am not logged in')
def step_impl(context):
    from django.contrib.auth.models import User

    u = UserFactory(username='foo', email='foo@example.com')
    u.set_password('bar')

    u.save()

@given(u'I am on the HomePage')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + INDEX_PAGE)

@when(u'I log in')
def step_impl(context):
    br = context.browser

    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    br.find_element_by_id('login_user').send_keys('foo')
    br.find_element_by_id('login_pass').send_keys('bar')
    br.find_element_by_name('submit').click()

@then(u'I should see the Latest Posts Block')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_id('latest_posts')

@then(u'I should see the Login Form')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_id('login_user')
    assert br.find_element_by_id('login_pass')

@then(u'I should see the Logout Button')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_id('logout_button')

@then(u'I should not see the New Form Button')
def step_impl(context):
    br = context.browser
    found = False
    try:
        br.find_element_by_id('post_submit')
        found = True
    except NoSuchElementException:
        found = False
    assert found == False

@then(u'I should be able to Logout')
def step_impl(context):
    br = context.browser
    br.find_element_by_id('logout_button').click()


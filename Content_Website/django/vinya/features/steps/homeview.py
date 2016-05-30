from behave import given, when, then
from test.factories.user import UserFactory

@given(u'I am not logged in')
def step_impl(context):
    from django.contrib.auth.models import User

    u = UserFactory(username='foo', email='foo@example.com')
    u.set_password('bar')

    u.save()

@given(u'I am on the HomePage')
def step_impl(context):
    br = context.browser
    br.get(context.base_url)

@then(u'I should see the Latest Posts Block')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_id('latest_posts')



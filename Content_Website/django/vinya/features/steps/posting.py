from behave import given, when, then
from test.factories.user import UserFactory
from django.contrib.auth.models import Permission

INDEX_PAGE = '/site/'

@given(u'I am logged in with posting capabilities')
def step_impl(context):
    from django.contrib.auth.models import User

    u = UserFactory(username='foo', email='foo@example.com')
    u.set_password('bar')
    permission = Permission.objects.get(codename='add_post')
    u.user_permissions.add(permission)

    u.save()

    br = context.browser
    br.get(context.base_url + INDEX_PAGE)

    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    br.find_element_by_id('login_user').send_keys('foo')
    br.find_element_by_id('login_pass').send_keys('bar')
    br.find_element_by_name('submit').click()

@given(u'I see a New Post button')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_id('new_post_button')

@when(u'I create a New Post')
def step_impl(context):
    br = context.browser
    br.find_element_by_id('post_title').send_keys('DA TITLE')
    br.find_element_by_id('post_content').send_keys('DA CONTENT')
    br.find_element_by_id('post_submit').click()


@then(u'it should appear on the HomePage')
def step_impl(context):
    pass


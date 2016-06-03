from behave import given, when, then
from test.factories.user import UserFactory
from django.contrib.auth.models import Permission
from website.models import Post

INDEX_PAGE = '/site/'

@given(u'I am logged in with posting capabilities')
def step_impl(context):
    from django.contrib.auth.models import User

    u = UserFactory(username='foo', email='foo@example.com')
    u.set_password('bar')
    permission = Permission.objects.get(codename='add_post')
    u.user_permissions.add(permission)
    permission = Permission.objects.get(codename='change_post')
    u.user_permissions.add(permission)
    permission = Permission.objects.get(codename='delete_post')
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
    assert br.find_element_by_id('post_submit')

@when(u'I create a New Post')
def step_impl(context):
    br = context.browser
    br.find_element_by_id('post_title').send_keys('DA TITLE')
    br.find_element_by_id('post_content').send_keys('DA CONTENT')
    br.find_element_by_id('post_submit').click()

@when(u'I create a New Post with title "{title}" and content "{content}"')
def step_impl(context, title, content):
    br = context.browser
    br.find_element_by_id('post_title').send_keys(title)
    br.find_element_by_id('post_content').send_keys(content)
    br.find_element_by_id('post_submit').click()


@then(u'it should appear on the HomePage')
def step_impl(context):
    response = context.test.client.get(context.base_url + INDEX_PAGE)
    context.test.assertContains(response, 'DA TITLE')

@then(u'I should see "{text}" on the HomePage')
def step_impl(context, text):
    response = context.test.client.get(context.base_url + INDEX_PAGE)
    context.test.assertContains(response, text)

@given(u'There is a Post with title "{title}" and content "{content}"')
def step_impl(context, title, content):
    Post.objects.create(title=title, content=content)

@then(u'I should be able to delete the first Post with title "{text}"')
def step_impl(context, text):
    br = context.browser
    br.find_element_by_class_name('delete_post').click()
    response = context.test.client.get(context.base_url + INDEX_PAGE)
    context.test.assertNotContains(response, text)

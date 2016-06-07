from behave import given, when, then
from test.factories.user import UserFactory

from selenium.common.exceptions import NoSuchElementException

ADMIN_PAGE = '/admin/'

@given(u'I am logged in on the Admin Site')
def step_impl(context):
    from django.contrib.auth.models import User

    u = UserFactory(username='foo', email='foo@example.com')
    u.set_password('bar')
    u.is_superuser=True
    u.is_staff=True

    u.save()

    br = context.browser
    br.get(context.base_url + ADMIN_PAGE)

    br.find_element_by_id('id_username').send_keys('foo')
    br.find_element_by_id('id_password').send_keys('bar')
    br.find_element_by_xpath("//input[@type='submit']").click()

@then(u'I should see the Admin Panel')
def step_impl(context):
    br = context.browser
    br.find_element_by_class_name('model-section')

@when(u'I add a new Section "{name}" with block "{block}"')
def step_impl(context, name, block):
    br = context.browser
    br.find_element_by_xpath("//tr[@class='model-section']//a[@class='addlink']").click()
    br.find_element_by_id('id_name').send_keys(name)
    br.find_element_by_id('id_block').send_keys(block)
    br.find_element_by_xpath("//input[@type='submit']").click()

@then(u'I should see a Section "{name}" on the Section List')
def step_impl(context, name):
    br = context.browser
    br.get(context.base_url + '/admin/website/section/')
    br.find_element_by_link_text(name)

@when(u'I delete the Section "{name}"')
def step_impl(context, name):
    br = context.browser
    br.get(context.base_url + '/admin/website/section/')
    br.find_element_by_link_text(name).click()
    br.find_element_by_link_text('Delete').click()

@then(u'I should not see a Section "{name}" on the Section List')
def step_impl(context, name):
    response = context.test.client.get(context.base_url +  '/admin/website/section/', follow=True)
    context.test.assertNotContains(response, name)


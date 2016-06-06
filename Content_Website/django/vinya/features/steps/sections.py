from behave import given, when, then
from test.factories.user import UserFactory
from django.contrib.auth.models import Permission
from django.shortcuts import get_object_or_404
from website.models import Post, Section
from selenium.webdriver.support.ui import Select

@given(u'There is a Section "{name}" assigned to "{block}"')
def step_impl(context, name, block):
    Section.objects.create(name=name, block=block)

@given(u'There is a Post assigned to section "{section}" with title "{title}" and content "{content}"')
def step_impl(context, section, title, content):
    p = Post.objects.create(title=title, content=content)
    p.save()
    section = get_object_or_404(Section, name=section)
    p.addSection(section)
    p.save()

@then(u'I should see a link to "{link_name}" on the HomePage inside the "{where}"')
def step_impl(context, link_name, where):
    br = context.browser
    br.find_element_by_xpath("//div[@id='" + where + "']//a[contains(.,'"+link_name+"')]")

@when(u'I click on the link to "{link_name}" inside the "{where}"')
def step_impl(context, link_name, where):
    br = context.browser
    br.find_element_by_xpath("//div[@id='" + where + "']//a[contains(.,'"+link_name+"')]").click()

@when(u'I create a New Post on section "{section}" with title "{title}" and content "{content}"')
def step_impl(context, section, title, content):
    br = context.browser
    br.find_element_by_id('post_title').send_keys(title)
    br.find_element_by_id('post_content').send_keys(content)
    Select(br.find_element_by_id('post_section')).select_by_visible_text(section)
    br.find_element_by_id('post_submit').click()

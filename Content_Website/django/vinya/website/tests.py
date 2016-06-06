from django.test import TestCase

from django.core.urlresolvers import reverse

from .models import Post, Section
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class PostTests(TestCase):

    def test_post_is_created_correctly(self):
        new_post = Post(title = "Mah title", content = "Mah content")
        new_post.save()
        self.assertEqual(new_post,Post.objects.all()[0])

    def test_newest_post_appears_in_homepage(self):
        new_post = Post(title = "Mah title", content = "Mah content")
        new_post.save()
        response = self.client.get(reverse("website:HomePage"))
        self.assertContains(response, "Mah content")


class UserTests(TestCase):
    
    def test_user_can_be_authenticated_if_it_exists(self):
        u = User.objects.create_user('paco', 'lucia@elcrack.es', 'flanesyqueso')
        self.assertIsNotNone(authenticate(username='paco', password='flanesyqueso'))

    def test_user_cant_be_authenticated_if_it_doesnt_exists(self):
        self.assertIsNone(authenticate(username='paco', password='flanesyqueso'))


class SectionTests(TestCase):

    def test_post_starts_without_sections(self):
        new_post = Post(title = "Mah title", content = "Mah content")
        new_post.save()
        self.assertEqual(0,new_post.sections.count())

    def test_post_can_have_a_section(self):
        new_post = Post(title = "Mah title", content = "Mah content")
        new_post.save()
        sec = Section(name="Potatoes")
        sec.save()
        new_post.addSection(sec)
        self.assertEqual(1,new_post.sections.count())

    def test_adding_post_to_section_increases_post_count_of_section(self):
        new_post = Post(title = "Mah title", content = "Mah content")
        new_post.save()
        sec = Section(name="Potatoes")
        sec.save()
        new_post.addSection(sec)
        sec.refresh_from_db()
        self.assertEqual(1,len(sec.post_set.all()))

    def test_deleting_post_removes_from_section_post_list(self):
        new_post = Post(title = "Mah title", content = "Mah content")
        new_post.save()
        sec = Section(name="Potatoes")
        sec.save()
        new_post.addSection(sec)
        sec.refresh_from_db()
        new_post.refresh_from_db()
        new_post.delete()
        sec.refresh_from_db()
        self.assertEqual(0,len(sec.post_set.all()))



class BlockTests(TestCase):

    def setUp(self):
        self.new_post = Post(title = "Mah title", content = "Mah content")
        self.new_post.save()
        self.sec = Section(name="Potatoes")
        self.sec.save()
        self.new_post.addSection(self.sec)

    def test_sections_can_be_on_a_block(self):
        self.sec.addToBlock("Top")
        self.sec.refresh_from_db()
        self.sec.block == "Top"

from django.test import TestCase

from django.core.urlresolvers import reverse

from .models import Post

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

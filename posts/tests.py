from django.test import TestCase, Client
from django.urls import reverse

class Contacts(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get(reverse("view-get_index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/index.html")

    def test_contacts(self):
        response = self.client.get(reverse("view-get_contacts"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/contacts.html")
        
    def test_about(self):
        response = self.client.get(reverse("view-get_about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/about.html")     
        
    def test_update_post(self):
        response = self.client.get(reverse("post-update"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/update_post.html")
        
    def test_create_post(self):
        response = self.client.get(reverse("post-create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/create_post.html")
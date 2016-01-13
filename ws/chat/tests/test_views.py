from django.core.urlresolvers import reverse
from django.test import TestCase


class IndexTests(TestCase):

    def test_get(self):
        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["headline"], "Broadcast Chat")
        self.assertIn("Broadcast Chat", response.content.decode('utf8'))

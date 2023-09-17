from django.test import TestCase
# commentaires


def test_dummy():
    assert 1


class IndexViewTestCase(TestCase):
    """ Classe de test pour la page d'accueil """

    def test_index(self):
        """ Test pour la page d'accueil """
        response = self.client.get('/')
        html_content = response.content
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to Holiday Homes", html_content)

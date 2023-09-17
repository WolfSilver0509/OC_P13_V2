from django.test import TestCase
from django.urls import reverse


class LettingsTestCase(TestCase):
    """ Classe de tests pour l'application 'lettings'. """
    fixtures = ['lettings.json']

    def test_lettings_index(self):
        """
        Teste la page d'accueil des biens locatifs.

        Vérifie si la page d'accueil ('lettings_index') renvoie un code de réponse HTTP 200
        et si le contenu HTML de la page contient le texte "Lettings".

        """
        url = reverse('lettings_index')
        response = self.client.get(url)
        html_content = response.content
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Lettings", html_content)

    def test_lettings(self):
        """
        Teste la page des détails d'un bien locatif.

        Vérifie si la page des détails ('letting') renvoie un code de réponse HTTP 200.

        """
        url = reverse('letting', kwargs={'letting_id': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

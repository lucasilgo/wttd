# coding: utf-8

from django.test import TestCase
from eventex.subscriptions.models import Subscription

class DetailTest(TestCase):
    def setUp(self):
        s = Subscription.objects.create(name='Lucas Gomes', cpf='12345678901',
            email='lucasilgo@hotmail.com', phone='27-998682764')
        self.resp = self.client.get('/inscricao/%d/' %(s.pk))

    def test_get(self):
        """Se retornar 200 o get da página ocorreu com sucesso"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """O template é o correto"""
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_details.html')

    def test_context(self):
        """Verifica se a página possui uma instancia de subscription"""
        sub = self.resp.context['subscription']
        self.assertIsInstance(sub, Subscription)

    def test_html(self):
        """A página contém qual informação"""
        self.assertContains(self.resp, 'Lucas Gomes')

class DetailNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get('/inscricao/0/')
        self.assertEqual(404, response.status_code)
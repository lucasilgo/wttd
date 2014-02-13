# coding: utf-8

from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription

class SubscribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        """
        GET /inscricao/ must return the status 200
        """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """
        Test the rendering template
        """
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_Html(self):
        """
        HTML must contains input controls
        """
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 3)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        """
        HTML contains csrf token
        """
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """
        If have a subscription form
        """
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

class SubscribePostTest(TestCase):
    """Testes relacionados ao envio de formulário"""
    def setUp(self):
        data = dict(name='Lucas Gomes', cpf='12345678901',
            email='lucasilgo@hotmail.com', phone='27-998682764')
        self.resp = self.client.post('/inscricao/', data)

    def test_post(self):
        """Testa a validação ao enviar um POST"""
        self.assertEqual(self.resp.status_code, 302)

    def test_save(self):
        """Testa se o dado de fato foi salvo no banco"""
        self.assertTrue(Subscription.objects.exists())

class SubscribeInvalidPostTest(TestCase):
    """Testes relacionados ao formulário inválido"""
    def setUp(self):
        data = dict(name='Lucas Gomes', cpf='039283120938120381',
            email='lucasilgo@hotmail.com', phone='27-998682764')
        self.resp = self.client.post('/inscricao/', data)

    def test_post(self):
        """Testa se o formulário será enviado"""
        self.assertEqual(200, self.resp.status_code)

    def test_save(self):
        """Não pode salvar com dados inválidos"""
        self.assertFalse(Subscription.objects.exists())

    def test_errors(self):
        """Caso o formulário seja inválido, os erros devem ser mostrados"""
        self.assertTrue(self.resp.context['form'].errors)
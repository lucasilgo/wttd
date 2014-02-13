# coding: utf-8

from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        """
        The form has 4 fields
        """
        form = SubscriptionForm()
        self.assertItemsEqual(form.fields, ['name', 'email', 'cpf', 'phone'])
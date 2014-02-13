# coding: utf-8

from django.test import TestCase
from eventex.subscriptions.models import Subscription
from datetime import datetime
from django.db import IntegrityError

class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name = 'Lucas Gomes',
            cpf = '12345678901',
            email = 'lucas@example.com',
            phone = '27-84938293'
        )

    def test_unicode(self):
        self.assertEqual(u'Lucas Gomes', unicode(self.obj))

    def test_create(self):
        """
        Create and save an object in BD
        """
        self.obj.save()
        self.assertEqual(1, self.obj.pk)

    def test_created_at(self):
        """
        If created_at have a type datetime
        """
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        Subscription.objects.create(
            name = 'Lucas Gomes',
            cpf = '12345678901',
            email = 'lucas@example.com',
            phone = '27-39238273'
        )

    def test_cpf_unique(self):
        """
        CPF is unique
        """
        s = Subscription(
            name = 'Lucas Gomes',
            cpf = '12345678901',
            email = 'lucasilgo@example.com',
            phone = '27-39238273'
        )
        self.assertRaises(IntegrityError, s.save)

    def test_email_unique(self):
        """
        Email is unique
        """
        s = Subscription(
            name = 'Lucas Gomes',
            cpf = '12345678902',
            email = 'lucas@example.com',
            phone = '27-39238273'
        )
        self.assertRaises(IntegrityError, s.save)
from django.test import TestCase

from accounts.tests.factories import UserFactory
from .factories import PaymentFactory, PaymentOrderFactory


class PaymentModelTestCase(TestCase):

    def test_save(self):
        p = PaymentFactory.build()
        self.assertEqual(p.save(), None)


class PaymentOrderTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory()

    def test_save(self):
        p = PaymentOrderFactory.build(
            user=self.user,
        )
        self.assertEqual(p.save(), None)

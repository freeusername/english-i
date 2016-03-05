from django.test import TestCase

from .factories import ConfigFactory


class GalleryTestCase(TestCase):

    def test_save(self):
        config = ConfigFactory.build()
        self.assertEqual(config.save(), None)

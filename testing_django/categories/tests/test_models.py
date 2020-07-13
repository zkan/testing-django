import os
from unittest.mock import MagicMock

from django.core.files import File
from django.test import TestCase

from ..models import Category


class TestCategory(TestCase):
    def test_catgory_should_have_defined_fields(self):
        # Given
        name = 'Personal'
        photo_mock = MagicMock(spec=File)
        photo_mock.name = 'test.png'

        # When
        category = Category.objects.create(name=name, photo=photo_mock)

        # Then
        self.assertEqual(category.name, name)
        self.assertEqual(category.photo.name, photo_mock.name)

        os.remove(f'media/{photo_mock.name}')

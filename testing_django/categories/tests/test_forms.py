import os
from unittest.mock import MagicMock

from django.core.files import File
from django.test import TestCase

from ..forms import CategoryForm
from ..models import Category


class TestCategoryForm (TestCase):
    def test_form_valid(self):
        category_name = 'Test Category'
        photo_mock = MagicMock(spec=File)
        photo_mock.name = 'test.png'

        form = CategoryForm(
            data={
                'name': category_name
            },
            files={
                'photo': photo_mock
            }
        )
        form.is_valid()
        form.save()

        category = Category.objects.last()
        self.assertEqual(category.name, category_name)
        self.assertEqual(category.photo.name, photo_mock.name)

        os.remove(f'media/{photo_mock.name}')

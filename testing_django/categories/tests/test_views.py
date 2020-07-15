import os
from unittest.mock import MagicMock

from django.core.files import File
from django.test import TestCase
from django.urls import reverse

from ..models import Category


class TestCategoryList(TestCase):
    def test_category_list_should_display_on_page(self):
        # Given
        Category.objects.create(name='Street Food')
        Category.objects.create(name='Elite')

        # When
        response = self.client.get(reverse('category_list'))

        # Then
        self.assertContains(response, '<li>Street Food</li>')
        self.assertContains(response, '<li>Elite</li>')

        assert '<li>Street Food</li>' in str(response.content)

    def test_add_new_category(self):
        # Given
        category_name = 'Test Category'
        photo_mock = MagicMock(spec=File)
        photo_mock.name = 'test.png'
        data = {
            'name': category_name,
            'photo': photo_mock
        }

        # When
        response = self.client.post(reverse('category_list'), data=data)

        # Then
        assert response.status_code == 200

        category = Category.objects.last()
        self.assertEqual(category.name, category_name)
        self.assertEqual(category.photo.name, photo_mock.name)

        os.remove(f'media/{photo_mock.name}')

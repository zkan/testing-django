from django.test import TestCase

from ..models import Category


class TestCategory(TestCase):
    def test_catgory_should_have_name_field(self):
        # Given
        name = 'Personal'

        # When
        category = Category.objects.create(name=name)

        # Then
        self.assertEqual(category.name, name)

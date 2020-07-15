import os
from unittest.mock import MagicMock

from django.core.files import File
from django.test import TestCase
from django.urls import reverse

from ..models import Category
from ..serializers import CategorySerializer


class TestCategorySerializers(TestCase):
    def test_category_serializer_should_have_defined_fields(self):
        # Given
        category = Category.objects.create(name='Street Food')

        # When
        category_serializer = CategorySerializer(category)

        # Then
        assert category_serializer.data == {'name': 'Street Food', 'photo': None}

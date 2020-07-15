from django.contrib import admin
from django.test import TestCase

from ..admin import CategoryAdmin
from ..models import Category


class CategoryAdminTest(TestCase):
    def test_admin_should_be_registered(self):
        assert isinstance(admin.site._registry[Category], CategoryAdmin)

    def test_admin_should_set_list_display(self):
        expected = (
            'name',
            'photo',
        )
        assert CategoryAdmin.list_display == expected

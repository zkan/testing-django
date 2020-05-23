#from django.shortcuts import render

from django.http import HttpResponse
from django.views import View

from .models import Category


class CategoryList(View):
    def get(self, request):
        categories = Category.objects.all()

        html = ''
        for category in categories:
            html += f'<li>{category.name}</li>'

        return HttpResponse(html)
#from django.shortcuts import render

from django.http import HttpResponse
from django.views import View

from .forms import CategoryForm
from .models import Category


class CategoryList(View):
    form_class = CategoryForm

    def get(self, request):
        categories = Category.objects.all()

        html = ''
        for category in categories:
            html += f'<li>{category.name}</li>'

        return HttpResponse(html)

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return HttpResponse()

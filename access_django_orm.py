import os
import sys

import django


# Add the project to sys.path, so that Python can find packages
PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "testing_django")
sys.path.append(PROJECT_ROOT)

# Set up the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testing_django.settings")
django.setup()


if __name__ == "__main__":
    from categories.models import Category

    categories = Category.objects.all()
    for index, each in enumerate(categories, start=1):
        print(f"{index}. {each.name}")

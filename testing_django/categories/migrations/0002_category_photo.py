# Generated by Django 3.0.6 on 2020-07-13 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='photo',
            field=models.FileField(default=None, upload_to=''),
            preserve_default=False,
        ),
    ]

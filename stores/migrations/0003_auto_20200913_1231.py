# Generated by Django 2.1.5 on 2020-09-13 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_store_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]

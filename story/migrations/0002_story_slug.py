# Generated by Django 3.2.5 on 2021-07-26 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='slug',
            field=models.SlugField(allow_unicode=True, default=' ', max_length=500, unique=True),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-30 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_sliders_slugedtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sliders',
            name='slugedtitle',
        ),
    ]

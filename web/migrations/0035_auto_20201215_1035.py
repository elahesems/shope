# Generated by Django 3.1.4 on 2020-12-15 10:35

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0034_auto_20201215_0847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='colorField',
            field=colorfield.fields.ColorField(blank=True, default=None, max_length=18, null=True, verbose_name='renk'),
        ),
    ]
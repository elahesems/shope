# Generated by Django 3.1.4 on 2020-12-16 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0045_auto_20201215_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
    ]

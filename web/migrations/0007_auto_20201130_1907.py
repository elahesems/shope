# Generated by Django 3.1.3 on 2020-11-30 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20201130_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='inDate',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='giriş tarihi'),
        ),
    ]

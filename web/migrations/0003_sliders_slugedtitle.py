# Generated by Django 3.1.3 on 2020-11-30 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20201130_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='sliders',
            name='slugedtitle',
            field=models.SlugField(blank=True, null=True, verbose_name=models.CharField(blank=True, max_length=100, null=True, verbose_name='en ust sırada yazılacak')),
        ),
    ]

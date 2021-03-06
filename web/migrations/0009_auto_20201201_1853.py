# Generated by Django 3.1.3 on 2020-12-01 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20201130_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='gender',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='web.CategoryTag'),
        ),
    ]

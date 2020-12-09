# Generated by Django 3.1.4 on 2020-12-09 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0025_auto_20201209_0559'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='brandin Ismi')),
                ('brandslogo', models.ImageField(upload_to='', verbose_name='logo')),
            ],
            options={
                'verbose_name_plural': 'BRaNDs',
            },
        ),
        migrations.AlterModelOptions(
            name='seyirci',
            options={'verbose_name_plural': 'ConTaCt'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='brandsname',
        ),
        migrations.RemoveField(
            model_name='product',
            name='brandspic',
        ),
        migrations.AddField(
            model_name='product',
            name='brandsby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.brands', verbose_name='brand'),
        ),
    ]
# Generated by Django 3.1.1 on 2020-09-30 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localizacao', '0004_auto_20200927_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidade',
            name='slug',
            field=models.SlugField(blank=True, default=' ', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='regiao',
            name='slug',
            field=models.SlugField(blank=True, default=' ', max_length=250, null=True),
        ),
    ]
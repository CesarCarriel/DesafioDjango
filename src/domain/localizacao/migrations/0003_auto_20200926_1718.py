# Generated by Django 3.1.1 on 2020-09-26 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localizacao', '0002_cidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regiao',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
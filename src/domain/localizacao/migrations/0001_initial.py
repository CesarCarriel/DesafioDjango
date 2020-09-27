# Generated by Django 3.1.1 on 2020-09-26 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Regiao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('nome', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
            ],
        ),
    ]

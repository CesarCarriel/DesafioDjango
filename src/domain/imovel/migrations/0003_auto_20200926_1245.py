# Generated by Django 3.1.1 on 2020-09-26 15:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('imovel', '0002_auto_20200926_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipo',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tipo',
            name='modificado_em',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# Generated by Django 3.2.7 on 2021-09-29 19:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_auto_20210929_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='facebook',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='instagram',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='usuarios/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='twitter',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
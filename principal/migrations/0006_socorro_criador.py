# Generated by Django 3.2.7 on 2021-09-17 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0005_auto_20210917_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='socorro',
            name='criador',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='criador', to='principal.usuario'),
            preserve_default=False,
        ),
    ]
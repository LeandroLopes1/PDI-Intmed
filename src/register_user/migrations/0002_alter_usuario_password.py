# Generated by Django 4.0.5 on 2022-07-06 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(error_messages={'max_length': 'A senha deve ter no máximo 8 caracteres'}, max_length=8),
        ),
    ]

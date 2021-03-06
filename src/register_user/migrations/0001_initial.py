# Generated by Django 4.0.5 on 2022-07-06 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(error_messages={'unique': 'Este email ja esta cadastrado'}, max_length=255, unique=True)),
                ('password', models.CharField(max_length=6)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

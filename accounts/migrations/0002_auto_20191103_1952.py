# Generated by Django 2.2.6 on 2019-11-03 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='ativo',
        ),
        migrations.RemoveField(
            model_name='user',
            name='data_cadastro',
        ),
        migrations.RemoveField(
            model_name='user',
            name='equipe',
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data de entrada'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Equipe'),
        ),
    ]

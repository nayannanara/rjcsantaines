# Generated by Django 2.2.6 on 2019-10-27 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20191027_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='encontreiro',
            name='ano_participacao',
            field=models.IntegerField(null=True, verbose_name='ano de participacao'),
        ),
        migrations.AddField(
            model_name='encontreiro',
            name='pessoa_convite_enc',
            field=models.CharField(max_length=30, null=True, verbose_name='padrinho ou madrinha'),
        ),
    ]
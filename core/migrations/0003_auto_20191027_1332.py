# Generated by Django 2.2.6 on 2019-10-27 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191027_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encontreiro',
            name='estado_encontreiro',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='estado'),
        ),
    ]

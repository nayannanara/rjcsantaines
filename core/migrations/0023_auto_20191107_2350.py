# Generated by Django 2.2.6 on 2019-11-08 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20191107_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encontreiro',
            name='status',
        ),
        migrations.RemoveField(
            model_name='encontrista',
            name='status',
        ),
    ]
# Generated by Django 2.2.6 on 2019-10-27 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20191027_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encontreiro',
            name='ano_participacao',
        ),
        migrations.RemoveField(
            model_name='encontreiro',
            name='curso_encontreiro',
        ),
        migrations.RemoveField(
            model_name='encontreiro',
            name='equipes_trab',
        ),
        migrations.RemoveField(
            model_name='encontreiro',
            name='escolaridade_enc',
        ),
        migrations.RemoveField(
            model_name='encontreiro',
            name='frequentando_igreja_enc',
        ),
        migrations.RemoveField(
            model_name='encontreiro',
            name='local_trabalho_enc',
        ),
        migrations.RemoveField(
            model_name='encontreiro',
            name='nome_igreja',
        ),
        migrations.RemoveField(
            model_name='encontreiro',
            name='pessoa_convite_enc',
        ),
        migrations.RemoveField(
            model_name='encontreiro',
            name='qtd_participacoes',
        ),
    ]

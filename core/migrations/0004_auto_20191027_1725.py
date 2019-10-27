# Generated by Django 2.2.6 on 2019-10-27 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20191027_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='encontreiro',
            name='ano_participacao',
            field=models.IntegerField(null=True, verbose_name='ano de participacao'),
        ),
        migrations.AddField(
            model_name='encontreiro',
            name='curso_encontreiro',
            field=models.CharField(max_length=70, null=True, verbose_name='Curso'),
        ),
        migrations.AddField(
            model_name='encontreiro',
            name='equipes_trab',
            field=models.CharField(blank=True, max_length=70, null=True, verbose_name='equipes_que trabalhou'),
        ),
        migrations.AddField(
            model_name='encontreiro',
            name='escolaridade_enc',
            field=models.CharField(max_length=30, null=True, verbose_name='escolaridade'),
        ),
        migrations.AddField(
            model_name='encontreiro',
            name='frequentando_igreja_enc',
            field=models.CharField(max_length=5, null=True, verbose_name='frequentando igreja'),
        ),
        migrations.AddField(
            model_name='encontreiro',
            name='local_trabalho_enc',
            field=models.CharField(max_length=40, null=True, verbose_name='local de trabalho'),
        ),
        migrations.AddField(
            model_name='encontreiro',
            name='nome_igreja',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='encontreiro',
            name='pessoa_convite_enc',
            field=models.CharField(max_length=30, null=True, verbose_name='padrinho ou madrinha'),
        ),
        migrations.AddField(
            model_name='encontreiro',
            name='qtd_participacoes',
            field=models.IntegerField(null=True, verbose_name='Quantidade de participações'),
        ),
        migrations.AlterField(
            model_name='encontreiro',
            name='bairro_encontreiro',
            field=models.CharField(max_length=25, null=True, verbose_name='bairro'),
        ),
        migrations.AlterField(
            model_name='encontreiro',
            name='cidade_encontreiro',
            field=models.CharField(max_length=30, null=True, verbose_name='cidade'),
        ),
        migrations.AlterField(
            model_name='encontreiro',
            name='estado_encontreiro',
            field=models.CharField(max_length=26, null=True, verbose_name='estado'),
        ),
    ]

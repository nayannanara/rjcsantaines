# Generated by Django 2.2.6 on 2019-10-27 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20191027_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='encontrista',
            name='curso',
            field=models.CharField(max_length=50, null=True, verbose_name='escolaridade'),
        ),
        migrations.AddField(
            model_name='encontrista',
            name='desejo_participacao',
            field=models.CharField(max_length=150, null=True, verbose_name='desejo participacao'),
        ),
        migrations.AddField(
            model_name='encontrista',
            name='escolaridade',
            field=models.CharField(max_length=40, null=True, verbose_name='escolaridade'),
        ),
        migrations.AddField(
            model_name='encontrista',
            name='local_trabalho',
            field=models.CharField(max_length=40, null=True, verbose_name='local trabalho'),
        ),
        migrations.AddField(
            model_name='encontrista',
            name='nome_escola',
            field=models.CharField(max_length=60, null=True, verbose_name='nome escola'),
        ),
        migrations.AddField(
            model_name='encontrista',
            name='nome_pessoas_participando',
            field=models.CharField(max_length=60, null=True, verbose_name='nome pessoas participando'),
        ),
        migrations.AddField(
            model_name='encontrista',
            name='nome_probsaude',
            field=models.CharField(max_length=60, null=True, verbose_name='nome probsaude'),
        ),
        migrations.AddField(
            model_name='encontrista',
            name='pergunta_jesus',
            field=models.CharField(max_length=150, null=True, verbose_name='Jesus pra você'),
        ),
        migrations.AddField(
            model_name='encontrista',
            name='pessoa_convite_enct',
            field=models.CharField(max_length=40, null=True, verbose_name='padrinho ou madrinha'),
        ),
        migrations.AddField(
            model_name='encontrista',
            name='pessoas_moradia',
            field=models.CharField(max_length=60, null=True, verbose_name='pessoas moradia'),
        ),
        migrations.AddField(
            model_name='encontrista',
            name='pessoas_participando',
            field=models.CharField(max_length=5, null=True, verbose_name='pessoas participando'),
        ),
        migrations.AddField(
            model_name='encontrista',
            name='possui_automovel',
            field=models.CharField(max_length=5, null=True, verbose_name='possui automovel'),
        ),
        migrations.AddField(
            model_name='encontrista',
            name='possui_probsaude',
            field=models.CharField(max_length=5, null=True, verbose_name='possui probsaude'),
        ),
        migrations.AddField(
            model_name='encontrista',
            name='telefone_pessoa_convite',
            field=models.CharField(max_length=40, null=True, verbose_name='telefone_pessoa_convite'),
        ),
        migrations.AddField(
            model_name='encontrista',
            name='telefones_urgencia',
            field=models.CharField(max_length=40, null=True, verbose_name='telefones urgencia'),
        ),
    ]

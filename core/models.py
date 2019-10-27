from django.db import models


class Encontreiro(models.Model):
    nome = models.CharField(max_length=60, null=False, blank=False, verbose_name='nome')
    data_nascimento = models.DateField(auto_now=False, null=True, verbose_name='data nascimento')
    cpf = models.CharField(unique=True, max_length=15, null=True, blank=False, verbose_name='cpf')
    celular = models.CharField(max_length=15, null=True, blank=False, verbose_name='celular')
    email = models.EmailField(max_length=50, null=True, blank=False, verbose_name='email')
    estado_civil = models.CharField(max_length=40, null=True, blank=False, verbose_name='estado_civil')
    facebook = models.CharField(max_length=50, null=True, blank=False, verbose_name='facebook')
    cep_encontreiro = models.CharField(max_length=11, null=False, blank=False)
    naturalidade_encontreiro = models.CharField(max_length=40, null=True, blank=False, verbose_name='naturalidade')
    logradouro_encontreiro = models.CharField(max_length=40, null=True, blank=False, verbose_name='logradouro')
    numero_encontreiro = models.IntegerField(null=True, verbose_name='numero')
    complemento_encontreiro = models.CharField(max_length=60, null=True, blank=False, verbose_name='complemento')
    bairro_encontreiro = models.CharField(max_length=25, null=True, blank=False, verbose_name='bairro')
    estado_encontreiro = models.CharField(max_length=26, null=True, blank=False,verbose_name='estado')
    cidade_encontreiro = models.CharField(max_length=30, null=True, blank=False, verbose_name='cidade')
    frequentando_igreja_enc = models.CharField(max_length=5, null=True, verbose_name='frequentando igreja')
    nome_igreja = models.CharField(max_length=50, null=True, blank=False, verbose_name='nome da igreja')
    local_trabalho_enc = models.CharField(max_length=40, null=True, blank=False, verbose_name='local de trabalho')
    escolaridade_enc = models.CharField(max_length=30, null=True, blank=False, verbose_name='escolaridade')
    pessoa_convite_enc = models.CharField(max_length=30, null=True, blank=False, verbose_name='padrinho ou madrinha')
    ano_participacao = models.IntegerField(null=True, blank=False, verbose_name='ano de participacao')
    equipes_trab = models.CharField(max_length=70, null=True, blank=False, verbose_name='equipes que trabalhou')
    curso_encontreiro = models.CharField(max_length=70, null=True, blank=False, verbose_name='Curso')
    qtd_participacoes = models.IntegerField(null=True, blank=False, verbose_name='Quantidade de participações')

    def __str__(self):
        return self.nome


class Encontrista(models.Model):
    nome_apelido = models.CharField(max_length=60, null=True, blank=False, verbose_name='nome apelido')
    data_nascimento_enc = models.DateField(auto_now=False, null=True, verbose_name='data nascimento')
    cpf = models.CharField(unique=True, max_length=15, null=True, blank=False, verbose_name='cpf')
    celular = models.CharField(max_length=15, null=True, blank=False, verbose_name='celular')
    estado_civil = models.CharField(max_length=40, null=True, blank=False, verbose_name='estado_civil')
    cep = models.CharField(max_length=10, null=True, blank=False, verbose_name='cep')
    logradouro = models.CharField(max_length=40, null=True, blank=False, verbose_name='rua')
    numero = models.IntegerField(null=True, verbose_name='numero')
    complemento = models.CharField(max_length=60, null=True, blank=False, verbose_name='complemento')
    bairro = models.CharField(max_length=25, null=True, blank=False, verbose_name='bairro')
    estado = models.CharField(max_length=4, null=True, blank=False, verbose_name='estado')
    cidade = models.CharField(max_length=30, null=True, blank=False, verbose_name='cidade')
    naturalidade = models.CharField(max_length=40, null=True, blank=False, verbose_name='naturalidade')
    email = models.EmailField(max_length=50, null=True, blank=False, verbose_name='email')
    facebook = models.CharField(max_length=50, null=True, blank=False, verbose_name='facebook')
    frequenta_igreja = models.CharField(max_length=5, null=True, blank=False, verbose_name='frequenta_igreja')
    religiao = models.CharField(max_length=30, null=True, blank=False, verbose_name='religiao')
    nome_pai = models.CharField(max_length=60, null=True, blank=False, verbose_name='nome_pai')
    religiao_pai = models.CharField(max_length=30, null=True, blank=False, verbose_name='religiao_pai')
    nome_mae = models.CharField(max_length=60, null=True, blank=False, verbose_name='nome_mae')
    religiao_mae = models.CharField(max_length=30, null=True, blank=False, verbose_name='religiao_mae')
    possui_automovel = models.CharField(max_length=5, null=True, blank=False, verbose_name='possui automovel')
    pessoas_moradia = models.CharField(max_length=60, null=True, blank=False, verbose_name='pessoas moradia')
    local_trabalho = models.CharField(max_length=40, null=True, blank=False, verbose_name='local trabalho')
    nome_escola = models.CharField(max_length=60, null=True, blank=False, verbose_name='nome escola')
    escolaridade = models.CharField(max_length=40, null=True, blank=False, verbose_name='escolaridade')
    curso = models.CharField(max_length=50, null=True, blank=False, verbose_name='escolaridade')
    pessoas_participando = models.CharField(max_length=5, null=True, blank=False, verbose_name='pessoas participando')
    nome_pessoas_participando = models.CharField(max_length=60, null=True, blank=False,
                                                 verbose_name='nome pessoas participando')
    possui_probsaude = models.CharField(max_length=5, null=True, blank=False, verbose_name='possui probsaude')
    nome_probsaude = models.CharField(max_length=60, null=True, blank=False, verbose_name='nome probsaude')
    telefones_urgencia = models.CharField(max_length=40, null=True, blank=False, verbose_name='telefones urgencia')
    pessoa_convite_enct = models.CharField(max_length=40, null=True, blank=False, verbose_name='padrinho ou madrinha')
    telefone_pessoa_convite = models.CharField(max_length=40, null=True, blank=False,
                                               verbose_name='telefone_pessoa_convite')
    desejo_participacao = models.TextField(null=True, blank=False, verbose_name='desejo participacao')
    pergunta_jesus = models.TextField(null=True, blank=False, verbose_name='Jesus pra você')

    def __str__(self):
        return self.nome_apelido


class Equipe(models.Model):
    nome_equipe = models.CharField(max_length=40, null=False, blank=False, verbose_name='nome_equipe')
    encontreiros = models.ForeignKey(Encontreiro, related_name='encontreiros',  blank=False, null=True, on_delete=models.CASCADE)
    qtd_participantes = models.IntegerField(null=True, verbose_name='qtd_participantes')
    nome_coordenador = models.OneToOneField(Encontreiro, related_name='coordenador', on_delete=models.CASCADE, null=True)
    nome_casal_ligacao = models.CharField(max_length=40, null=False, blank=False, verbose_name='nome_casal_ligacao')

    def __str__(self):
        return self.nome_equipe


class Circulo(models.Model):
    nome_circulo = models.CharField(max_length=40, null=False, blank=False, verbose_name='nome_circulo')
    encontristas = models.ForeignKey(Encontrista, blank=False, null=True, on_delete=models.CASCADE)
    qtd_participantes = models.IntegerField(null=True, verbose_name='qtd_participantes')
    lider_circulo = models.OneToOneField(Encontreiro, on_delete=models.CASCADE, null=True)
    cor_equipe = models.CharField(max_length=20, null=False, blank=False, verbose_name='cor_equipe')

    def __str__(self):
        return self.nome_circulo
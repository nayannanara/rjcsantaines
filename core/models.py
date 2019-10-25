from django.db import models


class Encontreiro(models.Model):
    nome = models.CharField(max_length=60, null=False, blank=False, verbose_name='nome')
    email = models.EmailField(max_length=50, null=False, blank=False, verbose_name='email')
    facebook = models.EmailField(max_length=50, null=False, blank=False, verbose_name='facebook')
    naturalidade = models.CharField(max_length=40, null=False, blank=False, verbose_name='naturalidade')
    cpf = models.CharField(unique=True, max_length=15, null=True, blank=False, verbose_name='cpf')
    celular = models.CharField(max_length=15, null=False, blank=False, verbose_name='celular', default="", editable=False)
    data_nascimento = models.DateField(auto_now=False, null=True, verbose_name='data_nascimento')
    frequentando_igreja = models.CharField(max_length=5, null=True, verbose_name='frequentando_igreja')
    nome_igreja = models.CharField(max_length=50, null=True, blank=True)
    cep = models.CharField(max_length=10, null=True, blank=False, verbose_name='cep')
    logradouro = models.CharField(max_length=40, null=True, blank=False, verbose_name='rua')
    numero = models.IntegerField(null=True, verbose_name='numero')
    complemento = models.CharField(max_length=60, null=True, blank=False, verbose_name='complemento')
    bairro = models.CharField(max_length=25, blank=True, verbose_name='bairro')
    estado = models.CharField(max_length=4, null=True, verbose_name='estados')
    cidade = models.CharField(max_length=30, null=True, verbose_name='idades')
    local_trabalho = models.CharField(max_length=40, null=True, blank=False,verbose_name='local_trabalho')
    escolaridade = models.CharField(max_length=30, null=True, blank=False, verbose_name='escolaridade')
    pessoa_convite = models.CharField(max_length=30, null=True, blank=False, verbose_name='pessoa_convite')
    ano_participacao = models.IntegerField(null=True, verbose_name='ano_participacao')
    equipes_trab = models.CharField(max_length=70, null=True, blank=True, verbose_name='equipes_trab')
    curso = models.CharField(max_length=70, null=True, blank=True, verbose_name='curso')
    qtd_participacoes = models.IntegerField(null=True, verbose_name='qtd_participacoes')

    def __str__(self):
        return self.nome


class Encontrista(models.Model):
    nome_apelido = models.CharField(max_length=60, null=False, blank=False, verbose_name='nome_apelido')
    possui_automovel = models.CharField(max_length=5, null=False, blank=False, verbose_name='possui_automovel')
    nome_escola = models.CharField(max_length=60, null=False, blank=False, verbose_name='nome_escola')
    possui_probsaude = models.CharField(max_length=5, null=False, blank=False, verbose_name='possui_probsaude')
    nome_probsaude = models.CharField(max_length=60, null=False, blank=False, verbose_name='nome_probsaude')
    pessoas_moradia = models.CharField(max_length=60, null=False, blank=False, verbose_name='pessoas_moradia')
    telefones_urgencia = models.CharField(max_length=40, null=False, blank=False, verbose_name='telefones_urgencia')
    pessoa_convite = models.CharField(max_length=40, null=False, blank=False, verbose_name='pessoa_convite')
    telefone_pessoa_convite = models.CharField(max_length=40, null=False, blank=False, verbose_name='telefone_pessoa_convite')
    pessoas_participando = models.CharField(max_length=5, null=False, blank=False, verbose_name='pessoas_participando')
    nome_pessoas_participando = models.CharField(max_length=60, null=False, blank=False, verbose_name='nome_pessoas_participando')
    nome = models.CharField(max_length=60, null=False, blank=False, verbose_name='nome')
    religiao = models.CharField(max_length=30, null=False, blank=False, verbose_name='religiao')
    frequenta_igreja = models.CharField(max_length=5, null=False, blank=False, verbose_name='frequenta_igreja')
    nome_pai = models.CharField(max_length=60, null=False, blank=False, verbose_name='nome_pai')
    religiao_pai = models.CharField(max_length=30, null=False, blank=False, verbose_name='religiao_pai')
    nome_mae = models.CharField(max_length=60, null=False, blank=False, verbose_name='nome_mae')
    religiao_mae = models.CharField(max_length=30, null=False, blank=False, verbose_name='religiao_mae')
    email = models.EmailField(max_length=50, null=False, blank=False, verbose_name='email')
    facebook = models.EmailField(max_length=50, null=False, blank=False, verbose_name='facebook')
    naturalidade = models.CharField(max_length=40, null=False, blank=False, verbose_name='naturalidade')
    cpf = models.CharField(unique=True, max_length=15, null=True, blank=False, verbose_name='cpf')
    celular = models.CharField(max_length=15, null=False, blank=False, verbose_name='celular', default="", editable=False)
    data_nascimento = models.DateField(auto_now=False, null=True, verbose_name='data_nascimento')
    cep = models.CharField(max_length=10, null=True, blank=False, verbose_name='cep')
    logradouro = models.CharField(max_length=40, null=True, blank=False, verbose_name='rua')
    numero = models.IntegerField(null=True, verbose_name='numero')
    complemento = models.CharField(max_length=60, null=True, blank=False, verbose_name='complemento')
    bairro = models.CharField(max_length=25, blank=True, verbose_name='bairro')
    estado = models.CharField(max_length=4, null=True, verbose_name='estados')
    cidade = models.CharField(max_length=30, null=True, verbose_name='idades')
    local_trabalho = models.CharField(max_length=40, null=True, blank=False,verbose_name='local_trabalho')
    endereco_trabalho = models.CharField(max_length=60, null=True, blank=False, verbose_name='endereco_trabalho')
    desejo_participacao = models.CharField(max_length=150, null=True, blank=True, verbose_name='desejo_participacao')
    pergunta_jesus = models.CharField(max_length=150, null=True, blank=True, verbose_name='pergunta_jesus')

    def __str__(self):
        return self.nome


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
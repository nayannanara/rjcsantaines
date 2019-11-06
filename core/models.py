from django.db import models


class Encontreiro(models.Model):
    nome = models.CharField('Nome', null=True, max_length=60)
    data_nascimento = models.DateField('Data de nascimento', null=True, auto_now=False)
    cpf = models.CharField('CPF', unique=True, null=True, max_length=15)
    celular = models.CharField('Celular',  null=True, max_length=15)
    email = models.EmailField('Email',  null=True, max_length=50)
    estado_civil = models.CharField('Estado civil',  null=True, max_length=40)
    facebook = models.CharField('Facebook', null=True,  max_length=50)
    cep_encontreiro = models.CharField('CEP',  null=True, max_length=11)
    naturalidade_encontreiro = models.CharField('Naturalidade', null=True,  max_length=40)
    logradouro_encontreiro = models.CharField('Logradouro', null=True, max_length=40)
    numero_encontreiro = models.IntegerField('Numero', null=True)
    complemento_encontreiro = models.CharField('Complemento', null=True, max_length=60)
    bairro_encontreiro = models.CharField('Bairro', null=True, max_length=25)
    estado_encontreiro = models.CharField('Estado', null=True, max_length=26)
    cidade_encontreiro = models.CharField('Cidade', null=True, max_length=30)
    frequentando_igreja_enc = models.CharField('Está frequentando a igreja?', null=True, max_length=5)
    nome_igreja = models.CharField('Nome da igreja', null=True, max_length=50)
    local_trabalho_enc = models.CharField('Local de trabalho',null=True,  max_length=40)
    escolaridade_enc = models.CharField('Escolaridade', null=True, max_length=30)
    pessoa_convite_enc = models.CharField('Padrinho ou madrinha', null=True, max_length=30)
    ano_participacao = models.IntegerField('Ano de participação', null=True)
    equipes_trab = models.CharField('Equipes que já trabalhou', null=True, max_length=70)
    curso_encontreiro = models.CharField('Curso', max_length=70, null=True, blank=True)
    qtd_participacoes = models.IntegerField('Quantidade de participações', null=True)
    data_cadastro = models.DateTimeField('Inscrito em', null=True, auto_now_add=True)

    def __str__(self):
        return self.nome


class Encontrista(models.Model):
    nome_apelido = models.CharField('Nome apelido', null=True, max_length=60)
    data_nascimento_enc = models.DateField('Data de nascimento', null=True, auto_now=False)
    cpf = models.CharField('CPF', unique=True, null=True, max_length=15)
    celular = models.CharField('Celular', null=True, max_length=15)
    estado_civil = models.CharField('Estado civil', null=True, max_length=40)
    cep = models.CharField('CEP', null=True, max_length=10)
    logradouro = models.CharField('Logradouro', null=True, max_length=40)
    numero = models.IntegerField('Numero', null=True)
    complemento = models.CharField('Complemento', null=True, max_length=60)
    bairro = models.CharField('Bairro', null=True, max_length=25)
    estado = models.CharField('Estado', null=True, max_length=4)
    cidade = models.CharField('Cidade', null=True, max_length=30)
    naturalidade = models.CharField('Naturalidade', null=True, max_length=40)
    email = models.EmailField('Email', null=True, max_length=50)
    facebook = models.CharField('Facebook', null=True, max_length=50)
    frequenta_igreja = models.CharField('Está frequentando alguma igreja?', null=True, max_length=5)
    religiao = models.CharField('Religião', null=True, max_length=30)
    nome_pai = models.CharField('Nome do pai', null=True, max_length=60)
    religiao_pai = models.CharField('Religião do pai', null=True, max_length=30)
    nome_mae = models.CharField('Nome da mãe', null=True, max_length=60)
    religiao_mae = models.CharField('Religião da mãe', null=True, max_length=30)
    possui_automovel = models.CharField('Possui automóvel?', null=True, max_length=5)
    pessoas_moradia = models.CharField('Quem mora na mesma residência', null=True, max_length=60)
    local_trabalho = models.CharField('Local de trabalho', null=True, max_length=40)
    nome_escola = models.CharField('Nome da escola', null=True, max_length=60)
    escolaridade = models.CharField('Escolaridade', null=True, max_length=40)
    curso = models.CharField('Curso', null=True, max_length=50)
    pessoas_participando = models.CharField('Algum conhecido participando do programa?', null=True, max_length=5)
    nome_pessoas_participando = models.CharField('Nome das pessoas', null=True, max_length=60)
    possui_probsaude = models.CharField('Possui algum problema de saúde?', null=True, max_length=5)
    nome_probsaude = models.CharField('Qual problema de saúde', null=True, max_length=60)
    telefones_urgencia = models.CharField('Telefones para urgência', null=True, max_length=40)
    pessoa_convite_enct = models.CharField('Quem o convidou?', null=True, max_length=40)
    telefone_pessoa_convite = models.CharField('Telefone do encontreiro', null=True, max_length=40)
    desejo_participacao = models.TextField('Porque deseja participar do programa?', null=True)
    pergunta_jesus = models.TextField('Quem é Jesus para você?', null=True)
    data_cadastro = models.DateTimeField('Inscrito em', null=True, auto_now_add=True)

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
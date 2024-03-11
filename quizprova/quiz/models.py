from django.db import models
from django.utils import timezone

class Banca(models.Model):
    descricao = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='Bancas'

    def __str__(self):
        return self.descricao

class Orgao(models.Model):
    descricao = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='Órgãos'

    def __str__(self):
        return self.descricao

class Concurso(models.Model):
    descricao = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='Concursos'

    def __str__(self):
        return self.descricao    

class Cargo(models.Model):
    descricao = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='Cargos'

    def __str__(self):
        return self.descricao    

class Disciplina(models.Model):
    descricao = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='Disciplinas'

    def __str__(self):
        return self.descricao

class Assunto(models.Model):
    disciplina = models.ForeignKey(Disciplina,on_delete=models.CASCADE,related_name='disciplina_assunto')
    descricao = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='Assuntos'

    def __str__(self):
        return self.descricao    

class Prova(models.Model):

    class Escolaridade(models.TextChoices):
        MEDIO = 'M', 'Médio'
        SUPERIOR = 'S', 'Superior'

    banca = models.ForeignKey(Banca,on_delete=models.CASCADE,related_name='banca_prova')
    orgao = models.ForeignKey(Orgao,on_delete=models.CASCADE,related_name='orgao_prova')
    concurso = models.ForeignKey(Concurso,on_delete=models.CASCADE,related_name='concurso_prova')
    cargo = models.ForeignKey(Cargo,on_delete=models.CASCADE,related_name='cargo_prova')
    descricao = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250)
    escolaridade = models.CharField(max_length=1,
                                    choices=Escolaridade.choices,
                                    default=Escolaridade.MEDIO)
    ano = models.IntegerField(null=True)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural='Provas'

    def __str__(self):
        return self.descricao

class Questao(models.Model):
    prova = models.ForeignKey(Prova,on_delete=models.CASCADE,related_name='prova_questao')
    disciplina = models.ForeignKey(Disciplina,on_delete=models.CASCADE,related_name='disciplina_questao')
    assunto = models.ForeignKey(Assunto,on_delete=models.CASCADE,related_name='assunto_questao')
    numero = models.IntegerField(null=True)
    texto1 = models.TextField(null=True, blank=True)
    imagem1 = models.ImageField(upload_to='quiz_imgs/', null=True, blank=True)
    texto2 = models.TextField(null=True, blank=True)
    imagem2 = models.ImageField(upload_to='quiz_imgs/', null=True, blank=True)
    texto3 = models.TextField(null=True, blank=True)
    imagem3 = models.ImageField(upload_to='quiz_imgs/', null=True, blank=True)

    class Meta:
        verbose_name_plural='Questões'

    def __str__(self):
        return self.texto1    

class Resposta(models.Model):
    questao = models.ForeignKey(Questao,on_delete=models.CASCADE,related_name='questao_resposta')
    letra = models.CharField(max_length=3, null=True, blank=True)
    texto = models.TextField(null=True, blank=True)
    imagem = models.ImageField(upload_to='quiz_imgs/', null=True, blank=True)
    correta = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural='Cargos'

    def __str__(self):
        return f"{self.questao.texto1[:50]}, {self.texto[:20]}"    

class TextoAssociado(models.Model):
    questao = models.ForeignKey(Questao,on_delete=models.CASCADE,related_name='questao_textoassociado')
    texto = models.TextField()

    class Meta:
        verbose_name_plural='Textos associados'

    def __str__(self):
        return f"{self.questao.texto1[:50]}, {self.texto[:20]}"    

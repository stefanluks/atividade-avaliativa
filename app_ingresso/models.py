from django.db import models

class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=50, blank= True, null= True)
    email = models.EmailField('E-mail', max_length=50, blank= True, null= True)

    def __str__(self):
        return self.nome


class PessoaFisca(Pessoa):
    cpf = models.CharField('CPF', max_length=50, blank= True, null= True)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    nome = models.CharField('Nome', max_length= 50, blank= True, null= True)
    sigla = models.CharField('Sigla', max_length= 10, blank= True, null= True)
    data_inicio = models.DateField('data de inicio', max_length = 20, blank= True, null= True )
    realizacao = models.ForeignKey(Pessoa, on_delete = models.CASCADE, blank = True, null = True)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Ingresso(models.Model):
    descricao = models.CharField('Descrição', max_length= 100, blank= True, null= True)
    valor = models.FloatField('valor', max_length= 20, blank= True, null= True)
    evento = models.ForeignKey(Evento , on_delete= models.CASCADE, verbose_name= 'Evento')

    def __str__(self):
        return self.descricao

class Inscricao(models.Model):
    pessoa =  models.ForeignKey(Pessoa, on_delete = models.CASCADE, blank = True, null = True)
    evento =  models.ForeignKey(Evento, on_delete = models.CASCADE, blank = True, null = True)
    ingressos = models.ForeignKey(Ingresso, on_delete = models.CASCADE, blank = True, null = True)

def __str__(self):
        return 'Confirmado'       
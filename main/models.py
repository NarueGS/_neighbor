import email

from uuid import uuid4
from django.db import models
import datetime
from main.tests import ran
# Inquilinos (nome, idade, sexo, telefone, email)
# Cadastro de inquilinos
# Visualização dos inquilinos cadastrados
# Unidades (identificação, proprietário, condomínio, endereço)
# Cadastro de unidades
# Visualização das unidades cadastradas
# Despesas das unidades (descrição, tipo_despesa, valor, vencimento_fatura, status_pagamento)

GENDER = (('m','Masculino'),('f','Feminino'),('n','Neutro'),('o','Outro'),
        ('0','Prefiro não dizer'))
TYP_DESPESA = (('f','finaciamento'),('c','conta'),('r','reparo'),
            ('o','outro'))

# class DU_filtroU(models.Manager):
#     def get_queryset(self):
#         return super(DU_filtroU, self).get_queryset().filter()

class Inquilinos(models.Model):
    id = models.CharField(primary_key=True,null=False,blank=False,
        default=ran(),unique=True,editable=False,max_length=64)
    
    nome = models.CharField(max_length=50,blank=False)
    idade = models.PositiveSmallIntegerField()
    sexo = models.CharField(max_length=1,choices=GENDER,default='0')
    telefone = models.CharField(max_length=11)
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Unidades(models.Model):
    indentificacao = models.CharField(max_length=50,blank=False)
    proprietario = models.ForeignKey(Inquilinos, on_delete = models.CASCADE, related_name = 'proprietario')
    condominio = models.CharField(max_length=50)
    endereco = models.TextField()
    
    def __str__(self):
        return self.indentificacao

class Despesas_Unidades(models.Model):
    descricao = models.TextField()
    tipo_despesa = models.CharField(max_length=1,choices=TYP_DESPESA,default='o')
    valor = models.DecimalField(decimal_places=2,max_digits=30)
    vencimento_fatura = models.DateField()
    status_pagamento = models.BooleanField()
    unidade =  models.ForeignKey(Unidades, on_delete = models.CASCADE, related_name = 'unidade')
    # fU = DU_filtroU()


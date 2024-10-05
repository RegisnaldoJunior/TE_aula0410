from enum import unique

from django.db import models
from django import forms
from django.contrib.auth.models import

class OrdemServico(models.Model):
    servico = models.CharField(max_lenght=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['servico']

    def __str__(self):
        return self.servico

class Clientes(models.Model):

    SEX = [
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino')
    ]
    id = models.AutoField(unique=True)
    nome = models.CharField(max_length=50)
    sexo = models.CharField(max_length=9, choices=SEX)
    cpf = models.CharField(max_length=)

"""Clientes (Id, nome, sexo, nascimento, CPF, endereço (rua, bairro, número,
CEP), data de cadastro, telefones (Fixo, celular), e-mail)
Obs. O nome do cliente deve ser preenchido sempre – Não permitir gravação
com o nome em branco;
Os telefones devem ser mascarados (99)99999-9999
Os campos CEP e CPF também devem receber máscaras
A data atual do servidor deve ser sugerida para a data de cadastro.
Se a data de nascimento for deixada em branco, uma mensagem deve informar,
mas será permitido a gravação sem que a mesma seja preenchida;
"""

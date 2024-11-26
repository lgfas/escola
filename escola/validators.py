import re
from validate_docbr import CPF

def cpf_invalido(numero_cpf):
    cpf = CPF()
    cpf_valido = cpf.validate(numero_cpf)
    return not cpf_valido

def nome_invalido(nome):
    return not nome.isalpha()

def celular_invalido(celular):
    modelo = r'^\d{2} \d{5}-\d{4}$'
    return not re.match(modelo, celular)

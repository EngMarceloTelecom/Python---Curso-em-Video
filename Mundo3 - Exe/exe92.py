'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import date
trabalhador = {}
nome = str(input('Nome: '))
ano = int(input('Qual Ano de Nascimento? '))
ct = int(input('Nº da CTPS (0 não tem)? '))
trabalhador['Nome'] = nome
trabalhador['Idade'] = (date.today().year) - ano
if ct == 0:
    trabalhador['CTPS'] = 'não tem'
else:
    anocontra = int(input('Ano de Contratação? '))
    trabalhador['CTPS'] = ct
    trabalhador['Contratado'] = anocontra
    trabalhador['Salario'] = float(input('Salario(R$)? '))
    trabalhador['Aposentadoria'] = ((date.today().year) - ano)+((anocontra + 40) - (date.today().year))
print('='*60)
#print(trabalhador)
for k,v in trabalhador.items():
    print(f'{k} = {v}')
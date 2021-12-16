'''Faça um programa que leia Nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
'''
aluno = {}

aluno['Nome'] = str(input('Nome: ')).upper().strip()
aluno['Media'] = float(input(f'Media do {aluno["Nome"]}: '))
print()
if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
    print(f'{aluno["Nome"]} a sua Media é {aluno["Media"]}, e Você Esta APROVADO')
elif 5 <= aluno['Media'] < 7:
    aluno['Situação'] = 'Recuperação'
    print(f'{aluno["Nome"]} a sua Media é {aluno["Media"]}, e Você Esta em RECUPERAÇÃO')
else:
    aluno['Situação'] = 'Reprovado'
    print(f'{aluno["Nome"]} a sua Media é {aluno["Media"]}, e Você Esta REPROVADO')
print()
print(aluno)
print()

for k,v in aluno.items():
    print(f'{k} é igual a {v}')
print('Fim do Programa')
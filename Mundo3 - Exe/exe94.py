'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média'''

pessoas = {}
grupo = []
soma = 0
while True:
    
    nome = str(input('Nome: ')).upper()
    sexo = str(input('Sexo [M/F]: ')).upper()[0].strip()
    while sexo not in 'MF':
        sexo = str(input('Digite Somente M ou F: ')).upper()[0].strip()
    idade = int(input('Idade: '))
    soma += idade
    pessoas['Nome'] = nome
    pessoas['Sexo'] = sexo
    pessoas['Idade'] = idade
    grupo.append(pessoas.copy())
    pessoas.clear()
    resp = str(input('Quer Continua [S/N]: ')).upper()[0].strip()
    while resp not in 'NS':
        resp = str(input('Erro!!! Responta S ou N: ')).upper()[0].strip()
    if resp == 'N':
            break
#print(pessoas)
media = soma / len(grupo)
print('='*60)
print(grupo)
print('='*60)
print(f'A) {len(grupo)} de Pessos Cadastrada')
print('='*60)
print(f'B) A media de Idade é {media:5.2f}')
print('='*60)
for p in grupo:
    if p['Sexo'] == 'F':
        print(f'C) {p["Nome"]}',end=' \n')
print('='*60)
print('D) Nomes com Idades a Cima da Media')
for p in grupo:
    if p['Idade'] >= media:
        for k, v in p.items():
            print(f'{v}')

print('<<FIM>>')
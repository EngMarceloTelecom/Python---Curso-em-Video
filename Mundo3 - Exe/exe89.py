'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

ficha =[]
while True:
    nome = str(input('Nome: ')).strip().upper()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1+n2)/2
    ficha.append([nome, [n1,n2], media])

    res = str(input('Quer Contunuar? [S/N]: ')).strip().upper()[0]
    while res not in "SN":
        res = str(input('Opção Invalida, Quer Contunuar? [S/N]')).strip().upper()[0]
    if res == 'N':
        break
print('='*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":8}')

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:<8.1f}')

while True:
    print('='*30)
    opc = int(input('Mostrar Nota de Qual Aluno: (99 Stop): '))
    if opc == 99:
        break
        print('Finalizando')
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')

print('FIM')
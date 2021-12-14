'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.                                                                 A) Quantas pessoas foram cadastradas.                                                             B) Uma listagem com as pessoas mais pesadas.                                                                 C) Uma listagem com as pessoas mais leves.'''

temp = []
princ = []
mai = men = 0
while True:
    nome = str(input('Nome: ')).strip().upper()
    peso = float(input('Peso: '))
    resp = str(input('Quer Continuar [S/N]: ')).strip().upper()[0]
    temp.append(nome)
    temp.append(peso)
    
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1]>mai:
            mai = temp[1]
        if temp[1]<men:
            men = temp[1]

    princ.append(temp[:])
    temp.clear()

    while resp not in 'SN':
        resp = str(input('Opção Invalida, Quer Continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print('='*60)
print(f'Os Dados da Lista Principal {princ}')
print()
print(f'Voce Cadastrou {len(princ)} Pessoas')
print()
print(f'O Maior Peso foi {mai}Kg ', end='')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]} de ', end='')
print()
print(f'O Menor Peso foi {men}Kg ', end='')
for p in princ:
    if p[1] == men:
        print(f'{p[0]} de ', end='')
print()
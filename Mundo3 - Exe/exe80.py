'''Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''
lis = []
for i in range(0,5):
    num = ((int(input(f'Digite {i+1}ª Numero: '))))
    if i == 0 or num > lis[-1]:
        print('Adicionado no Final da Lista..')
        lis.append(num)
    else:
        pos = 0
        while pos < len(lis):
            if num <= lis[pos]:
                lis.insert(pos,num)
                print(f'Adicionado a Posição {pos}...')
                break
            pos +=1

print(lis)
print('FIM')
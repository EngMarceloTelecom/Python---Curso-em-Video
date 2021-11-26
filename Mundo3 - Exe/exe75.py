'''Desenvolva um programa que leia quatro valores 
pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares'''

num = (int(input('Digite 1ª Numero: ')),int(input('Digite 2ª Numero: ')),
int(input('Digite 3ª Numero: ')), int(input('Digite 4ª Numero: ')),
int(input('Digite 5ª Numero: ')))

print(num)

print(f'O Valor 9 apareceu {num.count(9)} Vezes')
if 3 in num:
    print(f'O Valor 3 apareceu na {num.index(3)+1}ª Posição')
else:
    print('O Valor 3 não apareceu em nenhuma Posição')
print(f'Os Valores Pares são ', end='')
for i in num:
    if i % 2 == 0:
        print(f' {i}', end='')



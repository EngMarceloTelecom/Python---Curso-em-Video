a = int(input('Digite o Primeiro Valor: '))
b = int(input('Digite o Segundo Valor: '))
c = int(input('Digite o Terceiro Valor: '))

if a<b and a<c:
    menor = a
    print('O Menor Valor é o Primeiro = {}'.format(menor)) 
if b<a and b<c:
    menor = b
    print('O Menor Valor é o Segundo = {}'.format(menor))
if c<a and c<b:
    menor = c
    print('O Menor Valor é o Terceiro = {}'.format(menor)) 

if a>b and a>c:
    maior = a
    print('O Maior Valor é o Primeiro = {}'.format(maior))
if b>a and b>c:
    maior = b
    print('O Maior Valor é o Segundo = {}'.format(maior))
if c>a and c>b:
    maior = c
    print('O Maior Valor é Terceiro = {}'.format(maior))

if a == b:
    print('O Primeiro e o Segundo são Iguais = {}'.format(a))
    if a == c:
        print('O Primeiro e o Terceiro são Iguais = {}'.format(a))
    if b == c:
        print('O Segundo e o Terceiro são Iguais = {}'.format(b))
    if a == b and a == c and b == c:
        print('Todos os Numeros são Iguais = {}'.format(a))
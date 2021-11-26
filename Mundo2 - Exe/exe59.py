''' Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

import time
n1 = float(input('Primeiro Numero: '))
n2 = float(input('Segundo Numero: '))
opção = 0
print('='*30)
while opção !=5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa''')
    print('='*30)
    opção = int(input("Qual Sua Escolha? "))
    if opção ==1:
        print('{} + {} = {}'.format(n1,n2,(n1+n2)))
    elif opção ==2:
        print('{} x {} = {}'.format(n1,n2,(n1*n2)))
    elif opção ==3:
        if n1 > n2:
            print('{} é Maior que {}'.format(n1,n2))
        elif n1 == n2 and n2 == n1:
            print('{} é Igual {}'.format(n1,n2))
        else:
            print('{} é Menor que {}'.format(n1,n2))
    elif opção == 4:
        print('Informe os Numeros Novamente: ')
        n1 = float(input('Primeiro Numero: '))
        n2 = float(input('Segundo Numero: '))
    elif opção ==5:
        print('Fim do Programa')
    else:
        ('Opção Invalida Tente Novamente')
    print('='*30)
    time.sleep(2)
print('Volte Sempre')




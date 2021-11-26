import random
import time
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = random.randint(0, 2)

print('''Sua Opção:
[0] PREDRA
[1] PAPEL
[2] TESOURA''')
op = int(input('Escolha Sua Opção: '))

print('JO')
time.sleep(1)
print('KEM')
time.sleep(1)
print('PO!!!!')
time.sleep(1)

print('-='*15)
print('O Jogador escolheu {}'.format(itens[op]))
print('O Computador escolheu {}'.format(itens[computador]))
print('-='*15)

if op == 0:
    if computador == 0:
        print('EMPATE')
    elif computador == 1:
        print('COMPUTADOR GANHOU')
    elif computador == 2:
        print('JOGADOR GANHOU')
elif op == 1:
    if computador == 0:
        print('JOGADOR GANHOU')
    elif computador == 1:
        print('EMPATE')
    elif computador == 2:
        print('COMPUTADOR GANHOU')
elif op == 2:
    if computador == 0:
        print('COMPUTADOR GANHOU')
    elif computador == 1:
        print('JOGADOR GANHOU')
    elif computador == 2:
        print('EMPATE')
else:
    print('Opção Invalida, Tente Novamente')
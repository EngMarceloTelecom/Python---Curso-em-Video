import random
import time

while True:
    tipo = ' '
    tipo = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    while tipo not in 'PI':
        print('Opção Invalida')
        tipo = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    jogador = int(input('Digite o Valor: '))
    '''while jogador int():
        print('Opção Invalida')
        jogador = int(input('Digite o Valor: '))'''
    comp = random.randint(0,10)
    total = jogador + comp
            
    print('PORCESSANDO.....')
    time.sleep(1)
    print('='*40)
    
    print(f'Voce Jogou {jogador} e o Computador Jogou {comp}, a Soma é {total}')
        
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce Venceu')
        else:
            print('Voce Perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce Venceu')
        else:
            print('Voce Perdeu')
            break
    print('Quero Revanche, Vamos Jogar Novamente?')
    
print("HaHaHa...Game Over..Voce Perdeu")
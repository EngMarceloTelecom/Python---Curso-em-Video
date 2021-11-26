'''Crie um programa que tenha uma dupla totalmente preenchida
com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
cont = ('zero','um','dois','tres','quatro'
,'cinco','seis','sete','oito','nove','dez',
'onze','doze','treze','quatorse','quinze',
'disesses', 'desesete','desoito','desenove','vinte')

while True:
    n = int(input('Digite um Numero [0-20]: '))
    if 0 <= n <=20:

        res = ' '
        while res not in 'SN':
            res = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if res == 'N':
            break

    
print(f'O numero que Voce Digitou foi {cont[n]}')

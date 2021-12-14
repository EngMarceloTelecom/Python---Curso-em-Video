'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
import random
import time

lista = []
jogos = [lista]
tot = 1
qg = int(input('Quantos Jogos vc quer fazer: '))
while tot <= qg:
    while True:
        num = random.randint(1,60)
        if num not in lista:
            cont = 0
            lista.append(num)
            cont += 1
        if cont >=6:
            break
    lista.sort()
    
    tot +=1
    print(f'Os Numeros Sortiados foram {jogos}')
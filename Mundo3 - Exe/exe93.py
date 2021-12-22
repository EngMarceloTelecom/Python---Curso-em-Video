'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

jogador = {}
gols = []
nome = str(input('Nome: '))
partidas = int(input('Quantas Partidas Jogadas: '))
jogador['Jogador'] = nome
jogador['Partidas'] = partidas
for i in range(1, partidas+1):
    gol = int(input(f'  Quantos Gols na Partida {i}: '))
    gols.append(gol)
jogador['Gols'] = gols[:]
jogador['Total de Gols'] = sum(gols)
print('='*50)
print(jogador)
print('='*50)
for k,v in jogador.items():
    print(f'{k} {v}')
print('='*50)
for i, v in enumerate(gols):
    print(f'Na partida {i+1} o Jogador {nome} fez {v} Gols')
print('FIM\n')
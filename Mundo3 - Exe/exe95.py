'''Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

jogador = {}
gols = []
time = []
while True:
    nome = str(input('Nome do Jogador: '))
    partidas = int(input('Quantas Partidas Jogadas: '))
    jogador['Jogador'] = nome
    jogador['Partidas'] = partidas
    for i in range(1, partidas+1):
        gol = int(input(f'  Quantos Gols na Partida {i}: '))
        gols.append(gol)
    jogador['Gols'] = gols[:]
    #gols.clear()
    jogador['Total de Gols'] = sum(gols)
    time.append(jogador.copy())
    #time.clear()
    resp = str(input('Quer Continua [S/N]: ')).upper()[0].strip()
    while resp not in 'NS':
        resp = str(input('Erro!!! Responta S ou N: ')).upper()[0].strip()
    if resp == 'N':
        break

print('='*50)
print(time)
print('='*50)

'''for k,v in jogador.items():
    print(f'{k} {v}')
print('='*50)
for i, v in enumerate(gols):
    print(f'Na partida {i+1} o Jogador {nome} fez {v} Gols')
print('FIM\n')'''
'''Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''

jogador = {}
gols = []
time = []
while True:
    jogador.clear()
    nome = str(input('Nome do Jogador: ')).upper()
    partidas = int(input('Quantas Partidas Jogadas: '))
    jogador['Jogador'] = nome
    jogador['Partidas'] = partidas
    gols.clear()
    for i in range(1, partidas+1):
        gol = int(input(f'  Quantos Gols na Partida {i}: '))
        gols.append(gol)
    jogador['Gols'] = gols[:]
    jogador['T. Gols'] = sum(gols)
    time.append(jogador.copy())
    resp = str(input('Quer Continua [S/N]: ')).upper()[0].strip()
    while resp not in 'NS':
        resp = str(input('Erro!!! Responta S ou N: ')).upper()[0].strip()
    if resp == 'N':
        break
print('='*60)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('='*60)
while True:
    busca = int(input('Mostrar dados de qual Jogador [cod], (99 para sair): '))
    if busca == 99:
        break
    if busca >= len(time):
        print(f' ERRO.. Não Existe Jogador com esse cod {busca}')
    else:
        print('='*60)
        print(f'Levantamento do {time[busca]["Jogador"]}')
        for i, g in enumerate(time[busca]["Gols"]):
            print(f'No jogo {i+1} fez {g} gols')
    print('='*60)
print('=== FIM ===')


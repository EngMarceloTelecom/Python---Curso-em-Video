'''Aprimore o desafio anterior, mostrando 
A) A soma de todos os valores pares digitados.                                              B) A soma dos valores da terceira coluna.                                                 C) O maior valor da segunda linha.'''

matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite Um Valor da {l,c}: '))
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]

for l in range(0,3):
    scol += matriz[l][2]


print('='*30)
print(matriz[0])
print(matriz[1])
print(matriz[2])
print('='*30)
print(f'A Soma dos Valores Pares {spar}')
print(f'A Soma dos valores da 3º Coluna {scol}')
print(f'O Maior Valor da 2º Coluna {max(matriz[1])}')
print('='*30)
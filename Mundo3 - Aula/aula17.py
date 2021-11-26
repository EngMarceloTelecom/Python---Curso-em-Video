lis = [1,3,4,5,8,9]  # lista em []
print(lis)

lis[1] = 2  #trocar o numero 1 da lista pelo 2
print(lis)

lis.append(2) #adicionar o valor 7 ao final lista
print(lis)

lis.sort() #em oredem crescenti 
print(lis)

lis.sort(reverse=True) #em oredem descrecenti 
print(lis)

lis.insert(2,0) #adiciona o valor 0 na posição 2
print(lis)

lis.pop() #elimina o Ultimo da lista
print(lis)

lis.pop(2) #elimina o elemento da posição 2
print(lis)

lis.remove(2) #encontra e remove o primeiro elemento 2 da lista 
print(lis)

if 3 in lis:
    lis.remove(3) #encontra e remove o primeiro elemento 2 da lista 
else:
    print('Não Achei o Numero 3 Para Remover')


valores = []
valores.append(5)
valores.append(7)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na Posição {c} Encontrei o Valor {v}')

print(f'Quantidade de Elementos da Lista é {len(lis)}')

a = [2, 3, 4, 7]
b = a # 'b' esta ligado a 'a' Ligação
print(a, b)
b = a [:] # 'b' esta fazendo uma copia do 'a'
b[2] = 8
print(a, b)


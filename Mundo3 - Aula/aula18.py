
'''Lista dentro de Lista'''

pessoas = [['Pedro', 25],['Maria', 19]]
pessoas.append(['Gustavo', 15])

galera = pessoas[:]  #copia da Lista
galera.append(['Marcelo', 30])


print(pessoas)
print(galera)
print()
print(len(pessoas))
print()
print(pessoas[1][1])
print()

for i in galera:
    print(i[0]) 

print('FIM')
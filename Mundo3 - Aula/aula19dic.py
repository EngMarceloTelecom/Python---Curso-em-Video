dados = {'Nome':'Marcelo','idade': 25, 'Sexo':'M'}

print(dados['Nome'])
print(dados['idade'])
print(f'O {dados["Nome"]} tem {dados["idade"]} anos ')

print(dados.keys())     #mostra os indicis da lista
print(dados.values())   #mostra os valores dos indicis da lista
print(dados.items())    #mostra os 2 valores e indicis da lista
dados['Peso'] = 70
for k in dados.keys():
    print(k)

for k in dados.values():
    print(k)

for k, v in dados.items():
    print(f'{k} = {v}')
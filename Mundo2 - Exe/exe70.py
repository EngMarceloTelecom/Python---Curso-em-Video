print('-'*20)
print('  Lojão Do Marcelo')
print('-'*20)
cont = soma = tot100 = menor = 0
barato =' '
while True:
    Nome = str(input('Nome do Produto: ')).strip().upper()[0]
    preço = float(input('Preço R$: '))
    cont +=1
    soma+= preço
    if cont == 1 or preço < menor:
        menor = preço
        barato = Nome
    if preço > 1000:
        tot100 +=1
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break
print(f'Total de Itens da sua lista é {cont}, Valor Total da Compra é R$ {soma:.2f} ')
print(f'Temos {tot100} produtos acime de R$ 1000')
print(f'Produto Mais é {barato} no Valor de {menor}')
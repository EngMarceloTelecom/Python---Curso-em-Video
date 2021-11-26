tot18 = toth = totf  = 0
while True:
    idade = int(input('Idade: '))
    
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if idade >= 18:
            tot18 +=1
        if sexo == 'M':
            toth +=1
        if sexo == 'F' and idade <= 20:
            totf +=1
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break
print(f'Total de Pessoas com Mais de 18 Anos {tot18}')
print(f'Total de Homens com Mais de 18 Anos {toth}')
print(f'Total de Mulheres Menores de 20 Anos {totf}')
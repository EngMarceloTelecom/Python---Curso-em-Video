from datetime import date
aa = date.today().year

ano = int (input('Qaul ano de Nascimento: '))
dif = aa - ano

print('Sua idade é {} anos'.format(dif))
if dif <= 9:
    print('Sua Categoria é MIRIM')
elif dif <= 14:
    print('Sua Categoria é INFANTIL')
elif dif <= 19:
    print('Sua Categoria é JUNIOR')
elif dif <= 25:
    print('Sua Categoria é SÊNIOR')
elif dif > 25:
    print('Sua Categoria é MASTER')
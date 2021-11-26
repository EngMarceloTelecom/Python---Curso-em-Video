import datetime
atual = datetime.date.today().year
somai = 0
maioridadeh = 0
hmv = ''
somam = 0
for i in range(1,5):
    print('{}ª Pessoa'.format(i))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    print('='*20)
    if i == 1 and sexo in 'Mn':
        maioridadeh = idade
        hmv = nome
    if sexo in 'Mn' and idade > maioridadeh:
        maioridadeh = idade
        hmv = nome
    if sexo in 'Fm' and idade < 20:
        somam +=1
    somai += idade
    mi = somai/4
print('Media da idade {}'.format(mi))
print('O homen mais velho tem {}, e se chama {}'.format(maioridadeh, hmv))
print('São {} Mulheres com MENOS de 20 ANOS'.format(somam))
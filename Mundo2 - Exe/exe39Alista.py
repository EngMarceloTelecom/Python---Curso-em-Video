from datetime import date
atual = date.today().year
sexo = str(input('Sexo [M] ou [F]: '))
nascimento = int(input('Ano de Nascimento: '))
diferen = atual - nascimento

print('Quem Nasceu em {}'.format(nascimento))

if diferen == 18 and sexo == 'M':
    print('Pode ir se Alista Imediatamente voce tem {} seu ano de Alistamento é {}'.format(diferen,(atual)))
elif diferen < 18 and sexo == 'M':
    saldo = 18 - diferen
    print('Voce ainda não tem 18, Vc tem {} anos, falta {} ano para se Alista, Vc se Alista no Ano de {}'.format(diferen,saldo, (atual + saldo)))
elif diferen > 18 and sexo == 'M':
    saldo = diferen - 18
    print('Voce tem {}, vc ja deveria ter se alistado a {} anos atras, no Ano de {}'.format(diferen,saldo,(atual - saldo)))
elif sexo == 'F':
    print('Mulheres Não são obrigadas a se Alistarem')
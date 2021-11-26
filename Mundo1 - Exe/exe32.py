import datetime
ano = int(input('Digite o Ano: '))
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('O Ano {} é Boxesto'.format(ano))
if ano == 0:
    print('O Ano Atual {}'.format(datetime.date.today().year))
else:
    print('O Ano {} não é Bixesto'.format(ano))
    

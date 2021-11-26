print('='*40)
print('   OS 10 PRIMEIROS TERMOS DE UMA PA')
print('='*40)

pt = int(input('Primeiro Termo: '))
r = int(input('Razão: '))

for i in range(pt, ((11-1)*r), r):
    print('{}'.format(i), end =' -> ')
print('ACABOU')

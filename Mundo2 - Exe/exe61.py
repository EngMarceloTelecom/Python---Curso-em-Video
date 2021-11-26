
print('='*40)
print('   OS 10 PRIMEIROS TERMOS DE UMA PA')
print('='*40)

pt = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
termo = pt
cont = 1
while cont <= 10:
    print('{}'.format(termo), end =' -> ')
    termo += r
    cont +=1
print('ACABOU {}'.format(cont))
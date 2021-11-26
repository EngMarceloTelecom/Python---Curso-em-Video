print('='*40)
print('   OS 10 PRIMEIROS TERMOS DE UMA PA')
print('='*40)

pt = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
termo = pt
cont = 1
total = 0
mt = 10
while mt != 0:
    total = total + mt
    while cont <= total:
        print('{}'.format(termo), end =' -> ')
        termo += r
        cont +=1
    print('PAUSA', end =' ')    
    mt = int(input('\nQuantos termos mais vc quer ver? '))
print('ACABOU {}'.format(cont))
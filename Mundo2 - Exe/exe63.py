print('='*20)
print(' Sequencia Fibonate')
print('='*20)

qt = int(input('Quantos Termos: '))
t1 = 0
t2 = 1
cont = 3
qtm = qt
print(f'{t1} -> {t2} ->', end=' ')
while qtm !=0:
    qt = qt + qtm
    while cont <=qt:
        t3 = t1 + t2
        print(f'{t3} -> Mais ?', end=' ')
        t1 = t2
        t2 = t3
        cont +=1
    qtm = int(input('\nQuantos Termos Mais: '))
print(f'FIM {cont}')
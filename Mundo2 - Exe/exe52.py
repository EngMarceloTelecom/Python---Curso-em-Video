n = int(input('Digite um Numero: '))
tot = 0
for i in range(1,n+1):
    if n % i == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(i),end =' ')
print('\n\033[mO Numero {} foi Divisivel {} vezes'.format(n, tot))
if tot == 2:
    print('Por isso ele é PRIMO')
else:
    print('Esse numero NÃO É PRIMO')

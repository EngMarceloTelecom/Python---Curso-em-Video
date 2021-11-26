'''Faça um programa que leia um número qualquer 
e mostre o seu fatorial.'''
'''
ultimo = 1
n1 = int(input('Digite o Numero para o Fatorial: '))
cont = n1
while ultimo > 0:
    cont -=1
    print('{} x {} = {}'.format(n1,cont,n1*cont))'''

n1 = int(input('Digite o Numero para o Fatorial: '))
count = n1
fato = 1
for i in range(1,n1+1):
    fato *=i
    count -=0
    print('{} x {}'.format(count,i), end=' - ')
print('= {}'.format(fato))
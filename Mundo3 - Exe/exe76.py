Lista = ('Caderno','15.5',
'Caneta','2','Mochila', '120.5',)
print('='*40)
for i in range(0,len(Lista)):
    """print(Lista[i])"""
    if i % 2 == 0:
        print(f'{Lista[i]:.<30}',end=' ')
    else:
        print('R$ {:.2f}'.format(float(Lista[i])))
print('='*40)



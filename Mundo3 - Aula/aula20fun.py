def linha():
    print('='*30) 
linha()
print('Marcelo') 
linha()

def titulo(txt):
    print(txt)
    print('='*30)
#nome = str(input(''))
titulo(nome)

linha()
def soma(a, b):
    s = a + b
    print(s)
soma(2,4)

linha()
def contador(*num): #
    soma = sum(num)
    print(f'{soma}',end=' ')
contador(2,3,4,5)
contador(2,1)
contador(2,3,1)

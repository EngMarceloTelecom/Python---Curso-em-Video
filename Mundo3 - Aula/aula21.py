# interect help

'''print(help())
help(print)
print(input.__doc__)
'''
#docstrings
def contador (i,f,p):
    """

    """
#PARAMETROS OPCIONAL 
def soma (a=0,b=0,c=0):
    s = a+b+c
    print(f'A soma vale {s}')

soma(3,5,4)
soma(3,2)
#Escopo de Variavel
# variavel local e variavel global
def teste(b):
    global a # a global
    a = 8 # a local 
    b +=4
    print(a)
    print(b)
a = 5 # a global
teste(a)

#retorno de valores 

def soma (a=0,b=0,c=0):
    s = a+b+c
    return s

r1 = soma(3,5,4)
r2 = soma(3,2)
r3 = soma(1)
print(f'os resultados {r1} {r2} {r3}')


def fatorial(num=1):
    f = 1
    for c in range(num,0 , -1):
        f *=c
    return f

n = int(input('Digite um Numero: '))
print(f'Fatorial de {n} é {fatorial(n)}')
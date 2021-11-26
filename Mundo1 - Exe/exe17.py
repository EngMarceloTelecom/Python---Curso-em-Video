
import math

co = float(input("Digite o Valor do Cateto Oposto: "))
ca = float(input("Digite o Valor do Cateto Adjacente: "))
#hi = (co**2+ca**2)**(1/2)
hi = math.hypot(co, ca)
print('Cateto Oposto {}\nCateto Adjacente {}\nHipotenusa {}'.format(co,ca,hi))

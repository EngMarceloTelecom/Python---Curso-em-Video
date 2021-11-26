import math

ang = float(input('Digite o Angulo: '))
sen = math.sin (math.radians(ang))
cos = math.cos (math.radians(ang))
tan = math.tan (math.radians(ang))
print('Seu Seno é {:.2f}\nSeu Cosseno {:.2f}\nSua Tangente {:.2f}'.format(sen,cos,tan))

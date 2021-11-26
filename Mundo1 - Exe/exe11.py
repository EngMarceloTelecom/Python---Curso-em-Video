lar = float(input('Largura da Parede(m): '))
alt = float(input('Altura da Parede(m): '))
are = lar*alt
tin = are/2
print (' Suas Dimenções é {}m x {}m \n Aréa {:.3} m2 \n Quantidade de Tinta para Pintala é {:.3} L'.format(lar, alt, are, tin))

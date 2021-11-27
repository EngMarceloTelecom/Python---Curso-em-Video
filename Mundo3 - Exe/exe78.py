num = []
for i in range(0,5):
    num.append(int(input(f'Digite o {i}ª Numero: ')))

print(num)

print(max(num))

print(min(num))

print(f'O menor Numero é {min(num)} na Posição {enumerate(num)}')
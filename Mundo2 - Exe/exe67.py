while True:
    print ('*' * 14)
    n = int(input('Digite um Numero: '))
    if n < 0:
        break
    for m in range(1,11):
        print('{} x {} = {}'.format(n, m, m*n))
print('FIM')
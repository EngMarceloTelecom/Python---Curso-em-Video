import os
ip = input('Entre com IP: ')
os.system('ping {} -t'.format(ip))

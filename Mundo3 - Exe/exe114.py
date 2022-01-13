import urllib3
import urllib3.request

try:
    site = urllib3.request.urlopen('https://www.youtube.com/')
except:
    print('Erro no Site')
else:
    print('Site OK')
time = ('Atlético-MG','Flamengo','Palmeiras','Corinthians',
'Fortaleza','Bragantino','Fluminense','Internacional',
'Ceará','América-MG','Cuiabá','Santos','Athletico-PR',
'São Paulo','Atlético-GO','Juventude','Bahia','Grêmio',
'Sport','Chapecoense')

#22/11/21 - 13:00

#for i in time:
#    print(i)

print("="*60)
print(time[:5])

print("="*60)
print(time[-4:])

print("="*60)
print(sorted(time))

print("="*60)
print(f'Chapecoense esta na {time.index("Chapecoense")+1}ª posição')

print("="*60)
print("FIM")
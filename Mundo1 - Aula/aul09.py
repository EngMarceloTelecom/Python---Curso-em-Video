#Cadeia de Caracterios
#Cadeia de Texto
#Strig
frase ='Curso em Video Python'

print ('Fatiamento# '*5)

print (frase[9])
print (frase[9:13])
print (frase[9:14])
print (frase[9:21])
print (frase[9:21:2])
print (frase[:5])
print (frase[15:])
print (frase[9::3])

print ('Analisar# '*5)

print (len(frase)) #quantidade de frese
print (frase.count('o')) #contar o determinada letra e/ou espaço
print (frase.count('o',0,13))
print (frase.find('deo')) #buscar a posição onde nome ou letra começa
print (frase.find('Androide'))
print ('curso' in frase)

print ('Tranformação# '*5)

print (frase.replace('Python','Androide')) #Troca
print (frase.upper()) #Maiuscula
print (frase.lower()) #Minuscula
print (frase.capitalize()) #Somente a Primeira Maiuscula da Frase
print (frase.title()) #A Primeira Maiuscula de casa Parte

frase2 ='   Aprenda Python  '

print (frase2.strip()) #remove os espaços das pontas
print (frase2.rstrip()) #remove os espaços da direita
print (frase2.lstrip()) #remove os espaços da esquerda

dividido = frase.split()
print (frase.split()) #Separa a Frase em lista sem o espaço
print (dividido [3]) #Separa a Frase em lista sem o espaço Renumerando

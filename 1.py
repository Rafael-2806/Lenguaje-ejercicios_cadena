
frase_1= 'Hola-Rafa'
frase_2= ' ¿como-estas?'

#concatenar dos frases
frase= frase_1+frase_2
print(frase)


#separar por palabras
print(frase.split(' '))

#Bucle que acceda a cada palabra
for i in frase:
    print(i)
    
#Comprobar si tenemos palabras o numeros
print(frase.isdigit())

#contar numero palabras 
print(count(frase))
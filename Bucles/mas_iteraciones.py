frutas = ["banana", "manzana","ciruela","pera","naranja","granada","durazno"]
cadena = 'Hola Tomas'
numeros = [2,5,8,10]
for fruta in frutas:
    if fruta == "granada":
        continue #Saltea cuando el bucle llega a ese elemento
    print(f'Me voy a comer una: {fruta}')

#Evitar que el bucle siga ejecutandose
frutas = ["banana", "manzana","ciruela","pera","naranja","granada","durazno"]
for fruta in frutas:
   print(f'Me voy a comer una: {fruta}')
   if fruta == "pera":
       break

#Iterar una cadena de texto
for letra in cadena:
    print(letra)

#For en una sola linea de codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)

#Forma original
numeros_duplicados = list()
for num in numeros:
    numeros_duplicados.append(num*2)
print(numeros_duplicados)

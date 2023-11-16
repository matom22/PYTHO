
animales = ["gato","perro","loro","cocodrilo"]
numeros = [10,62,12,72]

for animal in animales:
    print (f'Ahora la variable animal es igual a : {animal}')

for num in numeros:
    resultado=num*10
    print(resultado)

#Iterar 2 listas al mismo tiempo del mismo tamaño
for num,animal in zip(animales,numeros):
    print(f"Recorriendo lista 1: {num}")
    print(f"Recorriendo lista 2: {animal}")

#Iterar funcion range (no funciona en conjuntos)
for num in range(len(numeros)):
    print(numeros[num])

#Forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor =num[1]
    print(f'El indice es {indice} y el valor es: {valor} ')

#usando el else
for numero in numeros:
    print("Ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("El bucle termino")
    

                
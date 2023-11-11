#Listas (Se pueden modificar)
lista = ["Tomas Rossa", "25", True, 1.85]
print(lista[1])

#Tupla (lo mismo que las listas pero en parentesis)
tupla = ["Tomas Rossa", "25", True, 1.85]
print(tupla[1]) #Las tuplas no se pueden modificar

#Creando un conjunto (set), no podemos modificar elementos.
conjunto = {"Tomas Rossa", "25", True, 1.85}

 #Creando un diccionario (dict), (la estructura es key : value y separamos con comas)
diccionario = {
    'nombre' : 'Tomas Rossa',
    'edad' : 18,
    'altura' : 1.84,
    'dato_duplicado': 'Tomas Rossa'
}

print(diccionario['nombre'])
print(diccionario['edad'])
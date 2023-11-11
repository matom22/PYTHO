# Keys() -> Devuelve las claves
# Get() -> Devuelve el valor de una clave
# Clear() -> Elimina todos los elementos
# Pop() -> Elimina un elemento
# Items() -> Para iterar el diccionario

diccionario = {
    "nombre" : "tomas",
    "apellido" : "rossa",
    "edad" : 25
}

claves = diccionario.keys()

claves = diccionario.get("apellido")

#Eliminando todo el diccionario
#diccionario.clear()

#Eliminando un elemento del diccionario
diccionario.pop("nombre")
print(diccionario)

#Obteniendo un elemento dict_items iterable
diccionario.items()
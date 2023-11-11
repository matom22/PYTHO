#Creando una lista con list
lista = list(["Hola", "Bievenido", "Chau"])
print(lista)

#Devuelve la cantidad de elementos
cadena = "Hola"
resultado = len(cadena)
print(resultado)

#Agrega elemento a la lista
lista.append("xd")
print(lista)

#Agregando elemento lista en un indice especifico
lista.insert(2,"Toma mama")
print(lista)

#Agregar varios elementos a la lista
lista.extend([False,2030])
print(lista)

#Elimina elemento de la lista
lista.pop(2)
print(lista)

#Elimina el ultimo elemento de la lista
lista.pop(-1) #-1 para el ultimo, -2 anteultimo, etc
print(lista)

#Remueve elemento de la lista por su valor
lista.remove("xd")
print(lista)

#Elimina todos los elementos de la lista
lista.clear()

#Ordena a los elementos de manera ascendente
lista.sort()
print(lista)

#Ordena los elementos al reves
lista.sort(reverse = True)

#Invierte los elementos de la lista
lista.reverse()


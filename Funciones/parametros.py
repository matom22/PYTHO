#Forma no optima de sumar valores
def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados

resultado = suma([5,3,9,10,20,3])

print(resultado)

#Forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])
resultado2 = suma_total ([5,3,9,10,20,3])
print(resultado2)



#Forma optima de sumar valores, utilizando parametro args (*args)
def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus numeros es:  {sum(numeros)}"
   
resultado = suma("Tomas",4,5,6,7,9)
print(resultado)


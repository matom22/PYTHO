#Creando una funcion que nos devuelva los numeros primos
#Entre 0 y el argumento que pasamos

#Crear funcion que verifique sea primo
def es_primo(num):
    #Verificamos que el numero pasado no pueda dividirse
    #Por ningun numetro entre 2 y ese mismo numero -1
    for i in range(2,num-1):
        #Si es divisible por alguno retornamos False y termina el bucle
        if num%i==0: return False
        #Si termina el bucle, significa que no fue divisible entonces es primo
    return True

#Creando una funcion que retorne una lista con todos los primos
def primos_hasta(num):
    #Creamos la lista
    primos = []
    for i in range(3,num+1):
        #Verificamos si el valor es primo
        resultado = es_primo(i)
        #En caso que lo sea lo agregamos a la lista
        if resultado == True: primos.append(i)
        #Devolvemos la lista
    return primos

#Creamos el resultado llamando a la funcion y lo mostramos
resultado = primos_hasta(13)
print(resultado)


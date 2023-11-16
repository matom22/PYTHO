#Crear funcion simple
def saludar():
    print("Hola tomas como andas")

#Ejecutando la funcion
saludar()

#Crar una funcion que tenga un parametro
def saludo(nombre,sexo):
    sexo =sexo.lower()
    if sexo == "mujer":
        adjetivo = "reina"
    elif sexo == "hombre":
        adjetivo = "titan"
    else:
        adjetivo = "amor"

    print(f'Hola {nombre},mi {adjetivo} como estas?')

saludo('Tomas',"hombre")

#Crear una funcion que nos retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num -2
    c2 = num 
    c3 = num  -5
    contraseña = f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}'
    return contraseña,num #Guarda el dato pero no lo muestra

#Desempaquetando la funcion
password,primer_numero = crear_contraseña_random(981)
#Mostrano los resultados obtenidos y los datos utilizados para obtenerlo
print(f'Tu contraseña nueva es: {password}')
print(f'El numero utilizado fue: {primer_numero}')


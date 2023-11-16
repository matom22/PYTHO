diccionario = {
    "nombre" : "tomas",
    "apellido" :"rossa",
    "edad" : "25"
}

#Recorriendo diccionario con items para obtener la clave
for key in diccionario:
    key
    print(f'La clave es {key}')


#Recorriendo diccionario con items para obtener la clave y valor
for datos in diccionario.items():
    key = datos[0]
    value = datos [1]
    print(f'La clave es {key} y el valor es : {value}')


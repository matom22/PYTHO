cadena1 = "Hola soy Tomas"
cadena2 = "Bienvenido"

#Funcion para devolver la lista de atributos
resultado = dir(cadena1) #Devuelve la lista de atributos validos del objeto

#Metodos que convierten valor
resultado = cadena1.upper() #Convierte el texto en mayuscula
resultado = cadena1.lower() #Convierte el texto a minuscula
resultado = cadena1.capitalize() #Convierte la primer letra en mayuscula

#Metodos que buscan un valor
resultado = cadena1.find("T") #Busca una cadena en otra cadena, si no hay condiciones devuelve -1
resultado = cadena1.index("T") #Busca una cadena en otra cadena, si no encuentra nada lanza error

#Metodos que consultan si son numericos o alfanumericos
resultado = cadena1.isnumeric() #Si es numerico da True, sino False
resultado = cadena1.isalpha() #Si es alfa da True, sino False (Solo valido de la A-Z, el espacio no es alfanumerico)

#Metodos que muestran cuantas veces encuentra coincidencias
resultado = cadena1.count("a")
resultado = len(cadena1) #Funcion

#Metodo que verifican si una cadena empieza con otra cadena dada, si es asi devuelve True
resultado = cadena1.startswith("H")

#Metodo que verifican si una cadena termina con otra cadena dada, si es asi devuelve True
resultado = cadena1.endswith("s")

#Metodo que reemplaza un pedazo de la cadena dada por otra dada
resultado = cadena1.replace("Hola", "Holu Maquina")

#Metodo que devuelve una matriz, separa una cadena con la cadena que le pasemos
resultado = cadena1.split(" ")



print(resultado)
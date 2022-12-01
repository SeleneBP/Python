#Nombre: Selene Bejarano Prieto
#Fecha: 30/11/2022
#Descripción: Proyecto. Problema 2.

#Imports/variables
from datetime import datetime #Importa la fecha y la hora
import random #Importa una librería que depende de lo que ponga letra o número lo pone aleatorio
import string #Importa cadenas
import os #Importa comando del sistema
#Inicializando la lista
cadenaconcovid=str("ccucggcgggca") #Creamos una variable que dentro haya una cadena con la cadena covid
codigo=input("Cúal es su código de paciente: ") #Preguntamos el codigo de paciente y la guardamos en codigo
cadena=string.ascii_lowercase #Creamos una variable y dentro de esa varible tendra una cadena en minusculas


#Bloque

os.system ("clear")
for i in range(50): #Crea un rango hasta el 50 de letras en minúsculas
    cadena_aleatoria = random.choice(cadena) #Creamos una variable que contenga la cadena letras aleatorias
    cadena_final=print(cadena_aleatoria,end="") #Creamos una variable que imprima la cadena aleatoria sin salto de línea
    #si no saldría así: 
    #a
    #b
    #c
    
    adn_generado = "".join(cadenaconcovid) #Generamos el adn y vemos si la cadena covid está dentro



if cadenaconcovid in adn_generado: #Si la cadena covid esta dentro de el adn generado entonces el resultado será negativo o positivo.
    resultado = "Negativo: No se encuentra restos de la variante COVID." 
else:
    resultado = "Positivo: Sí se encuentra restos de la variante COVID."


print("____")

print("INFORME DE VIRUS COVID")
print("Fecha:",datetime.today().strftime('%Y-%m-%d'))
print("Hora:",datetime.today().strftime('%H:%M') )
print("Código de paciente: ",codigo)
print("Resultado:", resultado) #Imprimimos el resultado dado

#Creamos una tupla 
datos = (datetime.today().strftime('%Y-%m-%d %H:%M'),codigo, resultado )
lista = list(datos)
file = open("virus.txt", "a")
file.write('virus = %s' % lista + '\n' )
file.close()

#Nombre: Selene Bejarano Prieto
#Fecha: 30/11/2022
#Descripción: Proyecto. Problema 2.

#Imports/variables
from datetime import datetime
import random
import string
import os
#Inicializando la lista
cadenaconcovid=str("ccucggcgggca")
codigo=input("Cúal es su código de paciente: ")
cadena=string.ascii_lowercase


#Bloque

os.system ("clear")
for i in range(50):
    cadena_aleatoria = random.choice(cadena)
    cadena_final=print(cadena_aleatoria,end="")
    
    adn_generado = "".join(cadenaconcovid)



if cadenaconcovid in adn_generado:
    resultado = "Negativo: No se encuentra restos de la variante COVID."
else:
    resultado = "Positivo: Sí se encuentra restos de la variante COVID."


print("____")

print("INFORME DE VIRUS COVID")
print("Fecha:",datetime.today().strftime('%Y-%m-%d'))
print("Hora:",datetime.today().strftime('%H:%M') )
print("Código de paciente: ",codigo)
print("Resultado:", resultado)

datos = (datetime.today().strftime('%Y-%m-%d %H:%M'),codigo, resultado )
lista = list(datos)
file = open("virus.txt", "a")
file.write('virus = %s' % lista + '\n' )
file.close()

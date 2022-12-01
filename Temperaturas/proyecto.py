#Nombre: Selene Bejarano Prieto
#Fecha: 30/11/2022
#Descripción: Proyecto. Problema 1.

#Imports/variables
from datetime import datetime
#Inicializando la lista
temperaturas=[]

import os
#Bloque
os.system ("clear")
print ("Di cuales son las temperturas máximas y mínimas del Parque Natural del Doñana")
while True:	
    temp_maxi =float(input("Dime la temperatura max: ")) 
    if temp_maxi == 100: 
        break
     
    temp_mini =float(input("Dime la temperatura min: ")) 
    if temp_mini == 100:   
        break
    muestra = []
    muestra.append(temp_maxi)
    muestra.append(temp_mini)
    temperaturas.append(muestra)


maxi = []
mini = []

for muestra in temperaturas:
    maxi.append(muestra[0])
    mini.append(muestra[1])
    

sumas = sum(mini) + sum(maxi)
media = sumas / len(temperaturas * 2)




#Informe
os.system ("clear")
print("________________________________________________________")
print("INFORME DE TEMPERATURAS DEL PARQUE NATURAL DE DOÑANA")
print("Fecha:",datetime.today().strftime('%Y-%m-%d'))
print("Hora:",datetime.today().strftime('%H:%M') )
print("Número de muestras: ", len(temperaturas))
print("Temperaturas tomadas: ", temperaturas)
print("Temperaturas máxima: ", max(maxi))
print("Temperaturas mínimas: ", min(mini))
print("Temperatura media: ", media )

datos = (datetime.today().strftime('%Y-%m-%d %H:%M'),temperaturas, max(maxi),min(mini),media )
lista = list(datos)
file = open("temperaturas.txt", "a")
file.write('temperaturas = %s' % lista + '\n' )
file.close()

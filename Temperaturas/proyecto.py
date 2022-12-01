#Nombre: Selene Bejarano Prieto
#Fecha: 01/12/2022
#Descripción: Proyecto. Problema 1.

#Imports/variables
from datetime import datetime #Importamos la fecha y la hora
#Inicializando la lista
temperaturas=[] #Inicializamos la lista temperaturas
import os #Importamos una librería para utilizar los comandos del sistema

#Bloque
os.system ("clear") #Limpiamos la pantalla
print ("Di cuales son las temperturas máximas y mínimas del Parque Natural del Doñana") #Imprimimos en pantalla 
while True:	#Inicializamos un bucle
    temp_maxi =float(input("Dime la temperatura max: ")) #Guardamos en una variable la temperatura máxima
    if temp_maxi == 100: #Si es igual que 100 cerramos el bucle
        break
     
    temp_mini =float(input("Dime la temperatura min: ")) #Guardamos en una variable la temperatura mínima
    if temp_mini == 100:   
        break
    muestra = [] #Inicializamos una lista
    muestra.append(temp_maxi)
    muestra.append(temp_mini)
    temperaturas.append(muestra) #Lee la lista muestra


maxi = [] #Inicializamos dos listas
mini = []

for muestra in temperaturas: #Crea un bucle que recoge las temperaturas guardadas y las mete en una lista
    maxi.append(muestra[0])
    mini.append(muestra[1])
    

sumas = sum(mini) + sum(maxi) #Se suma las temperaturas máximas y mínimas
media = sumas / len(temperaturas * 2) #Hace la media recogiendo las sumas y diviendolo por todas las temperaturas que se multiplican * 2 por la máxima y la mínima




#Informe
os.system ("clear")
print("________________________________________________________")
print("INFORME DE TEMPERATURAS DEL PARQUE NATURAL DE DOÑANA")
print("Fecha:",datetime.today().strftime('%Y-%m-%d')) #Pone la fecha
print("Hora:",datetime.today().strftime('%H:%M') ) #Pone la hora
print("Número de muestras: ", len(temperaturas)) 
print("Temperaturas tomadas: ", temperaturas) #Recoge todas las temperaturas
print("Temperaturas máxima: ", max(maxi)) #Recoge solo la máxima
print("Temperaturas mínimas: ", min(mini)) #Recoge solo la mínima
print("Temperatura media: ", media ) #Recoge la media

#Creamos una tupla
datos = (datetime.today().strftime('%Y-%m-%d %H:%M'),temperaturas, max(maxi),min(mini),media ) #Recoge en una variable todas las temperaturas más las fechas
lista = list(datos) #Creas una lista que lista los datos 
file = open("temperaturas.txt", "a") #Abre el archivo y mete los datos anterior sin machacar nada de lo que haya dentro
file.write('temperaturas = %s' % lista + '\n' ) #Escribe dentro del fichero
file.close() #Cierra la tupla

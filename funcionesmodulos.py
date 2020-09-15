# Escribe un programa en Python que dada una criptomoneda, 
# la cantidad acumulada y su correspondiente cotización por dólar del día, 
# le permita al usuario conocer la fecha completa y hora del momento 
# en que obtuvo el sistema esa información.
from datetime import datetime
criptomoneda = input("Introduzca el nombre de la criptomoneda ")
cantidad = float(input("Introduzca la cantidad de la criptomoneda "))
conversion = float(input("Introduzca la tasa de conversion a USD$ "))

totalUSD = cantidad * conversion
dt = datetime.now()


print("Usted posee un total de US$ " + str(totalUSD))
print("Informacion obtenida el " + dt.strftime("%A %d/%m/%Y %H:%M:%S"))
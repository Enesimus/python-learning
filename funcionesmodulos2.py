# Escribe un programa en Python que dada una criptomoneda, 
# la cantidad acumulada y su correspondiente cotización por dólar del día, 
# le permita al usuario conocer la fecha completa y hora del momento 
# en que obtuvo el sistema esa información, así como el monto en US$ 
# que tiene el usuario en su billetera digital. 
# Considerando un crecimiento del 5% por día, muéstrale al usuario 
# para ese mismo día de la siguiente semana cuál sería su ganancia en US$.

from datetime import datetime
criptomoneda = input("Introduzca el nombre de la criptomoneda ")
cantidad = float(input("Introduzca la cantidad de la criptomoneda "))
conversion = float(input("Introduzca la tasa de conversion a USD$ "))

totalUSD = cantidad * conversion
dt = datetime.now()
ganancia = totalUSD * (5/100) *7 
total_final = totalUSD + ganancia


print("Usted posee un total de US$ " + str(totalUSD))
print("Informacion obtenida el " + dt.strftime("%A %d de %B de %Y a las %I:%M:%S %p"))
print("La próxima semana su total sería US$" + str(total_final))

# Escribe un programa en Python que le permita al usuario 
#conocer el monto en dólares americanos que tiene acumulado 
#en su wallet o billetera digital correspondiente a una 
#criptomoneda particular. En tal sentido, el programa debe 
#leer el nombre de la criptomoneda, la cantidad acumulada 
#de esa criptomoneda y su cotización por US$ del momento. 
#Luego, debe calcular el monto total en US$ que posee el 
#usuario e imprimir el siguiente mensaje: “Ud. posee un total de US$” 
#seguido del cálculo realizado.

# Recomendaciones:

# Asigna a las variables nombres nemotécnicos; 
#es decir; que describan su contenido
# En Python no hay declaración de variables, 
#se crean asignando el valor deseado

criptomoneda = input("Introduzca el nombre de la criptomoneda ")
cantidad = float(input("Introduzca la cantidad de la criptomoneda "))
conversion = float(input("Introduzca la tasa de conversion a USD$ "))

totalUSD = cantidad * conversion

print("Usted posee un total de US$ " + str(totalUSD))



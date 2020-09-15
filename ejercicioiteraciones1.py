#Ejercicio Iteraciones 1
# Escribe un programa en Python que dados el nombre de una criptomoneda y su monto 
# inicial para un usuario, genere un porcentaje aleatorio entre 0 y 3%, además 
# puede ser de alza o baja, asociado a esa criptomoneda e imprima el porcentaje 
# diario durante una semana, si es alza o baja, el saldo diario de la billetera 
# digital del usuario y el total acumulado en esa semana.

import random
moneda = input("Ingrese el nombre de la moneda: ")
cantidad = float(input("Ingrese la cantidad de "+moneda+": "))
cantidad1 = cantidad
for i in range(1,8):
	variable = random.uniform(-0.03,0.03)
	print("El día",str(i),"la variación fue de un %6.2f"%(variable*100)+"%")
	cantidad2 = cantidad1 + (cantidad1 * variable)
	print("Su saldo el dia",str(i),"es de %6.2f"%cantidad2,moneda,".")
	cantidad1= cantidad2

ganancia = cantidad2 - cantidad
print("Al terminar la semana, su ganancia acumulada será de: %6.2f"%ganancia,moneda,".")


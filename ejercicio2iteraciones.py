#Escribe un programa en Python que solicite el ingreso de tres criptomonedas, las 
#cantidades y cotizaciones en Dólares Americanos (USD) de cada una de éstas, 
#validando que las tres criptomonedas pertenezcan a las siguientes (BTC, BCC, LTC,
#ETH, ETC y XRP), y que las cantidades y cotizaciones sean números reales. Por 
#último el programa debe indicar la cantidad de USD que el usuario tiene acumulado.

monedas = ["BTC", "BCC", "LTC", "ETH", "XRP"]

# m1 = input("Ingrese la primera moneda: ")
# m2 = input("Ingrese la segunda moneda: ")
# m3 = input("Ingrese la tercera moneda: ")
# c1 = float(input("Ingrese la cantidad de " + m1 + ": "))
# c2 = float(input("Ingrese la cantidad de " + m2 + ": "))
# c3 = float(input("Ingrese la cantidad de " + m3 + ": "))
# t1 = float(input("Ingrese la conversion a USD de " + m1 + ": "))
# t2 = float(input("Ingrese la conversion a USD de " + m2 + ": "))
# t3 = float(input("Ingrese la conversion a USD de " + m3 + ": "))
count = 0
total = 0
while count < 3:
	m1 = input("Ingrese la primera moneda: ")
	if m1 in monedas:
		c1 = float(input("Ingrese la cantidad de " + m1 + ": "))
		t1 = float(input("Ingrese la conversion a USD de " + m1 + ": "))
		if type(c1)!=float or type(t1)!=float:
			print("Error: El valor ingresado no es válido")
			break
		total = total + c1 * t1
	else:
		print("Error: no ha ingresado una moneda válida")
		break
	count = count+1

print("El monto total es de: %6.2f"%total,"USD")
# Escribe un programa en Python que dada una criptomoneda y 
# un monto en esa criptomoneda, permita incrementar el saldo 
# de tu teléfono móvil. Considera que los pagos pueden ser 
# realizados mediante bitcoin (BTC), dash (DASH) o litecoin (LTC).

moneda = input("Ingrese el tipo de criptomoneda (BTC, DASH o LTC): ")
if moneda == "BTC" or moneda == "DASH" or moneda == "LTC":
	cantidad = float(input("Ingrese la cantidad de " + moneda +":"))
	if moneda == "BTC":
		saldo = cantidad * 10
	elif moneda == "DASH":
		saldo = cantidad *8
	elif moneda == "LTC":
		saldo = cantidad *2
else:
	print("Moneda no permitida, ingrese BTC, DASH o LTC")

print("Su nuevo saldo es: " + str(saldo) + " " + moneda+".")

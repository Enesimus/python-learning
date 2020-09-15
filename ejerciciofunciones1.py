# Ahora, te motivamos a escribir un programa en Python que solicite el ingreso de 
# tres criptomonedas, las cantidades y cotizaciones en Dólares Americanos (USD) 
# de cada una de éstas; además, debes validar que las tres criptomonedas 
# pertenezcan a las siguientes (BTC, BCC, LTC, ETH, ETC y XRP), y que las 
# cantidades y cotizaciones sean números reales. Por último, el programa debe 
# indicar la cantidad de USD que el usuario tiene acumulada.

# Te recomendamos hacer uso de funciones para realizar las validaciones.
criptos = ["BTC", "BCC", "LTC", "ETH", "ETC", "XRP"]
orden = ["primera", "segunda", "tercera"]
def conversion(a,b):
	return a*b

def valcripto(a,b):
	if a in b:
		return a
	else:
		print("Error: %s no es una criptomoneda válida"%a)
                

def valnum(a):
	if type(a)==float:
		return a
	else:
		print("Error: no ha ingresado un valor adecuado")

i=0
c=0
cripto1=""
cripto, cant,tasa = None, None, None
while i < len(orden):
                while cripto1!=cripto:
                        cripto=input("Ingrese el nombre de la "+str(orden[i])+" moneda: ")
                        cripto1=valcripto(cripto,criptos)
                while type(cant) != float:
                        cant = (input("Ingrese la cantidad de " + cripto + ": "))
                        cant = valnum(float(cant))
                while type(tasa) != float:
                        tasa = (input("Ingrese la tasa de conversion a USD de "+ cripto + ": "))
                        tasa = valnum(float(tasa))
                c=c + conversion(cant,tasa)
                i+=1

print("El valor total es %6.2f USD"%c)

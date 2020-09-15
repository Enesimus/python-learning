#En esta oportunidad, te solicitamos que escribas 
#un programa en Python que lea el nombre de tres criptomonedas 
#y el monto que posee el usuario de cada una de éstas; 
#luego las muestre ordenadas de forma descendente cada nombre 
#con su respectivo monto. ¡Éxito!

cripto1nom = input("Ingrese el nombre de su moneda: ")
cripto1cant = float(input("Ingrese la cantidad de la moneda: "))
cripto2nom = input("Ingrese el nombre de su moneda: ")
cripto2cant = float(input("Ingrese la cantidad de la moneda: "))
cripto3nom = input("Ingrese el nombre de su moneda: ")
cripto3cant = float(input("Ingrese la cantidad de la moneda: "))

if cripto1cant > cripto2cant:
	if cripto2cant > cripto3cant:
		print("Ud. Posee : \n" + str(cripto1cant) + " " + cripto1nom + "\n" + str(cripto2cant) + " " + cripto2nom +"\n"+ str(cripto3cant) + " " + cripto3nom)
	else:	
		print("Ud. Posee : \n" + str(cripto1cant) + " " + cripto1nom + "\n" + str(cripto3cant) + " " + cripto3nom +"\n"+str(cripto2cant) + " " + cripto2nom)
elif cripto2cant > cripto3cant:
	if cripto3cant > cripto1cant:
				print("Ud. Posee : \n" + str(cripto2cant) + " " + cripto2nom + "\n" + str(cripto3cant) + " " + cripto3nom +"\n"+str(cripto1cant) + " " + cripto1nom)
	else:
				print("Ud. Posee : \n" + str(cripto2cant) + " " + cripto2nom + "\n" + str(cripto1cant) + " " + cripto1nom +"\n"+str(cripto3cant) + " " + cripto3nom)
else:
	if cripto2cant > cripto1cant:
				print("Ud. Posee : \n" + str(cripto3cant) + " " + cripto3nom + "\n" + str(cripto2cant) + " " + cripto2nom +"\n"+str(cripto1cant) + " " + cripto1nom)
	else: 
			print("Ud. Posee : \n" + str(cripto3cant) + " " + cripto3nom + "\n" + str(cripto1cant) + " " + cripto1nom +"\n"+str(cripto2cant) + " " + cripto2nom)

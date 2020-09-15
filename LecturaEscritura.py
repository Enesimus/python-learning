# Ejercicio Lectura y escritura

# Te proponemos escribir un programa en Python que nos permita calcular 
# la ganancia de una criptomoneda (Nombre y Cantidad), 
# si ésta se negocia por una cantidad de días indicada por el usuario 
# y a una ganancia fija indicada también por el usuario. 
# Al terminar, el programa debe indicar la ganancia en cantidad de criptomoneda, 
# la cantidad de días negociados y el monto total al finalizar los días.

# Recomendaciones:

# Asigna a las variables nombres nemotécnicos; es decir; 
# que describan su contenido
# En Python no hay declaración de variables, se crean asignando 
# el valor deseado
# Hacer las lecturas y escrituras correspondientes.

criptomoneda_nombre = input("Ingrese el nombre de la criptomoneda ")
criptomoneda_cantidad = float(input("Ingrese la cantidad de la criptomoneda "))
ganancia_diaria = float(input("Ingrese la ganancia diaria "))
numero_dias = int(input("Ingrese el número de días "))

ganancia_final = (ganancia_diaria*numero_dias)
monto_final = criptomoneda_cantidad + ganancia_final

print("La ganancia es " + str(ganancia_final) + " " + criptomoneda_nombre + ". "+"Se negoció durante " + str(numero_dias)+" días."+" El monto total al terminar el periodo es " + str(monto_final) + " " + criptomoneda_nombre +".")




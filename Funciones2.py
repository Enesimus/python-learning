# Escribe un programa que solicite el ingreso del nombre de una criptomoneda,
# validando que sea una de las siguientes (BTC,BCC,LTC,ETH,ETC y XRP), y que
# indique el precio actual de la misma obteniendo su valor de Binance en USDT.
# Para obtener el precio de la criptomoneda en USDT puedes hacer uso de la API
# Rest de Binance; además puedes hacer uso de la API price ticker, la que se
# invoca en el navegador a través del URL:
# https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT.

# Asimismo, utiliza el módulo requests, para lo cual debes importarlo
# primero a la máquina usando pip3 install requests o pip install requests
# desde la consola de comando o terminal de tu sistema operativo.

# Con la finalidad de invocar la API, puedes hacer uso de la función get
# de requests. Por ejemplo: requests.get(url).


import requests
dirfinal = "https://api.binance.com"
def binanceticker(api):
    return dirfinal+api

def obtprecio(cripto):
    return requests.get(binanceticker("/api/v3/ticker/price?symbol="+cripto))

def valida_cripto(a):
    criptos = ["BTC","BCC","LTC","ETH","ETC","XRP"]
    if a in criptos:
        return True
    else:
        print("Error: La moneda ingresada no es válida")
        return False
    
cripto = input("Ingrese el valor de la moneda: ")
# cant = ""
while not valida_cripto(cripto):
    cripto = input("Ingrese el nombre de la moneda: ")
    cripto = str.upper(cripto)
# while valida_cant(cant) == False:
#    cant = float(input("ingrese la cantidad de " + cripto + ": ")
    

data = obtprecio(cripto+"USDT").json()
print("El precio de", cripto, "es", data["price"])

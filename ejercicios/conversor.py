pesos = float(input("ingrese la cantidad de pesos: "))

tasa_cambio = float(input("ingrese la tasa de cambio actual: "))

dolares = pesos / tasa_cambio

dolares_mostrados = int(dolares * 100) / 100

print("con", pesos,"pesos colombianos puede obtener un total de ", dolares_mostrados, "dolares")
menu = {
    "arroz con pollo": 5000,
    "chontaduro": 7000,
    "pecao": 12000,
    "empanadas": 1200,
    "hamburguesas": 15000,
}
print("== MENU DEL DIA MI NIÑO ==")
for plato, precio in menu.items():
    print( plato, "-$", precio )

total = 0 

while True:
    pedido = input("escribe el plato que quieres: ").lower()
    if pedido == "salir":
        break
    elif pedido in menu:
        total = total + menu[pedido]
        print(pedido, "agregado. total a pagar es :", total)
    else:
        print("ese plato no esta en el menu mi niño, pide otro")

    print("monto total es", total)
    print("GRACIAS MI NIÑO")

meta = float(input("Ingrese su meta de ahorro: "))
total = 0
meses = 0
while total < meta:
    aporte = float(input(f"Ingrese el ahorro del mes {meses+1}: "))
    total += aporte
    meses += 1
print(f"¡Meta alcanzada en {meses} meses! Total ahorrado: {total}")
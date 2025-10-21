# Diccionario para guardar estudiantes y sus notas
estudiantes = {}

while True:
    nombre = input("Nombre del estudiante ('fin' para terminar): ")
    if nombre == 'fin':
        break
    
    notas = []
    print(f"Ingrese las notas de {nombre} (escriba 'listo' cuando termine):")
    while True:
        nota = input("Nota: ")
        if nota == 'listo':
            break
        notas.append(float(nota))
    
    estudiantes[nombre] = notas

print("\nPromedios:")
for nombre, notas in estudiantes.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.1f}")

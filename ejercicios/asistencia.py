estudiantes = []
while True: 
    nombre = input("ingrese el nombre del estudiante: ")
    if nombre.lower() == "salir":
        print("esos fueron los estudiantes que asistieron el dia de hoy", estudiantes )
        break
    estudiantes.append(nombre)
    print("estudiante registrado:", estudiantes)
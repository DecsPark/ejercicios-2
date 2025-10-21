"""Formulario que solicite nombre, edad y correo"""

import re

def validar_nombre(nombre):

    #verificar que la variable nombre no esta vacia
    return nombre.replace(" ", "").isalpha()

#funcion que valida la edad
def validar_edad(edad_val):
    try:
        edad = int(edad_val) # convertir a entera
        return 14 <= edad <= 100
    except ValueError:
        return False

def validar_correo(correo):
    patron = r"^[\w\.-]+@[\w\.-]+\w+$"
    return re.match(patron, correo) is not None

while True:
    nombre = input("ingrese su nombre:").strip()
    if not validar_nombre(nombre):
        print("nombre invalido coloquelo otra vez")
        continue

    edad = input("ingrese su edad:").strip()
    if not validar_edad(edad):
        print("edad invalida coloquelo otra vez")
        continue

    correo = input("ingrese su correo:").strip()
    if not validar_correo(correo):
        print("correo invalido coloquelo otra vez")
        continue 
    #Mostrar inofrmacion si pasa las validaciones
    print(f"registro exitoso: nombre {nombre}, edad: {edad}, correo; {correo}")
    break
   

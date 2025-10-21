#validar el ingreso de un numero entero del 1 al 10
while True:
    entrada = input("Digite un numero del 1 al 10: ")
    #Validacion de los datos ingresados
    try: 
        num = int(entrada) #convertir a entero
        if 1 <= num <=10:
            print(f"el {num} es numero valido")
            break
        else:
            print("el numero ingresado no esta en el rango permitido")
    except ValueError:
        print("el dato ingresado no es un numero valido")

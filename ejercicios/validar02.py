""""Validar el ingresp de categorias: a, b, y c"""

while True:
    categoria = input("ingresa una categoria (a, b, c): ").lower()
    if categoria in ["a", "b", "c"]:
        print(f"haz seleccionado la categoria: {categoria}")
        break
    else:
        print("la categoria ingresada no es valida")
        
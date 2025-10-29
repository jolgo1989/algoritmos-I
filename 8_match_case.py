# fruta = "manzana"

# match fruta:

#     case "manzana":
#         print("Es una manzana")
#     case "pera":
#         print("Es una pera")
#     case _:
#         print("Fruta desconocida")

# Ejercicio: realiza un programa que lea un color y devuelva su nombre en inglés
# color = input("Ingresa un color: ")
# match color:
#     case "rojo":
#         print("Red")
#     case "verde":
#         print("Green")
#     case "azul":
#         print("Blue")
#     case _:
#         print("Color desconocido")

# Ejercicio: realiza un programa que lea dos numero y realice la operación elegida

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

operacion = input(
    "Elige la operación (suma, resta, multiplicacion, division): ")

match operacion:
    case "suma":
        result = num1 + num2
        print(result)
    case "resta":
        result = num1 - num2
        print(result)
    case "multiplicacion":
        result = num1 * num2
        print(result)
    case "division":
        result = num1 / num2
        print(result)
    case _:
        print("Operación no válida")

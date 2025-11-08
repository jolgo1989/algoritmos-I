# ¿por que utilizar funciones?
# Las funciones permiten organizar el código en bloques reutilizables, mejorando la legibilidad y facilitando el mantenimiento. Además, ayudan a evitar la repetición de código y permiten abstraer tareas complejas en unidades manejables.

# Ejemplo: Mostrar un mensaje que se repita 3 veces en la página con el siguiente texto:

# print('Cuidado')
# print('Ingrese su documento correctamente')

# print('Cuidado')
# print('Ingrese su documento correctamente')

# print('Cuidado')
# print('Ingrese su documento correctamente')

# ? Usando una función para evitar la repetición de código

# def mostrar_mensaje():
#     print('Cuidado')
#     print('Ingrese su documento correctamente')


# mostrar_mensaje()
# mostrar_mensaje()
# mostrar_mensaje()

# ? Ejercicio: Crear una función que calcule el área de un rectángulo dado su base y altura, y luego utilizar esa función para calcular el área de varios rectángulos con diferentes dimensiones.


# def calcular_area_rectangulo(base, altura):
#     area = base * altura
#     return area


# Calcular el área de varios rectángulos
# area1 = calcular_area_rectangulo(5, 10)
# area2 = calcular_area_rectangulo(3, 7)
# area3 = calcular_area_rectangulo(8, 4)

# La palabra clave return sirve para que una función devuelva un valor al lugar desde donde fue llamada.
# Es decir, permite que el resultado de un cálculo u operación dentro de la función pueda ser usado en otra parte del programa.

# Ejemplo de uso de return

# area1 = calcular_area_rectangulo(5, 10)
# print("El área del rectángulo 1 es:", area1)

# operacion = area1 + 20
# print("El resultado de la operación es:", operacion)

def sumar(a, b):
    return (a + b)


print(sumar(3, 4)*3)
# print(sumar(3, 4)*4)

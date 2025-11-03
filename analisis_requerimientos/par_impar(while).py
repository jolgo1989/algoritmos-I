# Analisis
# Un profesor desea que sus estudiantes desarrollen un programa que permita al usuario ingresar varios números enteros y determinar si cada uno es par o impar. El proceso se repetirá en un ciclo while hasta que el usuario escriba un valor especial (por ejemplo, 0) para salir del programa.

# Requerimientos funcionales
# El programa debe mostrar un mensaje inicial explicando que el usuario puede salir ingresando 0.
# Debe solicitar un número entero.
# Si el número es distinto de 0, debe verificar si es par o impar e imprimir el resultado.
# Si el número es 0, el programa debe terminar.
# El ciclo debe repetirse indefinidamente hasta que se cumpla la condición de salida.

# Codigo

while True:
    n = int(input("Ingrese un número entero (0 para salir): "))

    if n == 0:
        print("Programa finalizado.")
        break

    if n % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")

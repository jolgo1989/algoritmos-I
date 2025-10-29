# Estructura repetitiva while
# x = 1
# while x <= 100:
#     print(x)
#     x = x+1

# Ejercicio: realiza un programa que lea un número y muestre los números del 1 al número ingresado
# valor_final = int(input("Ingrese el valor final:"))

# while x <= valor_final:
#     print(x)
#     x = x+1

# Acumulador
# Analisis del problema
# Problema redactado
# Un profesor desea que sus estudiantes desarrollen un programa que permita ingresar 5 números enteros por teclado y que, al finalizar, muestre en pantalla la suma total de esos valores. El programa debe solicitar los números uno por uno, acumularlos en una variable y, al terminar, imprimir el resultado final.
x = 1
suma = 0
while x <= 5:
    valor = int(input("Ingrese un valor: "))
    suma = suma + valor
    x = x + 1
print(suma)

# valor : tiene por objetivo cargar valores por teclado.
# x : nos sirva para contar cuantas veces se ha repetido el while, sabemos que debemos cortar cuando x toma el valor 6.
# suma : almacena la suma de valores ingresados hasta ese momento en la variable valor.

# Análisis
# Un profesor desea que sus estudiantes desarrollen un programa que permita ingresar un número entero y que, al finalizar, muestre en pantalla la tabla de multiplicar de ese número desde el 1 hasta el 10. El programa debe usar un ciclo while para generar los resultados.

# El programa debe solicitar al usuario un número entero.
# Debe inicializar un contador en 1.
# Mientras el contador sea menor o igual a 10:
# Multiplicar el número ingresado por el contador.
# Mostrar el resultado en pantalla.
# Incrementar el contador en 1.
# Al finalizar, debe mostrar la tabla completa del número ingresado.

# codigo
# Programa que imprime la tabla de multiplicar de un número del 1 al 10

# n = int(input("Ingrese un número: "))
# i = 1

# while i <= 10:
#     resultado = n * i
#     print(f"{n} x {i} = {resultado}")
#     i = i + 1

# Analisis
# Un profesor desea que sus estudiantes desarrollen un programa que permita al usuario ingresar varios números enteros y determinar si cada uno es par o impar. El proceso se repetirá en un ciclo while hasta que el usuario escriba un valor especial (por ejemplo, 0) para salir del programa.

# Requerimientos funcionales
# El programa debe mostrar un mensaje inicial explicando que el usuario puede salir ingresando 0.

# Debe solicitar un número entero.

# Si el número es distinto de 0, debe verificar si es par o impar e imprimir el resultado.

# Si el número es 0, el programa debe terminar.

# El ciclo debe repetirse indefinidamente hasta que se cumpla la condición de salida.

# Codigo
# Programa que determina si un número es par o impar usando ciclo while
# El programa termina cuando el usuario ingresa 0

while True:
    n = int(input("Ingrese un número entero (0 para salir): "))

    if n == 0:
        print("Programa finalizado.")
        break

    if n % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")

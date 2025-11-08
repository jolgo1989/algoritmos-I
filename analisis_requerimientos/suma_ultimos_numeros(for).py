# Desarrollar un programa que solicite la carga de 10 números e imprima la suma de lo últimos 5 valores ingresados.

suma = 0  # Acumulador para la suma de los últimos 5 valores
for i in range(10):
    valor = int(input(f"Ingrese el número {i+1}: "))
    if i >= 5:  # Solo sumar los últimos 5 valores
        suma += valor
print("La suma de los últimos 5 valores ingresados es:", suma)

# Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
# a) La cantidad de valores negativos ingresados.
# b) La cantidad de valores positivos ingresados.

cantidad_positivos = 0  # Contador de valores positivos
cantidad_negativos = 0  # Contador de valores
for i in range(10):
    valor = int(input(f"Ingrese el número {i+1}: "))
    if valor >= 0:
        cantidad_positivos += 1
    else:
        cantidad_negativos += 1
print("Cantidad de valores positivos ingresados:", cantidad_positivos)
print("Cantidad de valores negativos ingresados:", cantidad_negativos)

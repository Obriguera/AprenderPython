radio = input("Cargar radio del círculo (Número): ")
if radio.isdigit():
    radio = int(radio)  # Convertir la entrada a un entero
    area = 3.14 * radio**2  # Usar ** para calcular el cuadrado
    print("El área del círculo es:", area)
else:
    print("No se cargó un dato válido.")

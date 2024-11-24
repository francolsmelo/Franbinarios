# binarioshexa.py

from db_connection import get_db_connection
from guardar_datos import guardar_datos

def main():
    try:
        numero = float(input("Ingresa un número entero o real: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return

    opcion = input("Elige el tipo de conversión (binario/hexadecimal): ").strip().lower()

    if opcion == "binario":
        resultado_binario = bin(int(numero))[2:]
        resultado_hexadecimal = hex(int(numero))[2:]
        guardar_datos(numero, resultado_binario, resultado_hexadecimal)
    elif opcion == "hexadecimal":
        resultado_binario = bin(int(numero))[2:]
        resultado_hexadecimal = hex(int(numero))[2:]
        guardar_datos(numero, resultado_binario, resultado_hexadecimal)
    else:
        print("Opción no válida. Por favor, elige 'binario' o 'hexadecimal'.")

if __name__ == "__main__":
    main()
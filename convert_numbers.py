"""
Este módulo convierte números a diferentes tipos a partir de un archivo.
"""

import sys
import time
import argparse


def convert_numbers(file_path):
    """
    Convierte los números en el archivo a binario y hexadecimal.
    Muestra los resultados en la pantalla y guarda en un archivo \
        llamado ConversionResults.txt.
    Maneja errores en caso de datos inválidos en el archivo.
    Muestra el tiempo transcurrido al final de la ejecución.
    """
    def read_numbers_from_file(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as data_file:
                return [line.strip() for line in data_file]
        except FileNotFoundError:
            print(f"Error: Archivo '{file_path}' no encontrado.")
            sys.exit(1)

    def convert_to_binary_and_hex(numbers):
        binary_results = []
        hexadecimal_results = []

        for number in numbers:
            try:
                # Intenta convertir el número a decimal, permitiendo decimales
                decimal_number = float(number)
                # Verifica si el número es un entero antes de convertirlo
                # a binario y hexadecimal
                if decimal_number.is_integer():
                    decimal_number = int(decimal_number)
                else:
                    print(f"""Advertencia: Se ha encontrado un número decimal
                          '{number}'. Se convierte a decimal, pero los
                          resultados en binario y hexadecimal pueden no
                          ser representativos de la precisión
                          completa del número.""")

                # Utiliza format para convertir el número a
                # hexadecimal sin el prefijo '0x'
                hexadecimal_result = format(decimal_number, 'x')
                binary_result = bin(int(decimal_number))[2:]

                binary_results.append(binary_result)
                hexadecimal_results.append(hexadecimal_result)
            except ValueError:
                print(f"Error: Datos inválidos '{number}' \
                      en el archivo. Se omite.")

        return binary_results, hexadecimal_results

    def print_and_save_results(numbers, binary_results,
                               hexadecimal_results, elapsed_time):
        print("Decimal\t\tBinario\t\tHexadecimal")
        print("---------------------------------------")
        for i, number in enumerate(numbers):
            # Verifica si los índices son válidos antes de imprimir
            if i < len(binary_results) and i < len(hexadecimal_results):
                print(f"{number}\t\t{binary_results[i]}\t\t \
                      {hexadecimal_results[i]}")

        with open('ConversionResults.txt', 'w',
                  encoding='utf-8') as results_file:
            results_file.write("Decimal\t\tBinario\t\tHexadecimal\n")
            results_file.write("---------------------------------------\n")
            for i, number in enumerate(numbers):
                # Verifica si los índices son válidos antes de escribir
                if i < len(binary_results) and i < len(hexadecimal_results):
                    results_file.write(f"{number}\t\t{binary_results[i]}\t\t \
                                       {hexadecimal_results[i]}\n")

        print(f"\nTiempo transcurrido: {elapsed_time:.4f} segundos")
        with open('ConversionResults.txt', 'a',
                  encoding='utf-8') as results_file:
            results_file.write(f"\nTiempo transcurrido: \
                               {elapsed_time:.4f} segundos")

    start_time = time.time()
    numbers = read_numbers_from_file(file_path)
    binary_results, hexadecimal_results = convert_to_binary_and_hex(numbers)
    end_time = time.time()
    elapsed_time = end_time - start_time

    print_and_save_results(numbers, binary_results,
                           hexadecimal_results, elapsed_time)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convierte números \
                                     desde un archivo de datos.')
    parser.add_argument('file_path', metavar='file_path', type=str,
                        help='Ruta del archivo')
    args = parser.parse_args()

    convert_numbers(args.file_path)

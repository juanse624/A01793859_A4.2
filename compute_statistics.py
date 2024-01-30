"""
Este módulo realiza cálculos estadísticos a partir de un archivo de datos.
"""

import sys
import time


def read_file(file_path):
    """
    Lee el archivo y devuelve una lista de números en punto flotante.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = [float(line.strip()) for line in file]
        return data
    except (ValueError, FileNotFoundError) as e:
        print(f"Error al leer el archivo: {e}")
        return []


def calculate_mean(data):
    """
    Calcula y devuelve la media de los datos.
    """
    if not data:
        return None
    return sum(data) / len(data)


def calculate_median(data):
    """
    Calcula y devuelve la mediana de los datos.
    """
    if not data:
        return None
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    return (sorted_data[mid] + sorted_data[mid - 1]) / 2 \
        if n % 2 == 0 else sorted_data[mid]


def calculate_mode(data):
    """
    Calcula y devuelve la moda de los datos.
    """
    if not data:
        return None
    counts = {}
    for num in data:
        counts[num] = counts.get(num, 0) + 1
    max_count = max(counts.values())
    mode_values = [k for k, v in counts.items() if v == max_count]
    return mode_values if max_count > 1 else None


def calculate_variance(data, mean):
    """
    Calcula y devuelve la varianza de los datos.
    """
    if not data or mean is None:
        return None
    return sum((x - mean) ** 2 for x in data) / len(data) \
        if len(data) > 1 else 0


def calculate_std_dev(variance):
    """
    Calcula y devuelve la desviación estándar a partir de la varianza.
    """
    if variance is None:
        return None
    return variance ** 0.5


def main():
    """
    Función principal para ejecutar el programa.
    """
    if len(sys.argv) != 2:
        print("Uso: revisar readme")
        sys.exit(1)

    file_path = sys.argv[1]

    start_time = time.time()

    data = read_file(file_path)

    mean = calculate_mean(data)
    median = calculate_median(data)
    mode = calculate_mode(data)
    variance = calculate_variance(data, mean)
    std_dev = calculate_std_dev(variance)

    end_time = time.time()

    # Imprimir resultados en la pantalla
    print(f"Media: {mean}")
    print(f"Mediana: {median}")
    print(f"Moda: {mode if mode is not None else 'No hay moda'}")
    print(f"Varianza: {variance}")
    print(f"Desviación Estándar: {std_dev}")
    print(f"Tiempo transcurrido: {end_time - start_time} segundos")

    # Guardar resultados en un archivo
    with open("ResultadosEstadisticos.txt", 'w',
              encoding='utf-8') as result_file:
        result_file.write(f"Media: {mean}\n")
        result_file.write(f"Mediana: {median}\n")
        result_file.write(f"Moda: {mode if mode is not None else 'No moda'}\n")
        result_file.write(f"Varianza: {variance}\n")
        result_file.write(f"Desviación Estándar: {std_dev}\n")
        result_file.write(f"Tiempo transcurrido: \
                          {end_time - start_time} segundos\n")

    print("Resultados guardados en 'ResultadosEstadisticos.txt'.")


if __name__ == "__main__":
    main()

"""
Este módulo cuenta el numero de veces que se repite
una palabra de un archivo de datos.
"""
import sys
import time


def procesar_linea(linea, frecuencia_palabras):
    """
    Procesa una línea y actualiza el diccionario de frecuencia de palabras.
    """
    palabras = linea.split()
    for palabra in palabras:
        palabra = palabra.lower().strip()
        frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1


def procesar_archivo(ruta_archivo):
    """
    Procesa el archivo especificado y devuelve un diccionario
    con la frecuencia de cada palabra.
    """
    frecuencia_palabras = {}
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                procesar_linea(linea, frecuencia_palabras)

    except FileNotFoundError as e:
        print(f"Error: Archivo '{ruta_archivo}' no encontrado. {e}")
        return None

    except OSError as e:
        print(f"Error procesando el archivo: {e}")
        return None

    return frecuencia_palabras


def imprimir_resultados(frecuencia_palabras):
    """
    Imprime los resultados de la frecuencia de palabras en la consola.
    """
    if frecuencia_palabras is not None:
        for palabra, frecuencia in frecuencia_palabras.items():
            print(f"{palabra}: {frecuencia}")


def guardar_resultados(frecuencia_palabras, tiempo_transcurrido):
    """
    Guarda los resultados en un archivo llamado
    WordCountResults.txt con el tiempo transcurrido.
    """
    with open("WordCountResults.txt", 'w',
              encoding='utf-8') as archivo_resultado:
        for palabra, frecuencia in frecuencia_palabras.items():
            archivo_resultado.write(f"{palabra}: {frecuencia}\n")
        archivo_resultado.write(f"\nTiempo transcurrido: \
                                {tiempo_transcurrido:.6f} segundos")


def main():
    """
    Función principal que se ejecuta al iniciar el programa.
    """
    if len(sys.argv) != 2:
        print("Uso: python word_count.py fileWithData2.txt")
        return

    ruta_archivo = sys.argv[1]

    tiempo_inicio = time.time()

    frecuencia_palabras = procesar_archivo(ruta_archivo)

    tiempo_transcurrido = time.time() - tiempo_inicio

    imprimir_resultados(frecuencia_palabras)
    guardar_resultados(frecuencia_palabras, tiempo_transcurrido)


if __name__ == "__main__":
    main()

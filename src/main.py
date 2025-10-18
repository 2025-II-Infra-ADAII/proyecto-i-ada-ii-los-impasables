import sys
import time
import os
from bruta import roFB
from dinamica import roPD
from voraz import roV
from utils import leer_finca, escribir_salida

def ejecutar_algoritmo(finca, algoritmo: str, archivo_salida: str):
    print(f"\nEjecutando algoritmo {algoritmo}...")

    inicio = time.time()

    if algoritmo == "FB":
        perm, costo = roFB(finca)
    elif algoritmo == "PD":
        perm, costo = roPD(finca)
    elif algoritmo == "V":
        perm, costo = roV(finca)
    else:
        print("Algoritmo no reconocido")
        return None, None, None

    tiempo = time.time() - inicio

    print(f"Tiempo de ejecución: {tiempo:.4f} segundos")
    print(f"Costo mínimo: {costo}")
    print(f"Permutación óptima: {perm}")

    escribir_salida(archivo_salida, costo, perm)

    return tiempo, costo, perm


def main():
    if len(sys.argv) < 4:
        print("Uso: python main.py <archivo_entrada> <algoritmo> <archivo_salida>")
        print("Algoritmos: FB (Fuerza Bruta), PD (Programación Dinámica), V (Voraz)")
        print("\nEjemplos:")
        print("  python main.py data/juguete.txt FB resultados/juguete_fb.txt")
        print("  python main.py data/pequeno.txt PD resultados/pequeno_pd.txt")
        print("  python main.py data/mediano.txt V resultados/mediano_v.txt")
        return

    archivo_entrada = sys.argv[1]
    algoritmo = sys.argv[2].upper()
    archivo_salida = sys.argv[3]

    if algoritmo not in ["FB", "PD", "V"]:
        print("Algoritmo no válido. Use: FB, PD o V")
        return

    if not os.path.exists(archivo_entrada):
        print(f"Error: El archivo {archivo_entrada} no existe")
        print("Primero genera los datos: python generar_datos.py")
        return

    os.makedirs(os.path.dirname(archivo_salida) if os.path.dirname(archivo_salida) else '.', exist_ok=True)

    finca = leer_finca(archivo_entrada)
    if not finca:
        print("Error: No se pudo leer la finca")
        return

    print(f"Finca cargada: {len(finca)} tablones")
    ejecutar_algoritmo(finca, algoritmo, archivo_salida)


if __name__ == "__main__":
    main()
from typing import List, Tuple
import random

Finca = List[Tuple[int, int, int]]


def calcular_tiempos_inicio(finca: Finca, permutacion: List[int]) -> List[int]:
    n = len(finca)
    tiempos_inicio = [0] * n
    tiempo_actual = 0

    for idx in permutacion:
        tiempos_inicio[idx] = tiempo_actual
        tiempo_actual += finca[idx][1]
    return tiempos_inicio


def calcular_costo(finca: Finca, permutacion: List[int]) -> int:
    tiempos_inicio = calcular_tiempos_inicio(finca, permutacion)
    costo_total = 0

    for i, (ts, tr, p) in enumerate(finca):
        tiempo_fin = tiempos_inicio[i] + tr
        tardanza = max(0, tiempo_fin - ts)
        costo_total += p * tardanza
    return costo_total


def generar_finca_aleatoria(n: int, ts_max: int = 20, tr_max: int = 5, p_max: int = 4) -> Finca:
    finca = []
    for _ in range(n):
        ts = random.randint(1, ts_max)
        tr = random.randint(1, tr_max)
        p = random.randint(1, p_max)
        finca.append((ts, tr, p))
    return finca


def guardar_finca(finca: Finca, archivo: str):
    with open(archivo, 'w') as f:
        f.write(f"{len(finca)}\n")
        for ts, tr, p in finca:
            f.write(f"{ts},{tr},{p}\n")


def leer_finca(archivo: str) -> Finca:
    try:
        with open(archivo, 'r') as f:
            lineas = f.readlines()

        n = int(lineas[0].strip())
        finca = []

        for i in range(1, n + 1):
            if i < len(lineas):
                valores = lineas[i].strip().split(',')
                if len(valores) == 3:
                    ts, tr, p = map(int, valores)
                    finca.append((ts, tr, p))

        return finca
    except Exception as e:
        print(f"Error leyendo archivo {archivo}: {e}")
        return []


def escribir_salida(archivo: str, costo: int, permutacion: List[int]):
    try:
        with open(archivo, 'w') as f:
            f.write(f"{costo}\n")
            for idx in permutacion:
                f.write(f"{idx}\n")
        print(f"✓ Resultado guardado en: {archivo}")
    except Exception as e:
        print(f"Error escribiendo archivo {archivo}: {e}")
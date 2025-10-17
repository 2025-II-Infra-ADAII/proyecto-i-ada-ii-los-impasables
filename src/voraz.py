from typing import List, Tuple

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


def roV(finca: Finca):
    n = len(finca)
    if n == 0:
        return [], 0

    claves = []
    for i, (ts, tr, p) in enumerate(finca):
        if ts == 0 or tr == 0:
            clave = float("inf")
        else:
            clave = p / (ts * tr)
        claves.append((i, clave))

    claves.sort(key=lambda x: x[1], reverse=True)
    perm = [i for i, _ in claves]
    costo = calcular_costo(finca, perm)

    return perm, costo


if __name__ == "__main__":
    finca = [(5, 3, 4), (4, 1, 3), (8, 2, 2), (3, 2, 4), (10, 3, 3)]
    perm, costo = roV(finca)
    print("Orden voraz:", perm)
    print("Costo obtenido:", costo)
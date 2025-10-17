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


def generar_permutaciones(arr: List[int], l: int = 0):
    n = len(arr)
    if l == n - 1:
        yield arr.copy()
        return

    for i in range(l, n):
        arr[l], arr[i] = arr[i], arr[l]
        yield from generar_permutaciones(arr, l + 1)
        arr[l], arr[i] = arr[i], arr[l]


def roFB(finca: Finca):
    n = len(finca)
    if n == 0:
        return [], 0

    indices = list(range(n))
    mejor_perm = None
    mejor_costo = float("inf")

    for perm in generar_permutaciones(indices):
        costo = calcular_costo(finca, perm)
        if costo < mejor_costo:
            mejor_costo = costo
            mejor_perm = perm.copy()

    return mejor_perm, mejor_costo


if __name__ == "__main__":
    finca = [(5, 3, 4), (4, 1, 3), (8, 2, 2), (3, 2, 4), (10, 3, 3)]
    perm, costo = roFB(finca)
    print("Mejor orden:", perm)
    print("Costo mínimo:", costo)
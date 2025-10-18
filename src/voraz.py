from src import utils

from typing import List, Tuple

Finca = List[Tuple[int, int, int]]

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
    costo = utils.calcular_costo(finca, perm)

    return perm, costo


if __name__ == "__main__":
    finca = [(5, 3, 4), (4, 1, 3), (8, 2, 2), (3, 2, 4), (10, 3, 3)]
    perm, costo = roV(finca)
    print("Orden voraz:", perm)
    print("Costo obtenido:", costo)
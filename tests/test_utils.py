import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.utils import calcular_costo, generar_finca_aleatoria


class TestUtils:
    def test_calcular_costo(self):
        finca = [(5, 3, 2)]
        perm = [0]
        costo = calcular_costo(finca, perm)
        assert costo == 0

    def test_calcular_costo_con_penalizacion(self):
        finca = [(2, 3, 2)]
        perm = [0]
        costo = calcular_costo(finca, perm)
        assert costo == 2

    def test_generar_finca_aleatoria(self):
        finca = generar_finca_aleatoria(5)
        assert len(finca) == 5
        for ts, tr, p in finca:
            assert 1 <= ts <= 20
            assert 1 <= tr <= 5
            assert 1 <= p <= 4


if __name__ == "__main__":
    test = TestUtils()
    test.test_calcular_costo()
    test.test_calcular_costo_con_penalizacion()
    test.test_generar_finca_aleatoria()
    print("✓ Pruebas utils OK")
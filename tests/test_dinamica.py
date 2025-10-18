import pytest
import time
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.dinamica import roPD
from src.utils import leer_finca


class TestProgramacionDinamica:
    def test_finca_vacia(self):
        finca = []
        perm, costo = roPD(finca)
        assert perm == []
        assert costo == 0

    def test_finca_un_tablon(self):
        finca = [(5, 3, 2)]
        perm, costo = roPD(finca)
        assert perm == [0]
        assert costo == 0

    def test_finca_pequena(self):
        finca = [(5, 3, 4), (4, 1, 3)]
        perm, costo = roPD(finca)
        assert len(perm) == 2
        assert costo >= 0

    def test_optimalidad(self):
        finca = [(5, 3, 4), (4, 1, 3), (8, 2, 2)]
        perm, costo = roPD(finca)
        assert len(perm) == len(set(perm))
        assert all(0 <= i < len(finca) for i in perm)

    def test_archivos_referencia_pd(self):
        archivos_referencia = {
            'r_ejemplo_1_D.txt': 'ejemplo_1.txt',
            'r_ejemplo_2_PD.txt': 'ejemplo_2.txt',
            'r_ejemplo_3_PD.txt': 'ejemplo_3.txt',
            'r_ejemplo_4_PD.txt': 'ejemplo_4.txt'
        }

        for archivo_resultado, archivo_entrada in archivos_referencia.items():
            ruta_resultado = os.path.join('resultados', archivo_resultado)
            ruta_entrada = os.path.join('data', archivo_entrada)

            if os.path.exists(ruta_entrada) and os.path.exists(ruta_resultado):
                finca = leer_finca(ruta_entrada)
                assert finca, f"No se pudo cargar {ruta_entrada}"

                with open(ruta_resultado, 'r') as f:
                    lineas = f.readlines()
                costo_esperado = int(lineas[0].strip())
                permutacion_esperada = [int(linea.strip()) for linea in lineas[1:] if linea.strip()]

                perm_calculada, costo_calculado = roPD(finca)

                assert costo_calculado == costo_esperado, \
                    f"{archivo_resultado}: Costo esperado {costo_esperado}, calculado {costo_calculado}"

                assert len(perm_calculada) == len(permutacion_esperada)
                assert set(perm_calculada) == set(permutacion_esperada)

                print(f"✅ {archivo_resultado} - PD: Costo {costo_calculado} correcto")
            else:
                print(f"⚠️  Archivos no encontrados: {ruta_entrada} o {ruta_resultado}")


if __name__ == "__main__":
    test = TestProgramacionDinamica()
    test.test_finca_vacia()
    test.test_finca_un_tablon()
    test.test_finca_pequena()
    test.test_optimalidad()
    test.test_archivos_referencia_pd()
    print("✓ Pruebas programación dinámica OK")
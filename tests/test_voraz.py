import pytest
import time
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.voraz import roV
from src.utils import generar_finca_aleatoria, leer_finca


class TestVoraz:
    def test_finca_vacia(self):
        finca = []
        perm, costo = roV(finca)
        assert perm == []
        assert costo == 0

    def test_finca_un_tablon(self):
        finca = [(5, 3, 2)]
        perm, costo = roV(finca)
        assert perm == [0]
        assert costo == 0

    def test_estructura_solucion(self):
        finca = [(5, 3, 4), (4, 1, 3), (8, 2, 2)]
        perm, costo = roV(finca)
        assert len(perm) == 3
        assert len(set(perm)) == 3
        assert all(0 <= i < len(finca) for i in perm)
        assert costo >= 0

    def test_archivos_referencia_v(self):
        archivos_referencia = {
            'r_ejemplo_1_V.txt': 'ejemplo_1.txt',
            'r_ejemplo_2_V.txt': 'ejemplo_2.txt',
            'r_ejemplo_3_V.txt': 'ejemplo_3.txt',
            'r_ejemplo_4_V.txt': 'ejemplo_4.txt',
            'r_ejemplo_5_V.txt': 'ejemplo_5.txt'
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

                perm_calculada, costo_calculado = roV(finca)

                assert costo_calculado == costo_esperado, \
                    f"{archivo_resultado}: Costo esperado {costo_esperado}, calculado {costo_calculado}"

                assert len(perm_calculada) == len(permutacion_esperada)
                assert set(perm_calculada) == set(permutacion_esperada)

                print(f"✅ {archivo_resultado} - V: Costo {costo_calculado} correcto")
            else:
                print(f"⚠️  Archivos no encontrados: {ruta_entrada} o {ruta_resultado}")


if __name__ == "__main__":
    test = TestVoraz()
    test.test_finca_vacia()
    test.test_finca_un_tablon()
    test.test_estructura_solucion()
    test.test_archivos_referencia_v()
    print("✓ Pruebas voraz OK")
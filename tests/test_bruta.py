import pytest
import time
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.bruta import roFB
from src.utils import generar_finca_aleatoria, leer_finca


class TestFuerzaBruta:
    def test_finca_vacia(self):
        finca = []
        perm, costo = roFB(finca)
        assert perm == []
        assert costo == 0

    def test_finca_un_tablon(self):
        finca = [(5, 3, 2)]
        perm, costo = roFB(finca)
        assert perm == [0]
        assert costo == 0

    def test_finca_pequena(self):
        finca = [(5, 3, 4), (4, 1, 3)]
        perm, costo = roFB(finca)
        assert len(perm) == 2
        assert costo >= 0

    def test_archivos_referencia_fb(self):
        archivos_referencia = {
            'r_ejemplo_1_FB.txt': 'ejemplo_1.txt',
            'r_ejemplo_6_FB.txt': 'ejemplo_6.txt',
            'r_ejemplo_7_FB.txt': 'ejemplo_7.txt',
            'r_ejemplo_8_FB.txt': 'ejemplo_8.txt',
            'r_ejemplo_9_FB.txt': 'ejemplo_9.txt',

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

                perm_calculada, costo_calculado = roFB(finca)


                assert costo_calculado == costo_esperado, \
                    f"{archivo_resultado}: Costo esperado {costo_esperado}, calculado {costo_calculado}"

                assert perm_calculada == permutacion_esperada, \
                    f"{archivo_resultado}: Permutación diferente\nEsperada: {permutacion_esperada}\nCalculada: {perm_calculada}"

                print(f"✅ {archivo_resultado} - FB: Costo {costo_calculado} correcto")
            else:
                print(f"⚠️  Archivos no encontrados: {ruta_entrada} o {ruta_resultado}")


if __name__ == "__main__":
    test = TestFuerzaBruta()
    test.test_finca_vacia()
    test.test_finca_un_tablon()
    test.test_finca_pequena()
    test.test_archivos_referencia_fb()
    print("✓ Pruebas fuerza bruta OK")
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from tests.test_bruta import TestFuerzaBruta
from tests.test_dinamica import TestProgramacionDinamica
from tests.test_voraz import TestVoraz
from tests.test_utils import TestUtils


def run_all_tests():
    test_classes = [TestFuerzaBruta, TestProgramacionDinamica, TestVoraz, TestUtils]

    for test_class in test_classes:
        print(f"\n{'=' * 50}")
        print(f"Ejecutando {test_class.__name__}")
        print('=' * 50)

        test_instance = test_class()
        test_methods = [method for method in dir(test_instance) if method.startswith('test_')]

        for method_name in test_methods:
            print(f"✓ {method_name}...")
            try:
                getattr(test_instance, method_name)()
                print(f"  ✓ PASÓ")
            except Exception as e:
                print(f"  ✗ FALLÓ: {e}")


if __name__ == "__main__":
    run_all_tests()
    print("\nTodas las pruebas completadas")
import time
import matplotlib.pyplot as plt
import numpy as np
import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.bruta import roFB
from src.dinamica import roPD
from src.voraz import roV
from src.utils import generar_finca_aleatoria


def ejecutar_benchmark():
    tamanos_fb = [5, 7, 10]
    tamanos_pd = [10, 20, 25]
    tamanos_v = [10, 20, 50]

    resultados = {'FB': [], 'PD': [], 'V': []}

    print("=== FUERZA BRUTA ===")
    for n in tamanos_fb:
        finca = generar_finca_aleatoria(n)
        inicio = time.time()
        roFB(finca)
        tiempo = time.time() - inicio
        resultados['FB'].append((n, tiempo))
        print(f"n={n}: {tiempo:.4f}s")

    print("\n=== PROGRAMACIÓN DINÁMICA ===")
    for n in tamanos_pd:
        finca = generar_finca_aleatoria(n)
        inicio = time.time()
        roPD(finca)
        tiempo = time.time() - inicio
        resultados['PD'].append((n, tiempo))
        print(f"n={n}: {tiempo:.4f}s")

    print("\n=== ALGORITMO VORAZ ===")
    for n in tamanos_v:
        finca = generar_finca_aleatoria(n)
        inicio = time.time()
        roV(finca)
        tiempo = time.time() - inicio
        resultados['V'].append((n, tiempo))
        print(f"n={n}: {tiempo:.6f}s")

    return resultados


def graficar_resultados(resultados):
    """Genera gráficas comparativas de los resultados"""

    # Configurar el estilo de las gráficas
    plt.style.use('default')
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))

    # Extraer datos para cada algoritmo
    fb_n = [r[0] for r in resultados['FB']]
    fb_t = [r[1] for r in resultados['FB']]

    pd_n = [r[0] for r in resultados['PD']]
    pd_t = [r[1] for r in resultados['PD']]

    v_n = [r[0] for r in resultados['V']]
    v_t = [r[1] for r in resultados['V']]

    # Gráfica 1: Comparación directa
    ax1.plot(fb_n, fb_t, 'ro-', linewidth=2, markersize=8, label='Fuerza Bruta (FB)')
    ax1.plot(pd_n, pd_t, 'go-', linewidth=2, markersize=8, label='Programación Dinámica (PD)')
    ax1.plot(v_n, v_t, 'bo-', linewidth=2, markersize=8, label='Algoritmo Voraz (V)')
    ax1.set_xlabel('Tamaño (n)')
    ax1.set_ylabel('Tiempo (segundos)')
    ax1.set_title('Comparación de Tiempos de Ejecución')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Gráfica 2: Escala logarítmica en Y
    ax2.plot(fb_n, fb_t, 'ro-', linewidth=2, markersize=8, label='FB')
    ax2.plot(pd_n, pd_t, 'go-', linewidth=2, markersize=8, label='PD')
    ax2.plot(v_n, v_t, 'bo-', linewidth=2, markersize=8, label='V')
    ax2.set_yscale('log')
    ax2.set_xlabel('Tamaño (n)')
    ax2.set_ylabel('Tiempo (segundos) - Escala Log')
    ax2.set_title('Comparación - Escala Logarítmica')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    # Gráfica 3: Gráficas individuales
    if fb_t:
        ax3.plot(fb_n, fb_t, 'ro-', linewidth=2, markersize=6, label='FB', alpha=0.7)
    if pd_t:
        ax3.plot(pd_n, pd_t, 'go-', linewidth=2, markersize=6, label='PD', alpha=0.7)
    if v_t:
        ax3.plot(v_n, v_t, 'bo-', linewidth=2, markersize=6, label='V', alpha=0.7)

    # Agregar anotaciones para los puntos
    for i, (n, t) in enumerate(resultados['FB']):
        ax3.annotate(f'{t:.3f}s', (n, t), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)

    for i, (n, t) in enumerate(resultados['PD']):
        ax3.annotate(f'{t:.3f}s', (n, t), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)

    for i, (n, t) in enumerate(resultados['V']):
        ax3.annotate(f'{t:.6f}s', (n, t), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)

    ax3.set_xlabel('Tamaño (n)')
    ax3.set_ylabel('Tiempo (segundos)')
    ax3.set_title('Tiempos con Anotaciones')
    ax3.legend()
    ax3.grid(True, alpha=0.3)

    plt.tight_layout()

    # Guardar la gráfica
    import os
    os.makedirs('docs/imagenes', exist_ok=True)
    plt.savefig('docs/imagenes/benchmark_comparativo.png', dpi=300, bbox_inches='tight')
    plt.show()

    return fig


def generar_grafica_crecimiento(resultados):
    """Genera gráfica mostrando el crecimiento de cada algoritmo"""
    plt.figure(figsize=(10, 6))

    # Extraer datos
    fb_n = [r[0] for r in resultados['FB']]
    fb_t = [r[1] for r in resultados['FB']]

    pd_n = [r[0] for r in resultados['PD']]
    pd_t = [r[1] for r in resultados['PD']]

    v_n = [r[0] for r in resultados['V']]
    v_t = [r[1] for r in resultados['V']]

    # Calcular factores de crecimiento
    print("\n=== ANÁLISIS DE CRECIMIENTO ===")

    if len(fb_t) > 1:
        print("Fuerza Bruta (FB):")
        for i in range(1, len(fb_t)):
            crecimiento = fb_t[i] / fb_t[i - 1] if fb_t[i - 1] > 0 else 0
            print(f"  n={fb_n[i - 1]}→{fb_n[i]}: {fb_t[i - 1]:.4f}s → {fb_t[i]:.4f}s (x{crecimiento:.2f})")

    if len(pd_t) > 1:
        print("\nProgramación Dinámica (PD):")
        for i in range(1, len(pd_t)):
            crecimiento = pd_t[i] / pd_t[i - 1] if pd_t[i - 1] > 0 else 0
            print(f"  n={pd_n[i - 1]}→{pd_n[i]}: {pd_t[i - 1]:.4f}s → {pd_t[i]:.4f}s (x{crecimiento:.2f})")

    if len(v_t) > 1:
        print("\nAlgoritmo Voraz (V):")
        for i in range(1, len(v_t)):
            crecimiento = v_t[i] / v_t[i - 1] if v_t[i - 1] > 0 else 0
            print(f"  n={v_n[i - 1]}→{v_n[i]}: {v_t[i - 1]:.6f}s → {v_t[i]:.6f}s (x{crecimiento:.2f})")

    # Gráfica de crecimiento
    plt.plot(fb_n, fb_t, 'ro-', linewidth=3, markersize=10, label='FB - O(n x n!)', alpha=0.8)
    plt.plot(pd_n, pd_t, 'go-', linewidth=3, markersize=10, label='PD - O(n·2ⁿ)', alpha=0.8)
    plt.plot(v_n, v_t, 'bo-', linewidth=3, markersize=10, label='V - O(n log n)', alpha=0.8)

    plt.xlabel('Tamaño de Entrada (n)')
    plt.ylabel('Tiempo de Ejecución (segundos)')
    plt.title('Crecimiento de Complejidad Computacional\nComparación de Algoritmos')
    plt.legend()
    plt.grid(True, alpha=0.3)

    plt.savefig('docs/imagenes/crecimiento_complejidad.png', dpi=300, bbox_inches='tight')
    plt.show()


def generar_tabla_resultados(resultados):
    """Genera una tabla con los resultados numéricos"""
    print("\n" + "=" * 60)
    print("TABLA RESUMEN DE RESULTADOS")
    print("=" * 60)
    print(f"{'n':<4} {'FB (s)':<12} {'PD (s)':<12} {'V (s)':<12} {'FB/PD':<10} {'PD/V':<10}")
    print("-" * 60)

    # Encontrar todos los valores de n únicos
    todos_n = set()
    for algo in resultados.values():
        for n, t in algo:
            todos_n.add(n)

    todos_n = sorted(todos_n)

    for n in todos_n:

        fb_tiempo = next((t for n_val, t in resultados['FB'] if n_val == n), None)
        pd_tiempo = next((t for n_val, t in resultados['PD'] if n_val == n), None)
        v_tiempo = next((t for n_val, t in resultados['V'] if n_val == n), None)

        # Calcular ratios
        fb_pd_ratio = fb_tiempo / pd_tiempo if fb_tiempo and pd_tiempo and pd_tiempo > 0 else 0
        pd_v_ratio = pd_tiempo / v_tiempo if pd_tiempo and v_tiempo and v_tiempo > 0 else 0

        print(
            f"{n:<4} {fb_tiempo:<12.6f} {pd_tiempo:<12.6f} {v_tiempo:<12.6f} {fb_pd_ratio:<10.2f} {pd_v_ratio:<10.2f}")


if __name__ == "__main__":
    print("🚀 INICIANDO BENCHMARK...")
    resultados = ejecutar_benchmark()

    print("\n📊 GENERANDO GRÁFICAS...")
    graficar_resultados(resultados)
    generar_grafica_crecimiento(resultados)
    generar_tabla_resultados(resultados)

    print("\n✅ Benchmark completado!")
    print("📈 Gráficas guardadas en:")
    print("   - docs/imagenes/benchmark_comparativo.png")
    print("   - docs/imagenes/crecimiento_complejidad.png")
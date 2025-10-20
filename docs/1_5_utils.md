## Utils, antes de pasar a los algoritmos usados.

Este archivo contiene funciones auxiliares fundamentales para el proyecto que usan algunos de los metodos.

Por medio de
``` python
Finca = List[Tuple[int, int, int]]
```
se define el tipo de dato que representa una finca: En este caso, una lista de tuplas, donde cada tupla representa un tablón con `(ts, tr, p)`.


El siguiente bloque de codigo:
``` python
def calcular_tiempos_inicio(finca: Finca, permutacion: List[int]) -> List[int]:
```
Dice que, dado una permutación Π, se calcula cuándo comienza el riego de cada tablón. El tablón en la posición 0 de la permutación comienza en tiempo 0, y cada uno siguiente comienza cuando termina el anterior.

Su costo computacional es de O(n), ya que recorre la permutación una vez.

En este bloque de codigo
``` python
def calcular_costo(finca: Finca, permutacion: List[int]) -> int:
```
Permite calcular el costo total de riego por sufrimiento generado para la permutacion dada. 
Su costo es de O(n) para calcular tiempos + O(n) para sumar los costos por sufrimiento recorriendo una sola vez por cada accion la permutacion dada, es decir, su costo final es de: O(n).

La seccion
``` python
def generar_finca_aleatoria(n: int, ts_max: int = 20, tr_max: int = 5, p_max: int = 4) -> Finca:
```
Genera casos de prueba con valores aleatorios dentro de rangos, con el fin de hacer pruebas.


Los siguientes dos bloques:
``` python
def guardar_finca(finca: Finca, archivo: str):
```

``` python
def leer_finca(archivo: str) -> Finca:
```
Implementan el formato de entrada/salida, que es:
$$ n $$
$$ ts0, tr0, p0 $$
$$ ts1, tr1, p1 $$
$$ ... $$
$$ tsn, trn, pn $$

La ultima seccion
``` python
def escribir_salida(archivo: str, costo: int, permutacion: List[int]):
```
Implementa el formato de salida requerido:
$$ costo $$
$$ pi0 $$
$$ ... $$
$$ pin $$

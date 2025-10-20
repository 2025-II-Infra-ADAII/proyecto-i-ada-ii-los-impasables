## Voraz
En este caso, vamos a tener en cuenta una cosa, y es que aplicaremos una estrategia para una solución eficiente. La idea de la estrategia voraz es de optimización que toma decisiones localmente óptimas en cada paso, con la esperanza de alcanzar una solución globalmente óptima.

En este caso, usaremos esta logica para formar la estrategia, que en este caso se da de la siguiente manera.
Se ordenarán los tablones por medio de una clave voraz de mayor a menor, dada la formula:
$$
\text{clave}_i = \frac{p_i}{\text{ts}_i \cdot \text{tr}_i}
$$

Esta clave que se genera nos permite generar la estrategia, ya que nos permite priorizar los tablones con mayor prioridad, buscando tambien evitar en lo maximo posible la espera en tablones con bajo tiempo de supervivencia, buscando generar una especie de balanza entre la prioridad contra la supervivencia de cada tablon.
Se tiene en cuenta, además, que si su tiempo de supervivencia o de riego es 0, se le dará una clave infinita, haciendola de mayor prioridad de manera inmediata.

Ahora expliquemos codigo, con su unica función interna:
``` python
def roV(finca: Finca):
```
Se tiene en cuenta el caso base donde esta vacia la lista, para inmediatamente despues, en caso tal de que no este vacia, se trabaja en ella.
Se enumera cada uno de los tablones y se recorren por enumeracion, donde se le calcula la clave a cada uno y se maneja el caso excepcional mencionado anteriormente, guardandolas en una lista de pares junto al indice.
Costo: $$ O(n) $$

Por medio de el ordenamiento de python el cual es (timsort) se organizan las claves, manteniendo el orden de introduccion de datos en caso tal que se comparta clave con otra.
Costo: $$ O(n \log n) $$
Finalmente, se organiza la permutacion final que dio mejor resultado con la estrategia voraz.
Costo: $$ O(n) $$

Se calcula el costo, entonces, de la permutacion final.
Costo: $$ O(n) $$

Las pruebas se podran observar en la seccion de: `5_benchmark.md`

Dando por final que su coste computacional es de:
$$ O(n \log n) $$
Haciendolo significativamente mas eficiente que la fuerza bruta, sin embargo presenta un problema.

El resultado si bien es mucho mas eficiente que fuerza bruta, conserva una complicacion y es que **NO SIEMPRE** va a dar la respuesta mas eficiente.
Si bien esta solucion es optima para cuando no hay efectos acumulativos entre los tablones, en el momento en que las hay, su solucion optima local entorpece la solucion optima global.
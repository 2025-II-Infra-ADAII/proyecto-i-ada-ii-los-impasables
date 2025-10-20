## Fuerza bruta

La estrategia de **fuerza bruta** es siempre buscar evaluar **todas las posibles permutaciones** del posible orden en el que se pueden regar los tablones, calcular el costo total asociado a cada una y, finalizando el proceso, elegir aquella que genere **el costo mínimo posible (CRFΠ)**.  

Este método garantiza **_SIEMPRE_** la solución óptima, aunque su tiempo de ejecución crece de manera significativa con respecto al número de tablones.

En primeras, se hace lo siguiente:
``` python
generar_permutaciones(arr: List[int], l: int = 0):
```
Este metodo permite generar **TODAS** las permutaciones mediante la lista que se le introduce por medio de recursion, donde se fija un elemento y permuta el resto, generando así un coste computacional de O(n!)
Como tal se evalua primero si l == n-1, donde si se cumple, significa que ya se formó una permutación completa, entonces se retorna una copia. En caso tal de que no, intercambia el elemento actual con los siguientes y llama recursivamente para generar el resto. Finalmente, deshace el intercambio para restaurar el orden original (backtracking).
Además, se le atribuye un costo extra de O(n) por la creación de copias

Su complejidad computacional es de: $$O(n \times n!)$$

La funcion como tal,
``` python
def roFB(finca: Finca):
```
es la que implementa como tal el metodo de fuerza bruta. Primero, calcula el numero de tablones n, se crea una lista de indices donde se indica el orden de riego e inicializa varibles que permitiran seleccionar la mejor permutacion por costo.
Para cada una de las permutaciones se le calcula su costo, y en caso tal de definirse su costo como mejor al anterior, se actualiza para al final devolver la mejor permutacion.

El calculo de costo de cada una de las permutaciones es de
$$
O(n)
$$
ya que, nuevamente, se tiene en cuenta que se debe hacer esto para cada una de las permutaciones generadas.

El costo total de este metodo es de
$$
O(n \times n!)
$$

Este metodo siempre dará **La mejor respuesta posible, o en algunos casos, una de las mejores respuestas posibles** ya que hay listas donde hayan varias soluciones con el mismo mejor resultado.
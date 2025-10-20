# Interpretación del Proyecto

## Sobre el proyecto
El presente proyecto busca aplicar diferentes estrategias para resolver un mismo problema de naturaleza combinatoria: **calcular el plan de riego óptimo de una finca agrícola**.

A través del desarrollo del proyecto, se busca comparar el rendimiento, corrección y eficiencia de cada uno de los enfoques, buscando sus ventajas, desventajas y la busqueda sobre para que tipo de problema es más apropiado el uno del otro.  
Pero, como tal...

## ¿Cuál es el problema?

El problema plantea la situación de una finca que cuenta con varios **tablones de cultivo**, donde cada tablón posee tres características principales:

- `ts`: Es el tiempo de supervivencia → cuánto tiempo puede estar el cultivo en cuestion sin sufrir daños.  
- `tr`: Es el tiempo de regado → cuántos tiempo tarda en completarse su riego.  
- `p`: Es la prioridad (Un numero **entero** entre 1 y 4) → indica la importancia del tablón, siendo 4 la más alta.

Lo que se busca definir es, entonces, **el orden en que los tablones serán regados** debido a limitaciones.  
El objetivo entonces es: **minimizar el sufrimiento de los cultivos** a causa de la falta de agua, lo cual se mide mediante un costo total de riego.

El costo de sufrimiento para un tablón se define como:


$$
CRF_{\Pi}[i] = p_i \times \max \big( 0,\; (t_{\Pi_i} + tr_i) - ts_i \big)
$$

Donde: $$ (t_{\Pi_i} + tr_i) $$ indica el momento en el que el riego del tablon termina, siendo que si este excede ts<sub>i</sub>, el tablón sufre. Se hace una resta para poder representar los dias de retraso, y al multiplicarse por p<sub>i</sub> se obtiene la penalización ponderada dada por la prioridad (Cabe aclarar que si el riego acaba antes que ts<sub>i</sub>, su penalización es de 0).

El costo total y la formula que nos permite conocer cuanto sufrimiento se causó se obtiene al sumar todos los sufrimientos individuales talque:
$$
CRF_{\Pi} = \sum_{i=0}^{n-1} CRF_{\Pi}[i]
$$

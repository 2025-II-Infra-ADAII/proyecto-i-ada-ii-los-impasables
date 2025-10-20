## Dinamica

Como tal, el orden de riego optimo puede llegar a verse como una construccion incremental: Si tenemos un subconjunto parcial de tablones ya regados como:
$$ \text S \subseteq \{0, 1, 2,..., n-1\} $$
se puede decir que el siguiente tablon solo depende del costo minimo acumulado hasta dicho subconjunto.

Por ende, para este fin vamos a definir bien lo siguiente:
Se requiere de una mascara binaria que sea capaz de representar el grupo de tablones ya regados, donde si j esta "encendido", se puede decir que ya fue regado.

¿Cuantos subproblemas entonces se generan gracias a esto? Pues, dado que un tablon solo puede estar en dos estados (Regado o no regado), se dice que se generan:
$$ 2^n \ \text subproblemas$$

Una estructura de un problema de optimización con conjuntos (tipo bitmask DP).

Ahora, definamos el valor de la solucion optima.
Se sabe entonces que: $$ dp[S] = \text {Costo de regar los tablones en el conjunto S} $$
Donde **_S_** es una mascara binaria con los tablones ya regados
Por ende, vamos a trabajar bajo esa idea.

$$
dp[S]=\min_{j\in S}\{\,dp[S\setminus\{j\}]+p_j\cdot\max(0,T(S)-t_{S,j})\,\}
$$

Donde en primeras se toma el minimo, suponiendo que j es la ultima tarea en S.
Primero, se calcula en $ dp[S\setminus\{j\}] $ el coste optimo de calcular todo el riego en S exceptuando por j. Ademas, se tiene en cuenta $T(s)$ que es el tiempo total necesario para poder regar todos los tablones de S, por ende, la sección: $$ \ p_j\cdot\max(0,T(S)-t_{S,j})\, $$ evalua el costo adicional por regar el tablon j de ultimo en el conjunto S.
(En caso tal de que el tablon j sea el primero, se da el caso $dp[0] = 0$)

En el codigo, tenemos la funcion que encapsula todo esto definida como: 
``` python
def roPD(finca: Finca):
```
Se inicia con un caso base, e inmediatamente despues tras pasar este caso, se separa las listas de tiempos de supervivencia (ts), de regado (tr) y prioridades (p). Esto facilita el acceso directo a los datos de cada tablón por su índice.

``` python
ts = [x[0] for x in finca]
tr = [x[1] for x in finca]
p = [x[2] for x in finca]
```

De aqui, se creara un arreglo "total_tr", que sera el que contenga para cada masacara binaria el tiempo necesario para regar los tablones de dicha mascara; Este proceso se hace de manera incremental y no es necesario volver a repetir el proceso gracias a la propiedad de los bits.


Ahora vamos a trabajar la estructura principal del DP. Primero, en "dp" es donde se guardara el costo minimo de la riega del subconjunto de la mascara, "prev" nos permitira reconstruir el orden optimo mas tarde y se crea el caso base donde el costo es 0 ya que no hay tablones regados.

El nucleo del metodo dinamico ocurre en la siguiente seccion de codigo:
``` python
for mask in range(1, N):
        for j in range(n):
            if mask & (1 << j):
                mask_wo_j = mask ^ (1 << j)
                finish_j = total_tr[mask]
                tard_j = max(0, finish_j - ts[j])
                cost = dp[mask_wo_j] + p[j] * tard_j
                if cost < dp[mask]:
                    dp[mask] = cost
                    prev[mask] = j
```
En resumidas cuentas, lo que hace esta seccion es recorrer todos los subconjuntos posibles (la mascara) y todos los tablones j. Si el bit de j esta activo en la mascara, se determina que ese tablon **SI fue regado** en el subconjunto actual.
Secciones como "mask_wo__j" ayudan a obtener la mascara del subconjunto anterior al actual, "finish_j" permite conocer el tiempo total invertido de riego en el subconjunto actual, "tard_j" es el retraso del tablón j respecto a su tiempo de supervivencia.

El calculo del costo se da por subconjunto por costo acumulado suponiendo que j es el ultimo que se riega en el subconjunto, donde, si este costo mejora el minimo conocido para ese dicho subconjunto, se actualiza "dp" y se actualiza el "prev" para poder saber cual fue el ultimo tablon elegido.

Ahora se construira la solucion optima a traves de lo obtenido, usaremos "prev" con el fin de obtener el orden de riego optimo, ademas de que se obtendra el coste minimo total de riego de "dp[N-1]"

En la seccion de codigo: 

``` python
perm = []
mask = N - 1
while mask:
    j = prev[mask]
    perm.append(j)
    mask ^= (1 << j)
perm.reverse()
return perm, dp[N - 1]
```

Se parte desde el conjunto completo de mask = N - 1 para luego consultar en prev[mask] cuál fue el último tablón que se regó en la mejor solución de ese conjunto. Se adjunta dicho tablon a la lista y se elimina de la mascara y se repite hasta finalmente vaciar mask. Al estar adjuntandose de manera invertida, es necesario hacer un ".reverse()" a la lista final para organizar de manera correcta y obtener el orden correcto.

No se dieron estimaciones temporales y espaciales durante la explicacion ya que se dio prioridad a la explicacion de este algoritmo, pero ahora: ¿Temporal y espacialmente... que tal?

### Complejidad temporal y espacial
Como tal, el algoritmo recorre los $2^n$ subconjuntos posibles y en cada uno, se revisan hasta n tablones posibles como el ultimo elemento del subconjunto, por ende, su complejidad temporal final es de:
$$ O(n\times2^n)$$

El espacio de memoria usado esta inmediatamente determinado por los arreglos "dp", "prev" y "total_tr", y al ser cada uno de tamaño $2^n$, se puede decir entonces que la complejidad espacial necesaria para poder solucionar de manera dinamica es de:
$$ O(2^n) $$

Suponiendo un equipo que procesa $3\times 10^8$ operaciones por minuto y que cada celda ocupa **4 bytes**, evaluamos el comportamiento del algoritmo cuando $n = 2^k$ (es decir, el número de tablones crece como potencia de 2).  
En el código `roPD` el número de subproblemas es $2^n$. Aproximamos el número total de operaciones como $n \times 2^n$ y la memoria requerida contando las tres tablas principales (`dp`, `prev`, `total_tr`) como $3 \times 2^n$ celdas. Con 4 bytes por celda, la memoria en bytes es $12 \times 2^n$.

La siguiente tabla muestra, para valores de \(k\), los resultados calculados directamente a partir del código:

| k | n = 2ᵏ | Subconjuntos (2ⁿ) | Operaciones ≈ n·2ⁿ | Tiempo estimado (min) | Memoria (bytes) | Memoria (MB) |
|---:|-------:|-------------------:|-------------------:|----------------------:|-----------------:|-------------:|
| 1  | 2      | 4                  | 8                  | 2.67×10⁻⁸             | 48               | 4.58×10⁻⁵   |
| 2  | 4      | 16                 | 64                 | 2.13×10⁻⁷             | 192              | 1.83×10⁻⁴   |
| 3  | 8      | 256                | 2,048              | 6.83×10⁻⁶             | 3,072            | 2.93×10⁻³   |
| 4  | 16     | 65,536             | 1,048,576          | 3.50×10⁻³             | 786,432          | 0.75        |
| 5  | 32     | 4,294,967,296      | 1.37438953472×10¹¹ | 4.58×10²              | 51,539,607,552   | 49,152.00   |
| 6  | 64     | 1.8446744×10¹⁹     | 1.1805916207174113×10²¹ | 3.935305402391371×10¹² | 2.2136092888451462×10²⁰ | 2.11106232532992×10¹⁴ |

- **Subconjuntos (2ⁿ)** = $2^n$, con $n=2^k$.
- **Operaciones ≈ n·2ⁿ** corresponde a la estimación del bucle principal del código (para cada subconjunto se prueban hasta \(n\) candidatos).
- **Tiempo estimado (min)** = $\text (Operaciones) / 3\times 10^{8}$
- **Memoria (bytes)** = $3 \times 2^{n} \times 4 = 12 \cdot 2^{n}$  
- **Memoria (MB)** se calcula dividiendo los bytes entre $1024^2$.



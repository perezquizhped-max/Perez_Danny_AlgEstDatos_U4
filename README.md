# Laboratorio de eficiencia en Python - Unidad 4

Deber de **Algoritmos y Estructuras de Datos** (Ciencia de Datos, UPS).
Autor: Danny Pérez

## De qué trata

En este proyecto programé cuatro algoritmos que vimos en clase, medí cuánto
se demora cada uno con listas de distintos tamaños y después comparé lo que
salió con lo que decía la teoría.

Los algoritmos que se comparan son:

| Algoritmo | Tipo | Tiempo esperado | Espacio |
|---|---|---|---|
| Inserción | Ordenamiento simple | O(n²) | O(1) |
| Merge Sort | Ordenamiento eficiente | O(n log n) | O(n) |
| Búsqueda lineal | Búsqueda | O(n) | O(1) |
| Búsqueda binaria | Búsqueda (lista ordenada) | O(log n) | O(1) |

## Archivos

- `algoritmos.py`: aquí están los cuatro algoritmos, con la complejidad
  comentada en cada uno.
- `main.py`: genera las listas al azar, mide los tiempos con
  `time.perf_counter()` y muestra por pantalla la tabla con los tiempos y las
  razones.
- `README.md`: este archivo.

## Cómo ejecutarlo

Solo se necesita Python 3, no hay que instalar nada extra (uso solo la
biblioteca estándar: `random`, `time` y `cProfile`).

Abrir una terminal en la carpeta del proyecto y correr:

```
python main.py
```

Si en su computador no funciona `python`, probar con `py main.py`.

Al correrlo primero revisa que los cuatro algoritmos den bien, y después
imprime una tabla por algoritmo con los tamaños 1.000, 2.000, 4.000 y 8.000.

### Opcional: ver el cuello de botella con cProfile

```
python main.py perfil
```

Esto muestra el reporte de `cProfile`. Ahí se ve que la función que más
tiempo se lleva es `insercion`.

## Cómo se hizo la medición

- Las listas se generan con números al azar entre 1 y 1.000.000. Dejé una
  semilla fija (`random.seed(42)`) para que los datos sean siempre los mismos.
- Cada medición se hace 3 veces y me quedo con la mejor, para que el
  computador no meta tanto ruido.
- Las búsquedas buscan el número 0, que nunca está en la lista, o sea el
  **peor caso**.
- La búsqueda binaria necesita la lista ordenada, entonces la ordeno antes
  con Merge Sort. Ese ordenamiento no cuenta en el tiempo medido.
- Una sola búsqueda binaria demora menos de una millonésima de segundo y el
  tiempo sale casi cero, así que la repito 20.000 veces y saco el promedio.
  Con la lineal hago lo mismo, pero 200 veces.
- Lo importante de la tabla es la **razón** entre una fila y la anterior, no
  los segundos, porque los segundos dependen del computador.

## Qué entrega el programa

Por cada algoritmo se muestra una tabla así:

```
     n      tiempo(s)    razon   esperada (Tabla 16)
  1000     0.01297805        -
  2000     0.05109907     3.94   ~ 4
```

La última columna es lo que dice la Tabla 16 de la Clase 12 para esa
complejidad, para comparar rápido.

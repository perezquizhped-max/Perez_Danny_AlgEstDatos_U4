"""
algoritmos.py
Algoritmos del laboratorio de eficiencia (Unidad 4).
Aqui estan los cuatro algoritmos: insercion, merge sort,
busqueda lineal y busqueda binaria.
"""


# ---------------------------------------------------------------
# ORDENAMIENTO SIMPLE: INSERCION
# ---------------------------------------------------------------
def insercion(lista):
    # insercion: O(n^2) en tiempo (mejor caso O(n) si ya esta ordenada)
    # espacio: O(1), ordena sobre la misma lista sin crear otra
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        # corremos a la derecha los elementos mayores que "actual"
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista


# ---------------------------------------------------------------
# ORDENAMIENTO EFICIENTE: MERGE SORT
# ---------------------------------------------------------------
def fusionar(izq, der):
    # fusionar: O(n), recorre las dos mitades una sola vez
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado


def merge_sort(lista):
    # merge sort: O(n log n) SIEMPRE (log n niveles x O(n) por nivel)
    # espacio: O(n) por las listas auxiliares que se van creando
    # recurrencia: T(n) = 2*T(n/2) + O(n)
    if len(lista) <= 1:          # caso base
        return lista
    medio = len(lista) // 2
    izq = merge_sort(lista[:medio])    # dividir
    der = merge_sort(lista[medio:])
    return fusionar(izq, der)          # vencer


# ---------------------------------------------------------------
# BUSQUEDAS
# ---------------------------------------------------------------
def busqueda_lineal(lista, objetivo):
    # busqueda lineal: O(n) en el peor caso (el elemento esta al final o no esta)
    # espacio: O(1), solo usamos unas variables
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1


def busqueda_binaria(lista, objetivo):
    # busqueda binaria: O(log n), descarta la mitad en cada vuelta
    # espacio: O(1), version iterativa con dos indices
    # recurrencia: T(n) = T(n/2) + O(1)
    # PRECONDICION: la lista debe estar ordenada
    izq, der = 0, len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izq = medio + 1      # descarta la izquierda
        else:
            der = medio - 1      # descarta la derecha
    return -1

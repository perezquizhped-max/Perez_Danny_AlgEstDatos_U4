"""
main.py
Laboratorio de eficiencia - Unidad 4 (Algoritmos y Estructuras de Datos)
Autor: Danny Perez

Como correrlo:   py main.py            (en Windows)
                 python main.py        (en otros sistemas)
Con cProfile:    py main.py perfil
"""
import random
import sys
import time
import cProfile
import pstats

from algoritmos import insercion, merge_sort, busqueda_lineal, busqueda_binaria

TAMANOS = [1000, 2000, 4000, 8000]
CORRIDAS = 3          # cada medicion se hace 3 veces y nos quedamos con la mejor
OBJETIVO = 0          # los datos van de 1 a 10^6, asi que el 0 NO esta: peor caso


def medir(funcion, datos, repeticiones=1):
    """Devuelve el tiempo en segundos de UNA llamada a funcion(datos).

    Si la funcion es muy rapida (como la busqueda binaria) la repetimos
    muchas veces y sacamos el promedio, para que el tiempo no salga casi cero.
    """
    mejor = None
    for _ in range(CORRIDAS):
        copia = list(datos)                    # asi no danamos la lista original
        inicio = time.perf_counter()
        for _ in range(repeticiones):
            funcion(copia)
        total = time.perf_counter() - inicio
        if mejor is None or total < mejor:
            mejor = total
    return mejor / repeticiones


def verificar():
    """Revisa que los cuatro algoritmos den bien antes de medir."""
    prueba = [random.randint(1, 1000) for _ in range(500)]
    esperado = sorted(prueba)
    assert insercion(list(prueba)) == esperado, "Fallo insercion"
    assert merge_sort(list(prueba)) == esperado, "Fallo merge sort"
    elegido = esperado[123]
    assert esperado[busqueda_lineal(esperado, elegido)] == elegido, "Fallo lineal"
    assert esperado[busqueda_binaria(esperado, elegido)] == elegido, "Fallo binaria"
    assert busqueda_lineal(esperado, -5) == -1, "Lineal debia dar -1"
    assert busqueda_binaria(esperado, -5) == -1, "Binaria debia dar -1"
    print("Verificacion: los 4 algoritmos funcionan bien.\n")


def tabla(nombre, esperada, funcion_para, repeticiones=1):
    """Mide un algoritmo con todos los tamanos e imprime su tabla."""
    print(f"=== {nombre} ===")
    print(f"{'n':>6} {'tiempo(s)':>14} {'razon':>8}   {'esperada (Tabla 16)'}")
    anterior = None
    for n in TAMANOS:
        datos = [random.randint(1, 10**6) for _ in range(n)]
        t = medir(funcion_para(datos), datos, repeticiones)
        razon = f"{t / anterior:.2f}" if anterior else "-"
        esp = esperada if anterior else ""
        print(f"{n:>6} {t:>14.8f} {razon:>8}   {esp}")
        anterior = t
    print()


def laboratorio():
    random.seed(42)      # semilla fija: los datos al azar son siempre los mismos
    verificar()

    print("Tiempos por llamada, mejor de 3 corridas. La razon es contra la fila de arriba.\n")

    tabla("Insercion (simple)", "~ 4",
          lambda datos: insercion)

    tabla("Merge Sort (eficiente)", "algo mas de 2",
          lambda datos: merge_sort)

    # la lineal no necesita orden; la usamos sobre la lista tal cual
    tabla("Busqueda lineal (peor caso)", "~ 2",
          lambda datos: (lambda lista: busqueda_lineal(lista, OBJETIVO)),
          repeticiones=200)

    # la binaria SI necesita lista ordenada: la ordenamos con Merge Sort
    # (ese ordenamiento se hace antes de cronometrar, no cuenta en el tiempo)
    def preparar_binaria(datos):
        ordenada = merge_sort(datos)
        datos[:] = ordenada          # dejamos "datos" ya ordenada
        return lambda lista: busqueda_binaria(lista, OBJETIVO)

    print("=== Busqueda binaria (peor caso, lista ordenada con Merge Sort) ===")
    print(f"{'n':>6} {'tiempo(s)':>14} {'razon':>8}   {'esperada (Tabla 16)'}")
    anterior = None
    for n in TAMANOS:
        datos = [random.randint(1, 10**6) for _ in range(n)]
        funcion = preparar_binaria(datos)
        t = medir(funcion, datos, repeticiones=20000)
        razon = f"{t / anterior:.2f}" if anterior else "-"
        esp = "apenas mayor que 1" if anterior else ""
        print(f"{n:>6} {t:>14.8f} {razon:>8}   {esp}")
        anterior = t
    print()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "perfil":
        # opcional: profiling con cProfile para ver el cuello de botella
        perfil = cProfile.Profile()
        perfil.runcall(laboratorio)
        pstats.Stats(perfil).sort_stats("cumulative").print_stats(8)
    else:
        laboratorio()


"""Herramientas para medir tiempo y memoria de una función."""

from statistics import mean
import timeit
import tracemalloc


def medir_recursos(funcion, repeticiones=5):
    """Mide tiempo de ejecución y memoria máxima."""
    if not callable(funcion):
        raise TypeError(
            "Se debe proporcionar una función ejecutable."
        )

    if repeticiones < 1:
        raise ValueError(
            "La cantidad de repeticiones debe ser mayor que cero."
        )

    tiempos = timeit.repeat(
        funcion,
        repeat=repeticiones,
        number=1,
    )

    tracemalloc.start()
    funcion()
    _, memoria_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "tiempo_promedio_s": mean(tiempos),
        "tiempo_minimo_s": min(tiempos),
        "memoria_pico_mib": memoria_pico / (1024 ** 2),
    }


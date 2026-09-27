"""Funciones reutilizables del proyecto MCDI500 Grupo 9."""

from pathlib import Path


class ProyectoError(Exception):
    """Error específico de validación del proyecto."""


def buscar_raiz(inicio="."):
    """Busca la raíz que contiene README.md y la carpeta F1."""
    actual = Path(inicio).resolve()

    for carpeta in [actual, *actual.parents]:
        if (carpeta / "README.md").is_file() and (carpeta / "F1").is_dir():
            return carpeta

    raise ProyectoError("No se encontró la raíz del proyecto.")


def validar_columnas(columnas, esperadas):
    """Comprueba que estén presentes todas las columnas esperadas."""
    faltantes = sorted(set(esperadas) - set(columnas))

    if faltantes:
        raise ProyectoError(f"Faltan columnas: {faltantes}")

    return True


"""Funciones para localizar y cargar los datos del proyecto."""

from pathlib import Path

import pandas as pd


def buscar_raiz(inicio):
    """Busca la raíz del repositorio desde una carpeta inicial."""
    actual = Path(inicio).resolve()

    for candidata in [actual, *actual.parents]:
        tiene_readme = (candidata / "README.md").is_file()
        tiene_f1 = (candidata / "F1").is_dir()
        tiene_f2 = (candidata / "F2").is_dir()

        if tiene_readme and tiene_f1 and tiene_f2:
            return candidata

    raise FileNotFoundError(
        "No se encontró la raíz del repositorio."
    )


def cargar_csv(ruta, nombre):
    """Comprueba y carga un archivo CSV."""
    ruta = Path(ruta)

    if not ruta.is_file():
        raise FileNotFoundError(
            f"No se encontró {nombre}: {ruta}"
        )

    try:
        datos = pd.read_csv(
            ruta,
            encoding="utf-8-sig",
        )
    except pd.errors.EmptyDataError as error:
        raise ValueError(
            f"El archivo {nombre} está vacío."
        ) from error

    if datos.empty:
        raise ValueError(
            f"El archivo {nombre} no contiene registros."
        )

    print(
        f"{nombre}: "
        f"{datos.shape[0]} filas x "
        f"{datos.shape[1]} columnas"
    )

    return datos



"""Fábrica de transformadores para el pipeline."""

from .transformadores import CodificadorOneHot
from .transformadores import EscaladorRobusto


class FabricaTransformadores:
    """Crea un transformador según el tipo de variable."""

    @staticmethod
    def crear(tipo, columna):
        if not isinstance(tipo, str):
            raise TypeError(
                "El tipo de transformador debe ser texto."
            )

        tipo_normalizado = tipo.strip().lower()

        if tipo_normalizado == "categorica":
            return CodificadorOneHot(columna)

        if tipo_normalizado == "numerica":
            return EscaladorRobusto(columna)

        raise ValueError(
            f"Tipo de transformador desconocido: {tipo}"
        )

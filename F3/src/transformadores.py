
"""Clases de transformación utilizadas en la Fase 3."""

import numpy as np
import pandas as pd

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import RobustScaler


class Transformador:
    """Clase base para las transformaciones del pipeline."""

    def __init__(self, columna):
        self.columna = columna
        self._parametros = {}
        self._ajustado = False

    def ajustar(self, datos):
        """Aprende los parámetros desde entrenamiento."""
        if self.columna not in datos.columns:
            raise KeyError(
                f"No existe la columna: {self.columna}"
            )

        self._parametros = self.aprender(datos)
        self._ajustado = True
        return self

    def transformar(self, datos):
        """Aplica los parámetros aprendidos."""
        if not self._ajustado:
            raise RuntimeError(
                "El transformador debe ajustarse "
                "antes de transformar."
            )

        if self.columna not in datos.columns:
            raise KeyError(
                f"No existe la columna: {self.columna}"
            )

        return self.aplicar(datos.copy())

    def aprender(self, datos):
        """Cada clase hija define qué necesita aprender."""
        raise NotImplementedError

    def aplicar(self, datos):
        """Cada clase hija define cómo transforma los datos."""
        raise NotImplementedError


class CodificadorOneHot(Transformador):
    """Convierte una categoría en columnas binarias."""

    def aprender(self, datos):
        codificador = OneHotEncoder(
            sparse_output=False,
            handle_unknown="error",
            dtype=np.int8,
        )

        codificador.fit(datos[[self.columna]])

        return {
            "codificador": codificador,
            "columnas": (
                codificador.get_feature_names_out(
                    [self.columna]
                ).tolist()
            ),
        }

    def aplicar(self, datos):
        codificador = self._parametros["codificador"]
        columnas = self._parametros["columnas"]

        matriz = codificador.transform(
            datos[[self.columna]]
        )

        datos_codificados = pd.DataFrame(
            matriz,
            columns=columnas,
            index=datos.index,
        )

        return pd.concat(
            [
                datos.drop(columns=[self.columna]),
                datos_codificados,
            ],
            axis=1,
        )


class EscaladorRobusto(Transformador):
    """Escala una variable mediante mediana e IQR."""

    def aprender(self, datos):
        escalador = RobustScaler()
        escalador.fit(datos[[self.columna]])

        return {
            "escalador": escalador,
            "mediana": float(escalador.center_[0]),
            "iqr": float(escalador.scale_[0]),
        }

    def aplicar(self, datos):
        escalador = self._parametros["escalador"]

        valores_escalados = escalador.transform(
            datos[[self.columna]]
        )

        datos[self.columna] = valores_escalados.ravel()

        return datos


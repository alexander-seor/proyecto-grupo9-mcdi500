
"""Pipeline de transformación utilizado en la Fase 3."""


class Pipeline:
    """Organiza y ejecuta los pasos de transformación."""

    def __init__(self, pasos):
        self._pasos = list(pasos)
        self._ajustado = False

    def ajustar(self, datos):
        intermedio = datos.copy()

        for paso in self._pasos:
            paso.ajustar(intermedio)
            intermedio = paso.transformar(intermedio)

        self._ajustado = True
        return self

    def transformar(self, datos):
        if not self._ajustado:
            raise RuntimeError(
                "El pipeline debe ajustarse antes de transformar."
            )

        resultado = datos.copy()

        for paso in self._pasos:
            resultado = paso.transformar(resultado)

        return resultado

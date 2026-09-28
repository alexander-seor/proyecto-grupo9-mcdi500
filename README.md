Proyecto Grupo 9 — MCDI500

**Asignatura:** Programación para la Ciencia  
**Grupo:** 9  
**Estudiante:** Alexander Sepulveda Ormazabal

Proyecto de análisis de datos reproducible y documentado, desarrollado con el **AI4I 2020 Predictive Maintenance Dataset**. El trabajo comprende la definición del problema, la comprensión y validación de los datos y, posteriormente, su exploración, preparación y modelamiento.

## Integrantes

- Alexander Sepulveda Ormazabal ([@alexander-seor](https://github.com/alexander-seor)).

## Problemática

Las fallas inesperadas en maquinaria industrial pueden generar interrupciones operacionales, pérdidas de productividad y mayores necesidades de mantenimiento. El dataset AI4I 2020 contiene información sobre distintas condiciones de operación de equipos, como temperatura, velocidad de rotación, torque y desgaste de herramienta, además del registro de ocurrencia de fallas.

El proyecto buscará **identificar qué condiciones operacionales están asociadas con las fallas, reconocer posibles patrones de riesgo y posteriormente evaluar si estas variables permiten anticipar su ocurrencia.**

## Pregunta de investigación

> ¿Qué condiciones operacionales están asociadas con la ocurrencia de fallas en maquinaria industrial y en qué medida estas variables permiten identificar situaciones de riesgo de falla?

## Objetivo y alcance

Analizar la relación entre las condiciones operacionales y la ocurrencia de fallas, identificar posibles patrones de riesgo y evaluar posteriormente la capacidad predictiva de estas variables.

La **Fase 1** se centra en definir y orientar el proyecto, organizar el entorno reproducible y comprender los datos. La exploración, preparación y evaluación de modelos se desarrollarán progresivamente en las siguientes entregas. Las asociaciones encontradas no se interpretarán por sí solas como relaciones causales.

## Estructura del proyecto

```text
proyecto-grupo9-mcdi500/
├── README.md
├── requirements.txt
├── .gitignore
├── F1/
│   ├── data/
│   │   ├── raw/
│   │   └── processed/
│   ├── notebooks/
│   ├── docs/
│   └── src/
├── F2/
├── F3/
└── F4/
```

| Ruta | Propósito |
| --- | --- |
| `README.md` | Presentación del proyecto e instrucciones de ejecución. |
| `requirements.txt` | Dependencias necesarias para reproducir el trabajo. |
| `.gitignore` | Exclusión del entorno virtual, cachés y archivos temporales del control de versiones. |
| `F1/data/raw/` | Datos originales, conservados sin modificaciones. |
| `F1/data/processed/` | Datos derivados de transformaciones documentadas. |
| `F1/notebooks/` | Notebooks con código, metodología, decisiones y resultados. |
| `F1/docs/` | Mapa conceptual, documentación, informes y exportaciones HTML. |
| `F1/src/` | Funciones y código reutilizable. |
| `F1/` | Definición del problema y entorno reproducible. |
| `F2/` | Obtención, limpieza y transformación de datos. |
| `F3/` | Núcleo algorítmico: programación estructurada, recursiva y orientada a objetos. |
| `F4/` | Análisis, visualización y comunicación de resultados. |

## Dataset y clasificación de variables

**AI4I 2020** es un conjunto de datos sintético con **10.000 registros** que representa condiciones de mantenimiento predictivo industrial. El archivo original incluye identificadores, seis posibles predictores, una variable de falla general y cinco indicadores de modos de falla.

**Dimensiones del archivo original:** 10.000 filas y 14 columnas, incluidos los identificadores y las etiquetas de falla.

**Licencia:** [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/), según la ficha de UCI. Al reutilizar los datos, conservar la atribución a la fuente e indicar las modificaciones realizadas.

**Obtención:** si el CSV no está en el repositorio, descargarlo desde la [página oficial de AI4I 2020](https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset), descomprimir la descarga y colocar `ai4i2020.csv` en `F1/data/raw/ai4i2020.csv`.

| Categoría | Variables | Naturaleza y uso |
| --- | --- | --- |
| Identificadores | `UDI`, `Product ID` | Identificación de registros o productos; no representan magnitudes operacionales y se excluyen de los predictores. |
| Tipo de producto | `Type` | Categórica con niveles L, M y H de calidad del producto. |
| Temperaturas | `Air temperature [K]`, `Process temperature [K]` | Cuantitativas continuas, expresadas en kelvin. |
| Velocidad de rotación | `Rotational speed [rpm]` | Magnitud cuantitativa continua, registrada en revoluciones por minuto. |
| Torque | `Torque [Nm]` | Cuantitativa continua, expresada en newton metro. |
| Desgaste de herramienta | `Tool wear [min]` | Tiempo acumulado de uso, registrado en minutos enteros. |
| Variable objetivo | `Machine failure` | Categórica binaria: 0 indica ausencia de falla y 1 indica falla. |
| Modos de falla | `TWF`, `HDF`, `PWF`, `OSF`, `RNF` | Indicadores binarios de tipos de falla; se excluyen como predictores de la falla general para evitar fuga de información. |

Los modos corresponden a fallas por desgaste de herramienta (**TWF**), disipación de calor (**HDF**), potencia (**PWF**), sobreesfuerzo (**OSF**) y fallas aleatorias (**RNF**).

La clasificación distingue la naturaleza de la variable de su formato de almacenamiento: un identificador numérico no es una variable cuantitativa de análisis y una medición registrada como entero no necesariamente representa un conteo.

**Fuente:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset). Su carácter sintético debe considerarse al interpretar resultados; el desempeño sobre este dataset no demuestra por sí solo capacidad de anticipación en equipos reales.

## Preservación y validación de datos

- Conservar el archivo original en `F1/data/raw/` sin sobrescribirlo.
- Guardar los datos transformados en `F1/data/processed/` y documentar cómo se generaron.
- Registrar fuente, fecha de obtención, unidades y significado de las variables en la documentación o el notebook.
- Revisar dimensiones, nombres de columnas, tipos de datos, valores faltantes, duplicados, rangos y distribución de la variable objetivo.
- Justificar las decisiones de limpieza y selección de variables antes de aplicarlas.

Estos puntos describen el procedimiento de trabajo; las verificaciones realizadas y sus resultados deben quedar respaldados en los notebooks.

## Estado del proyecto

### Formativa 1

- [x] Creación de la estructura del repositorio.
- [x] Configuración del entorno virtual.
- [x] Configuración de dependencias.
- [x] Incorporación del dataset original.
- [x] Revisión de la estructura del dataset.
- [x] Identificación y clasificación de variables.
- [x] Validación de la clasificación de variables.
- [x] Definición inicial de la problemática.
- [x] Formulación de la pregunta de investigación.
- [x] Elaboración del mapa conceptual del flujo reproducible.


## Requisitos y ejecución

**Versión utilizada: Python 3.13.0**, informada mediante la consulta de versión en la terminal. Comprobar que el kernel del notebook utiliza el mismo entorno. La instalación completa de las dependencias debe verificarse antes de dar por reproducida la ejecución.

Se requieren Git, Python y las dependencias de `requirements.txt`. Comprobar la versión del intérprete con `python --version` (o `python3 --version` en macOS/Linux).

Ejecutar los siguientes comandos desde la raíz del repositorio.

### 1. Crear el entorno virtual

```bash
python -m venv .venv
```

En macOS/Linux, si el intérprete se invoca como `python3`, utilizar `python3 -m venv .venv`. Comprobar que corresponde a la versión requerida.

### 2. Activar el entorno

En **Windows PowerShell**:

```powershell
.\.venv\Scripts\Activate.ps1
```

En **Windows, símbolo del sistema (CMD)**:

```bat
.venv\Scripts\activate.bat
```

En **Windows, Git Bash**:

```bash
source .venv/Scripts/activate
```

En **macOS y Linux**:

```bash
source .venv/bin/activate
```

### 3. Instalar las dependencias

```bash
python -m pip install -r requirements.txt
```

Registrar la versión de Python utilizada y mantener las versiones de las dependencias en `requirements.txt`. El entorno `.venv/` no debe incorporarse al repositorio.

### 4. Abrir y ejecutar el notebook

JupyterLab y nbconvert están incluidos con versiones fijadas en el `requirements.txt` revisado. Para abrir JupyterLab:

```bash
python -m jupyterlab
```

Abrir el archivo `.ipynb` correspondiente en `F1/notebooks/` y seleccionar el kernel asociado al entorno del proyecto. Si se utiliza otra interfaz, como VS Code o Jupyter Notebook, seleccionar igualmente ese entorno.

Orden recomendado, según el contenido actual de los notebooks:

| Orden | Notebook | Función actual |
| --- | --- | --- |
| 1 | `F1/notebooks/F1_Definicion.ipynb` | Comprobar el intérprete, la carpeta de trabajo y la disponibilidad de numpy, pandas, matplotlib y sklearn. Actualmente contiene la comprobación del entorno; la definición narrativa del proyecto queda por incorporar al notebook. |
| 2 | `F1/notebooks/validador.ipynb` | Cargar el CSV, generar un perfil de variables, revisar requisitos, escribir `F1/docs/informe_dataset.md` y comparar la clasificación automática con la del equipo. |

Este orden facilita revisar el entorno antes de validar los datos; el validador no consume un archivo generado por el primer notebook. Los archivos de `.ipynb_checkpoints/` son copias automáticas de Jupyter y no se ejecutan como entregables. Incluir `.ipynb_checkpoints/` en `.gitignore`.

El validador utiliza rutas relativas a la raíz del repositorio. Abrir Jupyter desde esa raíz no garantiza que el kernel la utilice como carpeta de trabajo. Antes de ejecutar sus celdas, establecerla con esta celda inicial (funciona si el kernel parte de la raíz o de alguna subcarpeta del proyecto):

```python
from pathlib import Path
import os

actual = Path.cwd().resolve()
raiz = next(
    (p for p in [actual, *actual.parents]
     if (p / "F1/data/raw/ai4i2020.csv").is_file()),
    None,
)
if raiz is None:
    raise FileNotFoundError("Abra el proyecto y compruebe F1/data/raw/ai4i2020.csv")
os.chdir(raiz)
Path("F1/docs").mkdir(parents=True, exist_ok=True)
print("Raíz del proyecto:", Path.cwd())
```

Esta celda está documentada aquí para incorporarla al notebook; no se ha añadido automáticamente a los archivos originales.

Antes de compartir resultados, **reiniciar el kernel, ejecutar todas las celdas en orden y guardar el notebook**. Revisar que las rutas de los datos sean relativas y estén documentadas, para evitar dependencias de carpetas personales.

### 5. Exportar el notebook a HTML

Con los notebooks ejecutados y guardados, exportar copias para su lectura en el navegador. Desde la raíz del repositorio y con `nbconvert` instalado en el entorno:

```bash
python -m jupyter nbconvert --to html "F1/notebooks/F1_Definicion.ipynb" "F1/notebooks/validador.ipynb" --output-dir "F1/docs"
```

El HTML se guardará en `F1/docs/`. Abrirlo en un navegador y comprobar textos, tablas y gráficos. Este comando exporta los resultados ya guardados; no vuelve a ejecutar las celdas.

Conservar el **`.ipynb` como versión editable y ejecutable** y el **`.html` como versión de consulta**. Si JupyterLab o nbconvert se incorporan al flujo del proyecto, registrar sus versiones en `requirements.txt`.

## Documentación científica

Los notebooks integrarán:

- **Markdown:** problemática, pregunta, metodología, decisiones, interpretación y referencias.
- **Código:** carga, validación, transformación y análisis de datos.
- **Resultados:** tablas y gráficos con títulos, unidades y explicaciones vinculadas al objetivo.
- **Conclusiones:** hallazgos, limitaciones y pasos siguientes.

El README orienta la ejecución; los notebooks explican el análisis y `F1/docs/` conserva la documentación complementaria.

### Documentos disponibles

- [Mapa conceptual de la Formativa 1](F1/docs/mcdi500_s1_grupo9.pdf).
- [Informe de validación del dataset](F1/docs/informe_dataset.md).

### Comprobaciones pendientes del repositorio

- Añadir `.venv/`, `__pycache__/` y `*.pyc` a `.gitignore`; la versión revisada solo excluye `.ipynb_checkpoints/`.
- Comprobar si esos archivos ya están versionados: añadirlos a `.gitignore` no elimina su seguimiento previo.
- Verificar la instalación en macOS/Linux antes de afirmar compatibilidad: el listado actual incluye `pywinpty` sin un marcador de plataforma.
- Incorporar la definición narrativa al notebook `F1_Definicion.ipynb` y comprobar la ejecución completa desde un kernel limpio.

## Control de versiones y colaboración

Git permite registrar cambios y GitHub compartir el repositorio. Revisar los archivos modificados antes de prepararlos y utilizar commits descriptivos que identifiquen una tarea concreta.

Por ejemplo, para registrar una actualización de este documento:

```bash
git status
git add README.md
git commit -m "docs: actualiza problemática y reproducibilidad del Grupo 9"
git push
```

Para otras tareas, seleccionar los archivos correspondientes con `git add`.

### Convención de commits

Usar el formato `prefijo: descripción breve del cambio`.

| Prefijo | Uso | Ejemplo |
| --- | --- | --- |
| `docs` | Documentación y explicaciones. | `docs: documenta clasificación de variables AI4I` |
| `data` | Incorporación o transformación de datos. | `data: incorpora dataset original AI4I` |
| `feat` | Nueva funcionalidad o código de análisis. | `feat: agrega validación de columnas` |
| `fix` | Corrección de errores. | `fix: corrige ruta de carga del CSV` |

Acordar tareas y responsables, revisar los cambios antes de integrarlos y documentar decisiones relevantes. El historial debe permitir relacionar las modificaciones de datos, código y documentación con los resultados del análisis.

### Práctica de resolución de conflictos

Actividad pendiente de realizar conjuntamente en un archivo de prueba:

1. Crear y registrar un archivo de prueba con una línea de texto común.
2. Crear dos ramas desde ese mismo commit y modificar la misma línea de manera distinta en cada rama.
3. Intentar integrar una rama en la otra para provocar el conflicto.
4. Revisar juntos ambas versiones, acordar el contenido final y eliminar los marcadores de conflicto.
5. Preparar el archivo resuelto con `git add`, completar el commit y comprobar con `git status` que no queden conflictos.
6. Guardar en `F1/docs/` una evidencia del conflicto, la resolución acordada y el identificador del commit.

## Decisiones técnicas

Las siguientes decisiones orientan el trabajo; no implican que todas las transformaciones o evaluaciones ya se hayan ejecutado.

| Decisión | Motivo |
| --- | --- |
| Conservar `raw` y escribir derivados en `processed`. | Mantener una fuente original verificable y permitir reconstruir las transformaciones. |
| Utilizar `.venv` y registrar versiones en `requirements.txt`. | Aislar dependencias y facilitar la reproducción del entorno. |
| Analizar `Machine failure` como objetivo binario. | Vincular las condiciones operacionales con la presencia o ausencia de falla. |
| Excluir `UDI` y `Product ID` de los predictores. | Evitar utilizar identificadores como señales operacionales. |
| Excluir TWF, HDF, PWF, OSF y RNF de los predictores. | Evitar fuga de información desde indicadores relacionados con la falla objetivo. |
| Conservar el notebook junto con una exportación HTML. | Mantener una versión ejecutable y otra de consulta. |
| Evaluar posteriormente el desbalance y separar entrenamiento y prueba. | Evitar conclusiones engañosas y evaluar sobre datos no usados para ajustar el modelo. |

Actualizar este registro al tomar nuevas decisiones, indicando su motivo y la evidencia que las respalda. Revisar el README al cerrar cada fase.

## Proyección del trabajo

El análisis posterior explorará distribuciones, relaciones entre variables y diferencias entre registros con y sin falla. A continuación, se evaluarán alternativas de preparación y modelamiento.

En la evaluación predictiva se considerarán el balance de clases, la separación entre entrenamiento y prueba, el control de fuga de información y semillas reproducibles. Las transformaciones que aprendan de los datos se ajustarán únicamente con el conjunto de entrenamiento.

## Referencias

*AI4I 2020 predictive maintenance dataset* [Conjunto de datos]. (2020). UCI Machine Learning Repository. https://doi.org/10.24432/C5HS5C

Novak, J. D., & Cañas, A. J. (2008). *The theory underlying concept maps and how to construct and use them* (Technical Report IHMC CmapTools 2006-01 Rev 01-2008). Florida Institute for Human and Machine Cognition. https://cmap.ihmc.us/docs/theory-of-concept-maps

---

## Actualización del avance F1–F2

Esta sección complementa el registro inicial del README con la implementación realizada posteriormente. Las listas y proyecciones anteriores se conservan como evidencia de la planificación original; el estado actualizado se presenta a continuación.

### Objetivos específicos actualizados

1. Documentar la procedencia, estructura y roles analíticos de las variables de AI4I 2020.
2. Configurar un entorno reproducible con dependencias, rutas y semilla controladas.
3. Explorar tipos, nulos, duplicados, categorías, rangos, valores atípicos y distribución de la variable objetivo.
4. Construir un pipeline de limpieza y transformación que evite fuga de información.
5. Validar los resultados mediante comprobaciones de integridad y pruebas normales, límite y de excepción.
6. Preparar conjuntos separados de entrenamiento y prueba para las fases posteriores.

### Alcance, supuestos y limitaciones

- El análisis se limita a las variables incluidas en AI4I 2020.
- Se utilizan las unidades y definiciones publicadas por UCI.
- El archivo es sintético y no representa una planta industrial específica.
- La ausencia de valores faltantes evita la imputación, pero no garantiza que todas las observaciones sean representativas de maquinaria real.
- Los valores extremos se conservan porque pueden representar condiciones operacionales relacionadas con fallas.
- La Fase 2 prepara y valida los datos; todavía no estima el desempeño de un modelo predictivo.
- El desbalance de `Machine failure` deberá considerarse al seleccionar métricas y métodos posteriores.

### Estructura incorporada en F2

```text
F2/
├── F2_preprocesamiento.ipynb
├── data/
│   └── processed/
│       ├── ai4i2020_entrenamiento_procesado.csv
│       └── ai4i2020_prueba_procesado.csv
└── docs/
    ├── F2_preprocesamiento.html
    ├── diccionario_variables.csv
    ├── metadatos_proyecto.csv
    ├── metadatos_proyecto.json
    └── resumen_transformaciones.csv
```

El notebook `F2/F2_preprocesamiento.ipynb` implementa el flujo:

```text
Obtener → Explorar → Limpiar → Transformar → Escalar → Validar → Guardar
```

### Resultados verificados en F2

| Comprobación | Resultado |
| --- | --- |
| Dimensiones originales | 10.000 filas × 14 columnas |
| Valores faltantes | 0 |
| Duplicados exactos | 0 |
| Distribución de `Type` | L: 6.000; M: 2.997; H: 1.003 |
| Distribución del objetivo | Sin falla: 9.661; con falla: 339 |
| Atípicos según IQR | Velocidad: 418; torque: 69 |
| División estratificada | 8.000 registros de entrenamiento y 2.000 de prueba |
| Dimensiones finales | 9 columnas numéricas en cada conjunto |
| Validación | Sin nulos y con codificación One-Hot coherente |

La variable objetivo contiene un 3,39 % de fallas. Por ello, una evaluación posterior no deberá depender únicamente de exactitud; será necesario considerar sensibilidad, precisión, F1 y otras métricas adecuadas.

### Decisiones implementadas en F2

| Decisión | Justificación |
| --- | --- |
| Mantener `F1/data/raw/ai4i2020.csv` sin cambios. | Preservar una entrada verificable mediante SHA-256. |
| Guardar los resultados en `F2/data/processed/`. | Separar los productos procesados del archivo original. |
| No imputar ni eliminar filas. | No se encontraron nulos ni duplicados exactos. |
| Excluir `UDI` y `Product ID`. | Son identificadores y no condiciones operacionales. |
| Excluir TWF, HDF, PWF, OSF y RNF de los predictores. | Evitar fuga de información desde indicadores asociados con la falla. |
| Codificar `Type` mediante One-Hot. | Representar L, M y H sin asignar distancias numéricas artificiales. |
| Dividir antes de escalar. | Evitar que el conjunto de prueba participe en el ajuste. |
| Utilizar división estratificada. | Conservar aproximadamente la proporción de fallas. |
| Aplicar `RobustScaler`. | Reducir la influencia de valores extremos sin eliminarlos. |

### Entorno verificado

| Componente | Versión utilizada |
| --- | --- |
| Python | 3.13.0 |
| NumPy | 2.5.3 |
| pandas | 3.0.5 |
| Matplotlib | 3.11.2 |
| scikit-learn | 1.9.1 |

El listado completo se conserva en `requirements.txt`.

### Orden actualizado de ejecución

| Orden | Notebook | Función |
| --- | --- | --- |
| 1 | `F1/notebooks/F1_Definicion.ipynb` | Define la problemática, objetivos, alcance y entorno reproducible. |
| 2 | `F1/notebooks/validador.ipynb` | Perfila el archivo y valida requisitos y roles analíticos. |
| 3 | `F2/F2_preprocesamiento.ipynb` | Ejecuta obtención, exploración, limpieza, transformación, escalamiento, validación y persistencia. |

Para exportar la Fase 2 a HTML desde la raíz del repositorio:

```powershell
python -m jupyter nbconvert --to html "F2/F2_preprocesamiento.ipynb" --output-dir "F2/docs"
```

Antes de compartir resultados, ejecutar cada notebook mediante **Kernel → Restart Kernel and Run All Cells** y guardar la versión sin errores.

### Vinculación actualizada con el mapa conceptual

| Elemento del mapa | Implementación | Evidencia |
| --- | --- | --- |
| Delimitar el problema | Problemática, pregunta, objetivos, alcance y limitaciones | Notebook F1 |
| Preparar el entorno | `.venv`, dependencias, semilla y versiones | `requirements.txt` y notebooks |
| Preservar los datos | Original en F1 y derivados en F2 | Carpetas `raw/` y `processed/` |
| Validar y describir | Tipos, nulos, duplicados, rangos, categorías y objetivo | Notebooks y `docs/` |
| Limpiar y transformar | Selección, casting, One-Hot y RobustScaler | Notebook F2 |
| Verificar el código | Casos normales, límite y excepciones | Apartado 6 de F2 |
| Documentar evidencia | Diccionarios, metadatos, resúmenes y HTML | `F1/docs/` y `F2/docs/` |
| Controlar versiones | Commits descriptivos y repositorio GitHub | Historial de Git |
| Modelar y comunicar | Trabajo proyectado | Fases 3 y 4 |

### Estado actualizado

#### Fase 1

- [x] Problemática, pregunta, objetivos, alcance y limitaciones.
- [x] Entorno reproducible y estructura del repositorio.
- [x] Dataset, diccionario y evaluación de criterios.
- [x] Mapa conceptual, metadatos y documentación.
- [x] Notebook ejecutado y exportado.

#### Fase 2

- [x] Obtención y exploración inicial.
- [x] Limpieza y selección de variables.
- [x] Codificación One-Hot y escalamiento.
- [x] División estratificada de entrenamiento y prueba.
- [x] Validación técnica y pruebas de funciones.
- [x] Persistencia de datasets y documentación.
- [x] Notebook ejecutado sin errores y exportado a HTML.
- [ ] Registro de F2 mediante commit y envío a GitHub.
- [ ] Informe técnico integrado de F1 y F2 en PDF.

### Colaboración y contribución individual

El desarrollo actual corresponde a un solo integrante. Los commits configurados con su nombre y correo constituyen la evidencia individual. En un equipo, el flujo equivalente incorporaría ramas, revisión de cambios y resolución de conflictos antes de integrar a `main`. No se atribuyen contribuciones a personas inexistentes.



### Referencias técnicas complementarias

JupyterLab. (s. f.). *JupyterLab documentation*. https://jupyterlab.readthedocs.io/

pandas development team. (s. f.). *pandas documentation*. https://pandas.pydata.org/docs/

scikit-learn developers. (s. f.). *Preprocessing data*. https://scikit-learn.org/stable/modules/preprocessing.html

# Fase 3 Núcleo algorítmico eficiencia y programación orientada a objetos

## Propósito de la fase

Esta fase toma el preprocesamiento construido en la Fase 2 y lo reorganiza como una solución modular. Los datos y las reglas de transformación se mantienen; el cambio principal está en la arquitectura del código.

El trabajo permite que cada tarea tenga una responsabilidad clara, que los pasos puedan probarse por separado y que el pipeline pueda ampliarse sin concentrar toda la lógica en una sola celda del notebook.

## Punto de partida

La fase utiliza los siguientes archivos:

- `F1/data/raw/ai4i2020.csv`: conjunto original con 10.000 filas y 14 columnas.
- `F2/data/processed/ai4i2020_entrenamiento_procesado.csv`: referencia de entrenamiento con 8.000 filas y 9 columnas.
- `F2/data/processed/ai4i2020_prueba_procesado.csv`: referencia de prueba con 2.000 filas y 9 columnas.

La variable objetivo es `Machine failure`. Los predictores son `Type` y cinco variables operacionales. `UDI` y `Product ID` se excluyen por ser identificadores. TWF, HDF, PWF, OSF y RNF se excluyen porque informan directamente modos de falla y podrían causar fuga de información.

## Estructura

```text
F3/
├── S2_F3_NucleoAlgoritmico_Eficiencia_POO.ipynb
├── README.md
├── data/
│   └── processed/
│       ├── ai4i2020_entrenamiento_procesado.csv
│       ├── ai4i2020_prueba_procesado.csv
│       ├── diccionario_f3.csv
│       └── parametros_f3.csv
├── docs/
│   ├── arquitectura_fase3.csv
│   ├── comparacion_eficiencia.csv
│   ├── crecimiento_temporal.csv
│   ├── metadatos_fase3.csv
│   └── metadatos_fase3.json
└── src/
    ├── __init__.py
    ├── carga.py
    ├── fabrica.py
    ├── medicion.py
    ├── pipeline.py
    └── transformadores.py
```

## Qué hace cada módulo

| Archivo | Función dentro del proyecto |
| --- | --- |
| `carga.py` | Busca la raíz del repositorio, lee los CSV y comprueba que los archivos tengan contenido. |
| `transformadores.py` | Contiene la clase base y las clases que codifican `Type` y escalan las variables operacionales. |
| `pipeline.py` | Ejecuta los transformadores en el orden definido y controla que hayan sido ajustados. |
| `fabrica.py` | Crea el transformador adecuado según el tipo de variable. |
| `medicion.py` | Mide tiempo de ejecución y memoria máxima. |
| Notebook | Reúne explicación, pruebas, comparaciones, resultados y conclusiones. |

## Flujo aplicado

```text
Cargar datos
    ↓
Separar predictores y objetivo
    ↓
Dividir entrenamiento y prueba con estratificación
    ↓
Ajustar el pipeline solo con entrenamiento
    ↓
Codificar Type con One Hot Encoding
    ↓
Escalar variables operacionales con RobustScaler
    ↓
Aplicar los parámetros aprendidos al conjunto de prueba
    ↓
Comparar los resultados con la Fase 2
    ↓
Guardar datos y evidencia
```

La separación entre `ajustar` y `transformar` es necesaria para que las categorías, medianas e IQR se aprendan únicamente desde entrenamiento. De esta manera, la prueba no participa en la preparación de los parámetros.

## Conceptos aplicados

### Herencia

`CodificadorOneHot` y `EscaladorRobusto` heredan de `Transformador`. La clase base concentra las comprobaciones que comparten todos los pasos y las clases hijas implementan su transformación específica.

### Polimorfismo

`Pipeline` llama a `ajustar()` y `transformar()` de la misma manera para cada objeto. Cada clase responde a esos métodos según su propia responsabilidad.

### Encapsulamiento

Los atributos `_parametros`, `_ajustado` y `_pasos` representan estado interno. Antes de transformar, las clases verifican que el ajuste ya se haya realizado y generan una excepción clara si el orden es incorrecto.

### Cohesión y acoplamiento

Cada módulo tiene una tarea concreta, lo que mejora la cohesión. El pipeline trabaja mediante una interfaz común y no necesita conocer los detalles de cada transformador, lo que reduce el acoplamiento.

### Patrón Factory

`FabricaTransformadores` recibe el tipo de variable y crea el objeto correspondiente. La fábrica centraliza esta decisión y permite agregar otra clase de transformación sin cambiar la lógica que recorre el pipeline.

### División funcional

Se utilizó división funcional porque el problema se resuelve naturalmente como una secuencia de pasos. No se forzó recursividad, ya que los datos no presentan una estructura anidada que la justifique.

## Validaciones realizadas

Se comprobaron tres clases de situaciones:

1. **Caso normal:** el pipeline procesa entrenamiento y prueba con las dimensiones esperadas.
2. **Caso límite:** se validan entradas pequeñas y configuraciones mínimas sin alterar indebidamente los datos.
3. **Excepciones:** se comprueba la respuesta ante columnas inexistentes, categorías desconocidas, transformación antes del ajuste y parámetros inválidos.

La verificación principal utiliza `pandas.testing.assert_frame_equal` para comparar los resultados de F3 con los CSV generados en F2. La comparación confirmó que la reorganización del código no alteró el resultado.

## Resultados de eficiencia

La medición usa `timeit` para el tiempo y `tracemalloc` para la memoria máxima. Los valores de la ejecución guardada fueron:

| Implementación | Tiempo promedio | Tiempo mínimo | Memoria máxima |
| --- | ---: | ---: | ---: |
| Funcional | 0,01327 s | 0,01153 s | 0,663 MiB |
| POO modular | 0,03732 s | 0,03517 s | 1,239 MiB |

La implementación funcional fue más rápida y utilizó menos memoria en este conjunto. La alternativa orientada a objetos se mantuvo como arquitectura de F3 porque permite separar responsabilidades, conservar parámetros, reutilizar componentes y detectar errores con mayor claridad. Las mediciones pueden variar al repetir el notebook porque dependen de la carga del computador.

La prueba con 1.000, 5.000, 10.000 y 20.000 filas mostró un crecimiento compatible con recorridos lineales. Debido a que las ejecuciones son breves, esta conclusión se interpreta como una aproximación y no como una demostración matemática.

## Productos generados

- Cuatro CSV de transición en `F3/data/processed/`: entrenamiento, prueba, diccionario y parámetros.
- Una tabla de arquitectura.
- Una comparación de eficiencia.
- Una tabla de crecimiento temporal.
- Metadatos en formatos CSV y JSON.
- Nueve archivos generados y verificados en total.
- Un notebook con 31 celdas de código ejecutadas en orden continuo y sin errores.
- El informe `f3_s02_entregable_grupo9.pdf` y su versión editable en la raíz del repositorio.

## Cómo reproducir la fase

Desde la raíz del repositorio, con el entorno virtual activado:

```powershell
python -m jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=900 "F3/S2_F3_NucleoAlgoritmico_Eficiencia_POO.ipynb"
```

También puede abrirse el notebook en JupyterLab y ejecutar **Kernel → Restart Kernel and Run All Cells**. Al terminar deben aparecer las verificaciones finales con estado `[OK]`.

## Limitaciones

AI4I 2020 es un conjunto sintético sin valores faltantes ni duplicados. Por esta razón, la fase conserva las decisiones justificadas en F2 y no inventa problemas de calidad. La equivalencia con F2 confirma la corrección de la reorganización, pero no demuestra que el pipeline generalice a datos industriales reales.

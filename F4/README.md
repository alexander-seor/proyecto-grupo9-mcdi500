# Fase 4 — Análisis, reproducibilidad y comunicación

Esta fase integra los productos de F1, F2 y F3 para cerrar el análisis del
conjunto AI4I 2020. El notebook recupera categorías y unidades originales,
comprueba que las 10.000 observaciones se conservaron, construye las figuras
principales y documenta los límites de la interpretación.

## Propósito

La Fase 4 responde de forma descriptiva la pregunta del proyecto: qué
condiciones operacionales aparecen asociadas con una mayor frecuencia de
fallas. No se entrena un clasificador y, por lo tanto, no se reporta capacidad
predictiva.

## Entradas utilizadas

El notebook recibe cuatro productos de F3:

| Archivo | Función |
| --- | --- |
| `F3/data/processed/ai4i2020_entrenamiento_procesado.csv` | Matriz de entrenamiento transformada. |
| `F3/data/processed/ai4i2020_prueba_procesado.csv` | Matriz de prueba transformada. |
| `F3/data/processed/diccionario_f3.csv` | Descripción de las variables resultantes. |
| `F3/data/processed/parametros_f3.csv` | Medianas, IQR y categorías aprendidas en entrenamiento. |

El archivo `F1/data/raw/ai4i2020.csv` se utiliza como referencia para comprobar
que la reconstrucción mantiene las mismas filas, aunque estén en otro orden.

## Productos de F4

```text
F4/
├── F4_Consolidado_Proyecto.ipynb
├── README.md
├── presentacion_f4_grupo9.pptx
├── data/
│   └── processed/
│       └── ai4i2020_visualizacion.csv
├── docs/
│   ├── interaccion_operacional.csv
│   ├── mapa_objetivos_figuras.csv
│   ├── metadatos_fase4.json
│   ├── resumen_objetivo.csv
│   ├── resumen_variables_operacionales.csv
│   ├── tasas_quintiles.csv
│   ├── tasas_tipo_producto.csv
│   ├── trazabilidad_mejoras.csv
│   └── validacion_perfil.csv
└── figuras/
    ├── figura_0_balance_objetivo.png
    ├── figura_1_tasa_por_tipo.png
    ├── figura_2_tasas_por_quintiles.png
    └── figura_3_interaccion_operacional.png
```

La figura 0 documenta el desbalance y sirve de apoyo. Las figuras 1, 2 y 3
forman el relato principal de contexto, contraste y resolución.

## Resultados verificados

- Se conservaron 10.000 registros, 339 fallas y cero valores faltantes nuevos.
- La tasa global de falla es 3,39 %.
- El tipo L presenta 3,92 %, frente a 2,77 % en M y 2,09 % en H.
- Las tasas más altas por quintil aparecen con velocidad baja (12,16 %) y
  torque alto (11,50 %).
- Los cortes del perfil combinado se calcularon solo con entrenamiento:
  velocidad de hasta 1.422 rpm, torque superior a 46,8 Nm y desgaste de al
  menos 174 minutos.
- El perfil registra 28,94 % en entrenamiento y 27,50 % en prueba. El resto
  registra 2,48 % y 2,40 %, respectivamente.

Estas cifras describen AI4I 2020. No demuestran causalidad, no corresponden a
umbrales industriales y no constituyen métricas de predicción.

## Cómo ejecutar

Desde la raíz del repositorio, activar el entorno e instalar las dependencias:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Abrir JupyterLab:

```powershell
python -m jupyterlab
```

Abrir `F4/F4_Consolidado_Proyecto.ipynb`, seleccionar el intérprete de `.venv`
y utilizar **Restart Kernel and Run All Cells**. La ejecución validada contiene
20 celdas de código numeradas en forma continua y ninguna salida de error.

También puede ejecutarse desde la terminal:

```powershell
python -m jupyter nbconvert --to notebook --execute --inplace `
  --ExecutePreprocessor.timeout=900 "F4/F4_Consolidado_Proyecto.ipynb"
```

## Controles incluidos

- entorno virtual, versiones y semilla;
- disponibilidad y estructura de las cuatro entradas de F3;
- evidencia de pruebas, equivalencia y eficiencia de F3;
- inversión de `RobustScaler` y reconstrucción de `Type`;
- equivalencia de las siete variables analíticas con F1;
- generación de tablas, metadatos y cuatro figuras;
- validación descriptiva del perfil en entrenamiento y prueba;
- verificación final calculada desde los archivos producidos.

## Limitaciones

- AI4I 2020 es sintético y no representa una planta específica.
- La clase de falla corresponde solo al 3,39 % de los registros.
- Los cortes son cuantiles descriptivos aprendidos desde este conjunto.
- El perfil se definió después de la exploración.
- No se estimó desempeño predictivo ni causalidad.

## Entregables finales preparados

- `../informe_f4_grupo9.docx`: versión editable del informe final.
- `../informe_f4_grupo9.pdf`: informe final de 10 páginas.
- `presentacion_f4_grupo9.pptx`: presentación de 8 diapositivas para apoyar el video.

La presentación resume el problema, la continuidad entre las fases, las tres
figuras principales, la validación descriptiva y las conclusiones. El video de
Canvas Studio debe ser grabado y publicado por el autor utilizando estos
materiales.

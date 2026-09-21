# Validación del dataset — MCDI500

**Archivo:** `ai4i2020.csv` · 10000 filas × 14 columnas

## Perfil de variables

| variable | dtype | rol | unicos | pct_nulos |
| --- | --- | --- | --- | --- |
| ﻿UDI | int64 | identificador | 10000 | 0.0 |
| Product ID | str | identificador | 10000 | 0.0 |
| Type | str | nominal | 3 | 0.0 |
| Air temperature [K] | float64 | continua | 93 | 0.0 |
| Process temperature [K] | float64 | continua | 82 | 0.0 |
| Rotational speed [rpm] | int64 | continua | 941 | 0.0 |
| Torque [Nm] | float64 | continua | 577 | 0.0 |
| Tool wear [min] | int64 | discreta | 246 | 0.0 |
| Machine failure | int64 | binaria | 2 | 0.0 |
| TWF | int64 | binaria | 2 | 0.0 |
| HDF | int64 | binaria | 2 | 0.0 |
| PWF | int64 | binaria | 2 | 0.0 |
| OSF | int64 | binaria | 2 | 0.0 |
| RNF | int64 | binaria | 2 | 0.0 |

## Requisitos del curso

| estado | requisito | detalle |
| --- | --- | --- |
| OK | Al menos 2000 filas | 10000 filas |
| OK | Al menos 12 columnas | 14 columnas |
| OK | Combina al menos 3 roles analíticos | binaria, continua, nominal, discreta |
| OK | Al menos una variable numérica | 5 numéricas (continuas o discretas) |
| OK | Al menos una variable categórica | 7 categóricas (nominales, binarias u ordinales) |
| AVISO | Presencia de valores faltantes | máximo 0.0% en una variable |
| OK | Ninguna variable sobre 60% de faltantes | máximo 0.0% |
| AVISO | Incluye alguna variable de fecha | 0 detectadas |
| AVISO | Incluye texto o categórica de alta cardinalidad | 0 detectadas |
| OK | Archivo bajo 100 MB | 0.5 MB |
| OK | Sin filas duplicadas exactas | ninguna |

## Resultado

El conjunto **cumple** los requisitos mínimos.
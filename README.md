# Proyecto MCDI500 — Análisis de Datos

Proyecto desarrollado para la asignatura Programacion para la ciencia orientado al desarrollo de un proceso de análisis de datos reproducible y documentado.

## Descripción

El proyecto utiliza el dataset **AI4I 2020 Predictive Maintenance Dataset**, que contiene información relacionada con las condiciones operacionales de máquinas y la ocurrencia de fallas.

El trabajo busca aplicar las distintas etapas de un proyecto de análisis de datos, desde la comprensión y validación inicial del conjunto de datos hasta su posterior análisis y modelamiento.

## Estructura del proyecto

```text
proyecto-grupo9-mcdi500/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── F1/
│   ├── data/
│   │   ├── raw/
│   │   └── processed/
│   ├── notebooks/
│   ├── docs/
│   └── src/
│
├── F2/
├── F3/
└── F4/
```

### Carpetas principales

- `data/raw/`: datos originales sin modificar.
- `data/processed/`: datos procesados durante el análisis.
- `notebooks/`: notebooks utilizados para exploración y análisis.
- `docs/`: documentación e informes generados.
- `src/`: código reutilizable del proyecto.

## Dataset

Se utiliza el **AI4I 2020 Predictive Maintenance Dataset**.

Entre sus variables se encuentran:

- UDI
- Product ID
- Type
- Air temperature [K]
- Process temperature [K]
- Rotational speed [rpm]
- Torque [Nm]
- Tool wear [min]
- Machine failure

Durante la etapa inicial se realizó una revisión de las variables y su clasificación según su naturaleza.

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
- [ ] Análisis exploratorio de datos.
- [ ] Preparación de los datos.
- [ ] Conclusiones de la Formativa 1.

## Reproducibilidad

Crear el entorno virtual:

```bash
python -m venv .venv
```

Activarlo en Windows:

```bash
.venv\Scripts\activate
```

Instalar las dependencias:

```bash
python -m pip install -r requirements.txt
```

Las dependencias utilizadas en el proyecto se registran en `requirements.txt`.

## Flujo de trabajo

El proyecto utiliza Git para el control de versiones.

Los cambios se registran localmente mediante commits y posteriormente se sincronizan con el repositorio remoto.

```bash
git status
git add .
git commit -m "Descripción del cambio"
git push
```

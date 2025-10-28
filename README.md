# Importancia Data Visualization

## Portada

**Universidad Politécnica Salesiana**  
**Carrera:** Ingeniería en Ciencias de la Computación
**Período:** 67  
**Estudiante:** Juan Javier Malo Vega
**Asignatura:** Minería de Datos 

---

## Introducción Teórica al Cuarteto de Anscombe

### ¿Qué es el Cuarteto de Anscombe?

El Cuarteto de Anscombe es un conjunto de cuatro conjuntos de datos que tienen propiedades estadísticas prácticamente idénticas, pero que al ser graficados revelan formas completamente diferentes. Fue creado por el estadístico Francis Anscombe en 1973 para demostrar la importancia de la visualización de datos antes de realizar análisis estadísticos.

### Características de los Cuartetos

Los cuatro conjuntos de datos comparten las siguientes propiedades estadísticas:

- **Media de X:** 9.0
- **Varianza de X:** 11.0
- **Media de Y:** 7.5
- **Varianza de Y:** 4.125
- **Correlación entre X e Y:** 0.816
- **Ecuación de regresión lineal:** Y = 3.00 + 0.500X
- **Coeficiente de determinación (R²):** 0.67

### Los Cuatro Conjuntos de Datos

1. **Conjunto I:** Datos con distribución normal y relación lineal clara
2. **Conjunto II:** Datos con relación no lineal (curva)
3. **Conjunto III:** Datos con relación lineal pero con un valor atípico (outlier)
4. **Conjunto IV:** Datos donde X es constante excepto por un valor atípico

### Importancia de la Visualización

El Cuarteto de Anscombe ilustra perfectamente por qué es crucial visualizar los datos antes de confiar únicamente en estadísticas descriptivas. Aunque los cuatro conjuntos tienen estadísticas idénticas, sus patrones visuales son completamente diferentes, lo que demuestra que:

- Las estadísticas descriptivas pueden ser engañosas
- La visualización de datos es esencial para el análisis exploratorio
- Un análisis estadístico completo debe incluir tanto números como gráficos

### Referencias

- Anscombe, F. J. (1973). "Graphs in Statistical Analysis". *The American Statistician*, 27(1), 17-21.
- Tufte, E. R. (2001). *The Visual Display of Quantitative Information*. Graphics Press.

---

## Estructura del Repositorio

```
Importancia-Data-Visualization/
├── README.md                    # Este archivo
├── data/                       # Conjuntos de datos utilizados
│   ├── df_anscombe.csv        # Dataset del Cuarteto de Anscombe
│   └── README.md              # Documentación de los datos
├── R/                         # Código R para análisis (Datasaurus Dozen)
│   ├── regresion_simple.Rmd   # Regresión lineal con "high_lines"
│   └── regresion_simple.html  # Reporte HTML generado
└── Python/                    # Código Python para regresión lineal (Anscombe)
    ├── linear_regression_analysis.py  # Análisis del Cuarteto de Anscombe
    ├── tests.ipynb            # Notebook de pruebas
    ├── tests.py               # Script de pruebas
    └── requirements.txt       # Dependencias de Python
```

---

## Descripción de Secciones

### 📁 Directorio `data/`
Contiene todos los conjuntos de datos utilizados para la práctica, incluyendo el dataset del Cuarteto de Anscombe con los 4 conjuntos de datos originales.

### 📁 Directorio `R/`
Almacena el código R utilizado para realizar regresión lineal con el dataset "high_lines" del Datasaurus Dozen, incluyendo visualizaciones y análisis estadísticos.

### 📁 Directorio `Python/`
Contiene el código Python utilizado para realizar regresión lineal con el Cuarteto de Anscombe, implementando algoritmos de machine learning y análisis estadístico.

---

## Objetivos del Proyecto

1. Demostrar la importancia de la visualización de datos
2. Implementar análisis estadísticos en R
3. Realizar regresión lineal en Python
4. Comparar diferentes conjuntos de datos con estadísticas similares
5. Crear visualizaciones efectivas para comunicar hallazgos

---

## Tecnologías Utilizadas

- **R:** Análisis estadístico y visualización
- **Python:** Machine learning y regresión lineal
- **GitHub:** Control de versiones y colaboración
- **Markdown:** Documentación del proyecto
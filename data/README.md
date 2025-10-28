# Datos - Cuarteto de Anscombe

Este directorio contiene todos los conjuntos de datos utilizados para la práctica de visualización de datos.

## Archivos incluidos

### `df_anscombe.csv`
Dataset principal del Cuarteto de Anscombe con los 4 conjuntos de datos originales:
- **Columnas**: x, y, group
- **Filas**: 44 (11 por cada conjunto)
- **Grupos**: 4 conjuntos de datos con estadísticas idénticas pero patrones visuales diferentes

### Estructura de los datos

| Columna | Descripción | Tipo |
|---------|-------------|------|
| x | Variable independiente | numérico |
| y | Variable dependiente | numérico |
| group | Identificador del conjunto (1-4) | entero |

## Características de los conjuntos

### Conjunto 1: Relación lineal clara
- Datos con distribución normal
- Relación lineal evidente
- Sin valores atípicos

### Conjunto 2: Relación no lineal
- Datos con patrón curvilíneo
- Relación no lineal (curva)
- Estadísticas idénticas al Conjunto 1

### Conjunto 3: Valor atípico
- Relación lineal con un outlier
- Un punto se desvía significativamente
- Estadísticas idénticas a los otros conjuntos

### Conjunto 4: X constante con outlier
- Variable X constante excepto por un valor
- Patrón vertical con un punto atípico
- Estadísticas idénticas a los otros conjuntos

## Estadísticas compartidas

Todos los conjuntos comparten las siguientes propiedades estadísticas:

- **Media de X**: 9.0
- **Varianza de X**: 11.0
- **Media de Y**: 7.5
- **Varianza de Y**: 4.125
- **Correlación**: 0.816
- **R²**: 0.67
- **Ecuación de regresión**: Y = 3.00 + 0.500X

## Uso de los datos

Estos datos son ideales para:
- Demostrar la importancia de la visualización
- Enseñar análisis exploratorio de datos
- Mostrar limitaciones de las estadísticas descriptivas
- Practicar regresión lineal
- Crear visualizaciones efectivas

## Referencias

- Anscombe, F. J. (1973). "Graphs in Statistical Analysis". *The American Statistician*, 27(1), 17-21.
- Datos originales disponibles en: https://en.wikipedia.org/wiki/Anscombe%27s_quartet

# 05/09/2025
# Utilizando la misma base de micro-datos de la clase pasada:
# 1 - Analizar la columna P21 y responder:
# a - ¿Existen valores perdidos o no respuesta?
# b - ¿Cómo se trabajan? analizar los ponderadores existentes.
# c - Imputar la P21 utilizando la media
# 2- Evaluar si existen valores atípicos. ¿Qué opina que se debería hacer con ellos?
# 3 - Realizar transformaciones sobre la edad.

import pandas as pd

# Cargamos la base individual
df = pd.read_csv("usu_individual_T324.txt", sep=";", encoding="latin1", low_memory=False)

print("Ejercicio 1: Análisis de la columna P21")
# a) Ver si hay valores perdidos o no respuesta
# Resumen de P21
print(df["P21"].describe())     # estadísticas básicas
print("\nValores perdidos en P21:", df["P21"].isna().sum()) #cuenta cuántos registros faltan.
print("a) Total de filas:", len(df))

# b) Cómo trabajar los valores perdidos (ponderadores)
media_ponderada = (df["P21"] * df["PONDIIO"]).sum() / df["PONDIIO"].sum()
print("b) Media ponderada de P21:", media_ponderada)

# c) Imputar P21 usando la media
# reemplazar los valores faltantes con la media ponderada
df["P21"].fillna(media_ponderada, inplace=True)
print("c) Valores perdidos en P21 después de imputar:", df["P21"].isna().sum())

print("*****************************************************")

print("Ejercicio 2: Evaluación de valores atípicos en P21")
Q1 = df["P21"].quantile(0.25)
Q3 = df["P21"].quantile(0.75)
IQR = Q3 - Q1

# Definimos umbrales
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

outliers = df[(df["P21"] < limite_inferior) | (df["P21"] > limite_superior)]
print("Cantidad de outliers:", len(outliers))

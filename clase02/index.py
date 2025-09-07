# 29/08/2025
# Ejercicios de repaso
# 1- Abrir con pandas la base de microdatos de la encuesta permanente de hogares del tercer
# trimestre de 2024.
# Link:
# https://www.indec.gob.ar/ftp/cuadros/menusuperior/eph/EPH_usu_3_Trim_2024_txt.zip
# https://www.indec.gob.ar/ftp/cuadros/menusuperior/eph/EPH_registro_3T2024.pdf (para entender las variables)
# 2- Analizar el data frame y responder:
# a- ¿Cuántas columnas tiene?
# b- ¿Cuántas filas tiene?
# c- ¿Qué tipos de columnas tiene?
# 3- ¿Puede detectar alguna columna índice?


import pandas as pd
from pathlib import Path

# selecciono los archivos a analizar
FILE_HOGAR = "./usu_hogar_T324.txt"
FILE_INDIV = "./usu_individual_T324.txt"

def leer_txt(path):
    # Paso el archivo y devuelve un DataFrame de pandas con los datos listos para analizar
    return pd.read_csv(path, sep=";", encoding="latin1", low_memory=False) 

def analizar_df(df, nombre, tipo):
    print(f"\n=== {nombre} ===")
    # (a) ¿Cuántas columnas?
    print("Columnas:", df.shape[1]) #df.shape devuelve (filas, columnas). El índice 1 es columnas
    # (b) ¿Cuántas filas?
    print("Filas:", df.shape[0])
    # (c) ¿Qué tipos de columnas?
    print("\nTipos (conteo por dtype):")
    print(df.dtypes.value_counts()) #df.dtypes devuelve una Serie con los tipos de cada columna. value_counts() cuenta cuántas veces aparece cada tipo

    # Mostrar algunos nombres de columnas para ubicarte
    print("\nPrimeras 10 columnas:")
    print(list(df.columns[:10])) # toma las primeras 10 (slicing). list() convierte el Index a lista para que se vea mejor

    # 3) ¿Columna índice (clave única)?
    # Claves típicas EPH:
    # - Hogar: CODUSU + NRO_HOGAR
    # - Individual: CODUSU + NRO_HOGAR + COMPONENTE
    claves = {
        "hogar": ["CODUSU", "NRO_HOGAR"],
        "individual": ["CODUSU", "NRO_HOGAR", "COMPONENTE"]
    }
    if tipo in claves and set(claves[tipo]).issubset(df.columns): #issubset(df.columns) checa que todas las columnas necesarias existen en el DataFrame.
        clave = claves[tipo]
        es_unica = not df.duplicated(subset=clave).any() #devuelve una Serie booleana marcando como True las filas repetidas según esa combinación de columnas.  any() devuelve True si hay al menos un True en la Serie, es decir, si hay duplicados. El not invierte el resultado.
        if es_unica:
            # Si no hay duplicados, la combinación puede funcionar como índice único (clave primaria).
            print(f"\n✅ Candidata a índice única: {clave}")
        else:
            dups = df.duplicated(subset=clave).sum() #duplicated().sum() cuenta las repeticiones extra (no cuenta la primera aparición).
            print(f"\n⚠️ La combinación {clave} NO es única (duplicados: {dups}).")
    else:
        print("\n⚠️ No se encontraron todas las columnas clave esperadas para este tipo.")

# Leer y analizar
df_hogar = leer_txt(FILE_HOGAR) # me crea un DataFrame de pandas para pasarle a la función analizar_df
analizar_df(df_hogar, "HOGAR (usu_hogar_T324.txt)", "hogar")

df_indiv = leer_txt(FILE_INDIV)
analizar_df(df_indiv, "INDIVIDUAL (usu_individual_T324.txt)", "individual")
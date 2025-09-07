# NumPy es una biblioteca de Python que permite realizar cálculos numéricos de manera eficiente, especialmente con arreglos multidimensionales. (Se instalo con "pip install numpy")

# COLAB PROFESOR:    https://colab.research.google.com/drive/1x-5Rp6Erfq18CL7-0ANoI4189KSpoTMt?usp=sharing#scrollTo=c5dgRGgHeO1S

import numpy as np
import time

# Usando listas de Python
lista = list(range(10 ** 6))
inicio = time.time()
lista_cuadrados = [x ** 2 for x in lista]
dif_py = time.time() - inicio
print("Tiempo con listas:", dif_py)

# Usando NumPy
array = np.arange(10 ** 6) #constructor
inicio = time.time()
array_cuadrados = array ** 2 #No requiere bucle
dif_np = time.time() - inicio
print("Tiempo con NumPy:", dif_np)
print("Diferencia relativa: ", dif_py/dif_np)

print("*************************************")

# EJERCICIO: Utilizando la ley de los grandes numeros deberiamos acceder a una media que sea relativamente cercana. No deberiamos tener tanta variabilididad en la diferencia relativa.

repeticiones = 30
suma_py = 0
suma_np = 0

for i in range(repeticiones):
    # Usando listas
    lista = list(range(10**6))
    inicio = time.time()
    lista_cuadrados = [x ** 2 for x in lista]
    dif_py = time.time() - inicio
    suma_py += dif_py

    # Usando NumPy
    array = np.arange(10**6)
    inicio = time.time()
    array_cuadrados = array ** 2
    dif_np = time.time() - inicio
    suma_np += dif_np

    print(f"Medición {i+1}: listas={dif_py:.4f}s | NumPy={dif_np:.4f}s")

# Calcular promedios
prom_py = suma_py / repeticiones
prom_np = suma_np / repeticiones
relativa = prom_py / prom_np

print("\n--- Resultados Finales ---")
print(f"Tiempo promedio listas: {prom_py} segundos")
print(f"Tiempo promedio NumPy:  {prom_np} segundos")
print(f"Diferencia relativa promedio: {relativa}x")
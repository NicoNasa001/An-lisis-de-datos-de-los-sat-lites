import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("Satelites.xlsx") # Importacion del archivo

df = df.dropna() # Limpieza de espacios en blanco
# Definicion de las columnas numericas
df["Edad"] = df["Edad"].astype(int)
df["Km/h"] = df["Km/h"].astype(int)

print(df.head()) # Muestara de los dtos en un cuadro comparativo

print(df["Km/h"].mean()) # Pormediode los km/h

print(df[df["Km/h"] == df["Km/h"].max()]) # Cual satelite tiene más km/h
# Grafico de barras
plt.bar(df["Nombre"], df["Km/h"]) # Bara de datos
plt.title("Kilometros por hora por satelite") # Nombre
plt.xlabel("Nombre") # Eje x
plt.ylabel("Km/h") # Eje y
plt.show() # Mostrar el grafico
# Grafico de barras
plt.bar(df["Nombre"], df["Edad"])
plt.title("Edades de lanzamiento")
plt.xlabel("Nombre")
plt.ylabel("Edad")
plt.show()
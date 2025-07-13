import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') 
from sklearn.linear_model import LinearRegression
import numpy as np

class Visualizer:
    def __init__(self, datos):
        self.datos = datos

    def generar_dispersion(self):
        try:
            datos = self.datos.copy()
            datos = datos.dropna(subset=['precio', 'area'])

            plt.figure(figsize=(10, 6))
            plt.scatter(datos['area'], datos['precio'], alpha=0.6, c='teal', edgecolors='k', label='Datos reales')

            X = datos[['area']]
            y = datos['precio']
            modelo = LinearRegression()
            modelo.fit(X, y)

            x_line = np.linspace(X['area'].min(), X['area'].max(), 100).reshape(-1, 1)
            y_line = modelo.predict(x_line)

            plt.plot(x_line, y_line, color='red', linewidth=2, label='Línea de Regresión')
            plt.title("Diagrama de Dispersión: Precio vs Área con línea de regresión")
            plt.xlabel("Área (m2)")
            plt.ylabel("Precio")
            plt.legend()
            plt.grid(True)

            plt.savefig('static/dispersion.png')
            plt.close()
        except Exception as e:
            print(f"Error generando gráfico: {e}")
            
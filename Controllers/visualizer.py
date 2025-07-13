import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') 

class Visualizer:
    def __init__(self, ruta_datos):
        self.ruta_datos = ruta_datos

    def generar_dispersion(self):
        try:
            datos = pd.read_excel(self.ruta_datos, header=1, engine='openpyxl')
            datos['valor_m2'] = datos['precio'] / datos['area']

            plt.figure(figsize=(10, 6))
            plt.scatter(datos['precio'], datos['valor_m2'], alpha=0.6, c='teal', edgecolors='k')
            plt.title("Diagrama de Dispersión: Precio vs Valor por m2")
            plt.xlabel("Precio de la Vivienda")
            plt.ylabel("Valor por m2")
            plt.grid(True)
            plt.savefig('static/dispersion.png')
            plt.close()
        except Exception as e:
            print(f"Error generando gráfico: {e}")
            
import pandas as pd

class DataLoader:
    def __init__(self, ruta):
        self.ruta = ruta
        self.datos = None

    def cargar_datos(self):
        try:
            self.datos = pd.read_excel(self.ruta, header=1, engine='openpyxl')
            return self.datos
        except Exception as e:
            print(f"Error al cargar los datos: {e}")
            return None
        
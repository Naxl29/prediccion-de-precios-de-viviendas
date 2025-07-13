from Models.data_loader import DataLoader
from Models.statistics import Statistics
from Controllers.visualizer import Visualizer

class PredictorController:
    def __init__(self, ruta_dataset):
        self.ruta_dataset = ruta_dataset
        self.data_loader = DataLoader(ruta_dataset)
        self.statistics = Statistics()
        self.visualizer = Visualizer()

    def procesar_todo(self):
        datos = self.data_loader.cargar_excel()

        estadisticas = self.statistics.calcular_estadisticas(datos)

        self.visualizer.generar_dispersion(datos)

        return estadisticas
    
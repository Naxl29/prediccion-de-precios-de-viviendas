from Models.data_loader import DataLoader
from Models.statistics import Statistics
from Controllers.visualizer import Visualizer

class PredictorController:
    def __init__(self, ruta_dataset):
        self.ruta_dataset = ruta_dataset
        self.data_loader = DataLoader(ruta_dataset)
        self.datos = self.data_loader.cargar_datos()
        
    def procesar_todo(self):
        if self.datos is None:
            return {}
        
        estadisticas = Statistics(self.datos).calcular_estadisticas()
        Visualizer(self.datos).generar_dispersion()
        return estadisticas
    
    def _clasificador_tipo(self, desc):
        if isinstance(desc, str):
            if 'casa' in desc.lower():
                return 'Casa'
            elif 'apartamento' in desc.lower():
                return 'Apartamento'
        return 'Otro'
    
from Models.data_loader import DataLoader
from Models.statistics import Statistics
from Controllers.visualizer import Visualizer
from Models.model_trainer import ModelTrainer

class PredictorController:
    def __init__(self, ruta_dataset):
        self.ruta_dataset = ruta_dataset
        self.data_loader = DataLoader(ruta_dataset)
        self.datos = self.data_loader.cargar_datos()
        
        self.stat_calculator = None
        self.visualizer = None
        self.model_trainer = None

    def procesar_todo(self):
        """Carga datos, calcula estadísticas y grafica dispersión."""

        if self.datos is None:
            return {}

        self.stat_calculator = Statistics(self.datos)
        estadisticas = self.stat_calculator.calcular_estadisticas()

        self.visualizer = Visualizer(self.datos)
        self.visualizer.generar_dispersion()

        return estadisticas
    
    def entrenar_regresion(self):
        """Entrena el modelo de regresión y devuelve coeficientes y métricas."""
        if self.datos is None:
            return {}

        # Inicializa y entrena
        self.model_trainer = ModelTrainer(self.datos)
        resultados = self.model_trainer.entrenar_modelo()
        return resultados

    def _clasificador_tipo(self, desc):
        if isinstance(desc, str):
            if 'casa' in desc.lower(): return 'Casa'
            elif 'apartamento' in desc.lower(): return 'Apartamento'
        return 'Otro'
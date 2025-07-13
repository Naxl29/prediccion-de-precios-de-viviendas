from flask import Flask, render_template
import pandas as pd
from Controllers.predictor_controller import PredictorController
from Controllers.visualizer import Visualizer
import os

app = Flask(__name__)

ruta_dataset = r"dataset/dataset_viviendas.xlsx"

controlador = PredictorController(ruta_dataset)

@app.route('/')
def dashboard():
    """Dashboard principal"""
    try:
        estadisticas = controlador.procesar_todo()
        print ("Estadísticas calculadas correctamente.")
        return render_template('dashboard.html', **estadisticas)
    except Exception as e:
        print(f"Error en el dashboard: {e}")
        return render_template('dashboard.html')


@app.route('/tabla')
def mostrar_tabla():
    """Ruta para mostrar la tabla de datos"""
    try:
        datos = controlador.datos
        datos_html = datos.to_html(classes='table table-bordered', index=False)
        return render_template('tabla.html', tabla=datos_html)
    except Exception as e:
        print(f"Erro mostrando la tabla: {e}")
        return render_template('tabla.html')

@app.route('/resumen')
def resumen_estadistico():
    """Ruta para mostrar el resumen estadístico"""
    try:
        total = len(controlador.datos)
        promedio_m2 = (controlador.datos['precio'] / controlador.datos['area']).mean()
        conteo = controlador.datos['descripcion'].apply(controlador._clasificador_tipo).value_counts()
        return render_template('resumen.html', total=total, promedio_m2=round(promedio_m2, 2), conteo=conteo.to_dict())
    except Exception as e:
        print(f"Error en el resumen estadístico: {e}")
        return render_template('resumen.html')

@app.route('/grafico')
def mostrar_grafico():
    """Ruta para mostrar el gráfico de dispersión"""
    try:
        Visualizer(controlador.datos).generar_dispersion()
        return render_template('grafico.html')
    except Exception as e:
        print(f"Error generando gráfico: {e}")
        return render_template('grafico.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
import pandas as pd
from Controllers.predictor_controller import PredictorController
from Controllers.visualizer import Visualizer
from Models.conexion import Conexion
from Models.data_loader import DataLoader
import os

app = Flask(__name__)

conexion = Conexion()


controlador = PredictorController(conexion)

@app.route('/')
def dashboard():
    """Dashboard principal"""
    estadisticas = controlador.procesar_todo()
    return render_template('dashboard.html', **estadisticas)


@app.route('/tabla')
def mostrar_tabla():
    """Ruta para mostrar la tabla de datos"""
    datos_html = controlador.datos.to_html(classes='table table-bordered', index=False)
    return render_template('tabla.html', tabla=datos_html)

@app.route('/resumen')
def resumen_estadistico():
    """Ruta para mostrar el resumen estadístico"""
    total = len(controlador.datos)
    promedio_m2 = (controlador.datos['precio'] / controlador.datos['area']).mean()
    conteo = controlador.datos['descripcion'].apply(controlador._clasificador_tipo).value_counts()
    return render_template('resumen.html',
                           total=total,
                           promedio_m2=round(promedio_m2, 2),
                           conteo=conteo.to_dict())

@app.route('/grafico')
def mostrar_grafico():
    """Ruta para mostrar el gráfico de dispersión"""
    Visualizer(controlador.datos).generar_dispersion()
    return render_template('grafico.html')

@app.route('/modelo')
def mostrar_modelo():
    """Ruta para entrenar regresión lineal y mostrar métricas."""
    resultados = controlador.entrenar_regresion()
    return render_template('modelo.html', **resultados)

if __name__ == '__main__':
    app.run(debug=True)

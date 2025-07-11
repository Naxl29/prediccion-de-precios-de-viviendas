from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def mostrar_tabla():
    ruta = r"C:\laragon\www\PYTHON\prediccion-de-precios-de-viviendas\dataset\dataset_viviendas.xlsx"
    datos = pd.read_excel(ruta, index_col=0, engine='openpyxl')
    datos_html = datos.to_html(classes='table table-bordered', index=False)
    return render_template('tabla.html', tabla=datos_html)

if __name__ == '__main__':
    app.run(debug=True)

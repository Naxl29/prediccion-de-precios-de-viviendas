from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def mostrar_tabla():
    ruta = r"C:\laragon\www\PYTHON\prediccion-de-precios-de-viviendas\dataset\dataset_viviendas.xlsx"
    datos = pd.read_excel(ruta, index_col=0, engine='openpyxl')
    datos_html = datos.to_html(classes='table table-bordered', index=False)
    return render_template('tabla.html', tabla=datos_html)

@app.route('/resumen')
def resumen_estadistico():
    ruta = r"C:\laragon\www\PYTHON\prediccion-de-precios-de-viviendas\dataset\dataset_viviendas.xlsx"
    datos = pd.read_excel(ruta,  header=1, engine='openpyxl') 

    total_viviendas = len(datos)

    datos['precio_m2'] = datos['precio'] / datos['area']
    promedio_m2 = datos['precio_m2'].mean()

    def claficar_tipo(desc):
        if isinstance(desc, str):
            if 'casa' in desc.lower():
                return 'Casa'
            elif 'apartamento' in desc.lower():
                return 'Apartamento'
        return 'Otro'

    datos['tipo_vivienda'] = datos['descripcion'].apply(claficar_tipo)
    conteo_tipo = datos['tipo_vivienda'].value_counts()

    return render_template('resumen.html',
                           total=total_viviendas,
                           promedio_m2=round(promedio_m2, 2),
                            conteo=conteo_tipo.to_dict()
                            )

if __name__ == '__main__':
    app.run(debug=True)

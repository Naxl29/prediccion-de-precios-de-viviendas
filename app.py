from flask import Flask, render_template
import pandas as pd
from Controllers.grafico_dispersion import generar_dispersion
import os

app = Flask(__name__)

@app.route('/')
def dashboard():
    try:
        ruta = r"C:\laragon\www\PYTHON\prediccion-de-precios-de-viviendas\dataset\dataset_viviendas.xlsx"

        if os.path.exists(ruta):
            datos = pd.read_excel(ruta, header=1, engine='openpyxl')
            total_viviendas = len(datos)
            precio_promedio = datos['precio'].mean()
            area_promedio = datos['area'].mean()
            datos['precio_m2'] = datos['precio'] / datos['area']
            precio_m2_promedio = datos['precio_m2'].mean()

            def clasificar_tipo(desc):
                if isinstance(desc, str):
                    if 'casa' in desc.lower():
                        return 'Casa'
                    elif 'apartamento' in desc.lower():
                        return 'Apartamento'
                return 'Otro'
            
            datos['tipo_vivienda'] = datos['descripcion'].apply(clasificar_tipo)
            conteo_tipo = datos['tipo_vivienda'].value_counts()

            estadisticas = {
                'total_viviendas': total_viviendas,
                'precio_promedio': f"{precio_promedio:,.0f}",
                'area_promedio': f"{area_promedio:,.0f}",
                'precio_m2_promedio': f"{precio_m2_promedio:,.0f}",
                'casas_count': conteo_tipo.get('Casa', 0),
                'apartamentos_count': conteo_tipo.get('Apartamento', 0),
                'otros_count': conteo_tipo.get('Otro', 0),
                'precio_min':f"{datos['precio'].min():,.0f}",
                'precio_max': f"{datos['precio'].max():,.0f}",
                'area_comum': f"{datos['area'].mean():,.0f}"
            }

            print("Estadisticas calculadas correctamente.")
            return render_template('dashboard.html', **estadisticas)
        else:
            print("El archivo no existe en la ruta especificada.")
            return render_template('dashboard.html')
    except Exception as e:
        print(f"Error en el dashboard: {e}")
        return render_template('dashboard.html')

@app.route('/tabla')
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
@app.route('/grafico')
def mostrar_grafico():
    generar_dispersion()
    return render_template('grafico.html')

if __name__ == '__main__':
    app.run(debug=True)

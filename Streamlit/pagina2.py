#PRUEBA PARA ENTRAR A BIGQUERY, SI SE QUIERE USAR HAY QUE CAMBIAR EL ARCHIVO DE LAS CREDENCIALES

#from google.oauth2 import service_account
#from google.cloud import bigquery
import streamlit as st # type: ignore
import pandas as pd
import numpy as np

import os
import joblib # type: ignore

import ipywidgets as widgets # type: ignore
from IPython.display import display

import matplotlib.pyplot as plt # type: ignore
from datetime import datetime
from datetime import timedelta

from sklearn.metrics import mean_absolute_error, mean_squared_error # type: ignore

from prophet import Prophet # type: ignore
from prophet.plot import plot_plotly # type: ignore
import plotly.graph_objects as go # type: ignore

import time
# Acceder a las credenciales desde st.secrets
#credentials = service_account.Credentials.from_service_account_info(st.secrets["google_credentials"])

# ID del proyecto
#PROJECT_ID = st.secrets["google_credentials"]["project_id"]

# Configurar cliente de BigQuery
#client = bigquery.Client(credentials=credentials, project=PROJECT_ID)

# Consulta SQL: Ordenar por total_amount en orden descendente y limitar a 10 registros
#query = """
#    SELECT *
#    FROM `proyecto-final-sh-441422.taxis.INDUSTRY`
#    ORDER BY total_amount DESC
#    LIMIT 10
#"""

# Ejecutar la consulta
#@st.cache_data
#def run_query(query):
#    query_job = client.query(query)  # Ejecutar la consulta
#    results = query_job.result()  # Obtener los resultados
#    return results.to_dataframe()  # Convertir a un DataFrame de pandas

# Obtener los datos
#df = run_query(query)

# Mostrar los datos en Streamlit
#st.title("Top 10 registros con mayor Total Amount")
#st.dataframe(df)  # Mostrar como tabla

st.title('Modelo de Machine Learning')
st.subheader('Series de tiempo')

st.markdown("""
En esta página, podrás explorar las predicciones futuras para varias variables clave dentro de la industria de taxis, tanto para taxis verdes como amarillos. Las predicciones incluyen:

- **Cantidad de vehículos (unique_vehicles)**: Estimación de la cantidad de vehículos activos en la flota.
- **Tarifa Total (total_amount)**: Pronóstico de la tarifa total diaria.
- **Distancia Promedio (avg_trip_distance)**: Estimación de la distancia promedio recorrida por cada viaje.
- **Horas Promedio por Chofer (avg_hours_per_day_per_driver)**: Proyección de las horas totales que los choferes trabajarán cada día, basándose en el total de viajes.
- **Viajes Totales (total_trips)**: Predicción del número total de viajes realizados por día, proporcionando una visión general de la actividad en la flota.
- **Emisiones de CO2 (total_co2_emission)**: Estimación de las emisiones de dióxido de carbono generadas por los vehículos.

Estas predicciones se pueden utilizar para anticipar las tendencias del sector y ayudar a tomar decisiones informadas, tanto para la gestión operativa de los taxis como para la optimización de la flota y la reducción del impacto ambiental.            

""")
# Cargar los datos
df = pd.read_csv('datasets/2. Depurados/TLC Aggregated Data/ML_TS_Input.csv')
df['date'] = pd.to_datetime(df['date'])

# Widgets de Streamlit
# Selección de la industria
# Cargar los parámetros
df_params = pd.read_csv("Modelos de ML\mejores_modelos.csv")

# Crear un selector para la industria
industry_type = df_params['industry'].unique()
selected_industry = st.selectbox("Seleccione la industria:", options=industry_type)

# Filtrar las columnas en función de la industria seleccionada
filtered_df = df_params[df_params['industry'] == selected_industry]
columns = filtered_df['column'].unique()
selected_column = st.selectbox("Seleccione la variable a predecir:", options=columns)

# Crear un selector para el número de períodos
selected_periods = st.slider("Seleccione el número de períodos:", min_value=1, max_value=64, step=1)

# Mostrar los resultados seleccionados
st.write("### Selección")
st.write(f"**Industria seleccionada:** {selected_industry}")
st.write(f"**Variable seleccionada:** {selected_column}")
st.write(f"**Períodos seleccionados:** {selected_periods}")



#def graficar_original(df_prophet, column_name):
# #     fig = go.Figure()
# #     fig.add_trace(go.Scatter(x=df_prophet["ds"], y=df_prophet["y"], marker=dict(symbol='circle', color='royalblue')))
# #     fig.layout.update(title_text="Datos históricos", yaxis_title=f"{column_name}", xaxis_rangeslider_visible=True)
# #     fig.show()

# Función para graficar la predicción
def graficar_predicción(df_prophet, column_name, forecast, industry_type):
    """
    Función para graficar la predicción realizada por Prophet junto con el intervalo de confianza.
    Ajusta automáticamente el eje Y al rango de valores de los datos.
    """
    # Crear figura
    fig = go.Figure()

    # Datos históricos
    fig.add_trace(go.Scatter(
        x=df_prophet["ds"], 
        y=df_prophet["y"], 
        mode='lines+markers', 
        name='Datos Históricos', 
        marker=dict(symbol='circle', color='royalblue'),
        line=dict(color='royalblue', width=2)
    ))

    # Predicción
    fig.add_trace(go.Scatter(
        x=forecast['ds'], 
        y=forecast['yhat'], 
        mode='lines', 
        name='Predicción', 
        line=dict(color='green', width=3, dash='dot')
    ))

    # Intervalo de predicción
    fig.add_trace(go.Scatter(
        x=forecast['ds'].tolist() + forecast['ds'][::-1].tolist(),
        y=forecast['yhat_upper'].tolist() + forecast['yhat_lower'][::-1].tolist(), 
        fill='toself', 
        fillcolor='rgba(0, 128, 0, 0.2)', 
        line=dict(color='rgba(0, 0, 0, 0)'), 
        name='Intervalo de Predicción'
    ))

    # Calcular el rango automático para el eje Y
    y_values = (
        df_prophet["y"].tolist() + 
        forecast['yhat'].tolist() + 
        forecast['yhat_upper'].tolist()
    )
    y_min, y_max = min(y_values), max(y_values)

    # Configuración del layout
    fig.update_layout(
        title=f"Predicción para {column_name} ({industry_type})",
        xaxis_title='Fecha', 
        yaxis_title=column_name, 
        xaxis_rangeslider_visible=True,
        yaxis=dict(range=[y_min, y_max]), 
        template='plotly_white',
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
    )

    # Mostrar gráfico
    st.plotly_chart(fig)
    
    # Seleccionar y renombrar las columnas
    forecast_df = forecast[['ds', 'yhat']].rename(columns={'ds': 'Fecha', 'yhat': column_name})

    # Mostrar el DataFrame resultante
    st.write("Tabla de Predicciones:")
    st.dataframe(forecast_df)


# Función para obtener el nombre del archivo del modelo
def obtener_nombre_archivo(industry_type, column_name):
    """Genera un nombre de archivo único para una combinación de industria y columna."""
    return f"Modelos de ML/models/prophet_model_{industry_type}_{column_name}.pkl"

# Función para cargar o entrenar un modelo Prophet
def cargar_o_entrenar_modelo(df_prophet, industry_type, column_name, cps, sps, sm):
    """
    Carga un modelo Prophet guardado o lo entrena y guarda si no existe.
    """
    # Crear el directorio "models" si no existe
    os.makedirs("models", exist_ok=True)
    
    # Nombre del archivo del modelo
    modelo_path = obtener_nombre_archivo(industry_type, column_name)
    
    #Intentar cargar el modelo si ya existe
    if os.path.exists(modelo_path):
         st.write(f"Cargando modelo desde {modelo_path}...")
         model = joblib.load(modelo_path)
    
    else: 
        st.write(f"Entrenando modelo para {industry_type} - {column_name}...")
        model = Prophet(
            changepoint_prior_scale=cps,
            seasonality_prior_scale=sps,
            seasonality_mode=sm,
            yearly_seasonality=True,
            weekly_seasonality=False,
        )
        model.fit(df_prophet)
    # Guardar el modelo entrenado
    joblib.dump(model, modelo_path)
    print(f"Modelo guardado en {modelo_path}.")

    return model


# Función para cargar los datos y filtrar la serie de tiempo seleccionada
def cargar_y_preparar_datos(df, industry_type, column_name):
    """
    Filtra y prepara los datos para Prophet según el tipo de industria y la columna seleccionada.
    """
    df_filtered = df[df['industry'] == industry_type][['date', column_name]].copy()
    df_filtered.columns = ['ds', 'y']  # Renombrar columnas para Prophet
    df_filtered['ds'] = pd.to_datetime(df_filtered['ds'])  # Asegurar formato de fecha
    return df_filtered if not df_filtered['y'].isnull().all() else None


# Función principal para realizar la predicción
def pronóstico_con_grid_search(df_prophet, df_params, industry_type, column_name, periodos, frecuencia):
    """
    Realiza el pronóstico utilizando un modelo Prophet guardado o entrenado.
    """
    # Obtener los mejores parámetros
    filtered_df = df_params[(df_params['industry'] == industry_type) & (df_params['column'] == column_name)]
    
    if not filtered_df.empty:
        cps = filtered_df['changepoint_prior_scale'].iloc[0]
        sps = filtered_df['seasonality_prior_scale'].iloc[0]
        sm = filtered_df['seasonality_mode'].iloc[0]
    else:
        print("No se encontraron datos para la combinación especificada.")
        return

    # Cargar o entrenar modelo
    model = cargar_o_entrenar_modelo(df_prophet, industry_type, column_name, cps, sps, sm)

    # Realizar predicción
    future = model.make_future_dataframe(periods=periodos, freq=frecuencia)
    forecast = model.predict(future)

    # Graficar predicción
    graficar_predicción(df_prophet, column_name, forecast, industry_type)


# Configuración y ejecución principal
df_params = pd.read_csv('Modelos de ML/mejores_modelos.csv')

periodos = selected_periods
frecuencia = "MS"

industry_type = selected_industry
column_name = selected_column

# Preparar los datos
df_prophet = cargar_y_preparar_datos(df, industry_type, column_name)

if df_prophet is not None and not df_prophet.empty and df_prophet['y'].notnull().all():
    # Ejecutar Grid Search
    pronóstico_con_grid_search(df_prophet, df_params, industry_type, column_name, periodos=periodos, frecuencia=frecuencia)

# Mostrar tabla filtrada (opcional, para depuración o información al usuario)
#st.write("### Detalles de la industria seleccionada")
#filtered_df = pd.DataFrame(filtered_df)
#st.dataframe(filtered_df.style.format(precision=2, thousands=None))
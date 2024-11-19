# Proyecto de Machine Learning: Predicción de Series de Tiempo

**Dataset de Entrenamiento**
Utilizando un datset depurado de Taxis de Nueva York mensuales, construiremos un modelo de serie tiempo para la predicción de ciertas características.
Este proyecto tiene como objetivo predecir diferentes métricas en la industria de taxis usando modelos de series de tiempo. Utilizamos **Prophet** para construir un modelo que permita proyectar valores futuros con base en datos históricos.

## Requisitos

- **Prophet**
- **pandas**
- **plotly**
- **matplotlib**

### Prophet:

Es una biblioteca de código abierto desarrollada por Facebook para la previsión de series temporales. Hemos elegido esta biblioteca porque:

1. Facilidad de uso: La sintaxis es intuitiva y se puede integrar fácilmente con bibliotecas de Python, lo cual en nuestra curva de aprendizaje se vuelve de gran relevancia.
2. Manejo de estacionalidades y tendencias: Prophet asimila datos de series de tiempo con estacionalidad múltiples y genera una proyección con un margen de error aceptable.
3. Manejo de datos faltantes y outliers: Puede manejar datos ruidosos sin necesidad de un preprocesamiento exhaustivo.
4. Escalabilidad: para trabajar con grandes conjuntos de datos y múltiples series temporales.
5. Resultados interpretables: Los resultados son fáciles de leer y analizar.

## Contenido del Proyecto

### Carga de datos:

- Para el MVP, los datos se cargan desde un archivo CSV (`merged_taxi_data.csv`), filtrados por tipo de industria y variable a predecir, los cuales se seleccionan mediante inputs en el código. En el siguiente Sprint su carga será desde la nube para poder trabajar luego con Streamlit.
- Se asegura que solo se trabajen valores no negativos para mantener la coherencia de los datos.

## Cómo ejecutar el proyecto

En esta etapa de MVP, para ejecutar el análisis y realizar predicciones, el usuario debe tener los archivos de datos en la ubicación especificada y correr el notebook, donde se solicitarán inputs para la selección de variables y parámetros. En el producto final podrá realizarse dichas acciones directamente desde una botonera interactiva desarrollada en Streamlit.

### Selección de parámetros:

- El usuario puede elegir el tipo de industria y la métrica que desea analizar, entre opciones como `trips_per_day`, `total_co2_emission`, `vehicles_per_day`, entre otras.
- El usuario también puede definir la cantidad de períodos y la frecuencia de predicción (`D` para diaria, `W` para semanal, `M` para mensual, o `YE` para anual).

### Preparación de los datos:

- Los datos son procesados para cumplir con el formato que requiere Prophet, renombrando las columnas necesarias (`ds` para la fecha y `y` para la métrica).

### Visualización de datos históricos:

- Se genera un gráfico interactivo de los datos históricos seleccionados usando Plotly, lo que permite observar la tendencia inicial de la métrica seleccionada.

### Predicción de la serie de tiempo:

- Se configura el modelo de Prophet para incluir una estacionalidad mensual y modo aditivo.
- El modelo realiza una predicción, y los resultados se muestran en un gráfico con los valores históricos, la predicción, y el intervalo de confianza.

### Análisis de componentes:

- Se genera un análisis de los componentes del modelo de predicción, permitiendo observar las tendencias y estacionalidades capturadas.

### Guardado de predicciones:

- Finalmente, se guardan los resultados de la predicción en un archivo CSV.

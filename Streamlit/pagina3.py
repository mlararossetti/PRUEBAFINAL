#pagina de dashboards
import streamlit as st

# Título de la aplicación
st.title("Dashboards interactivos")
st.subheader("Introducción del Proyecto")

st.markdown(
    """
Este proyecto tiene como objetivo proporcionar una visión integral del mercado de taxis en Nueva York, explorando aspectos claves como la evolución de la flota, la geolocalización de los viajes, el impacto ambiental  asociado a esta industria, como así también un y un detalle financiero sobre la propuesta de negocio. Para ello, se desarrollaron tres dashboards en Power BI que permiten analizar y comprender las dinámicas y tendencias del mercado de taxis entre 2021 y 2024. Estas visualizaciones interactivas facilitan la toma de decisiones estratégicas para quienes buscan insights profundos sobre el funcionamiento y el impacto de esta industria en la ciudad.
   """
)

st.markdown(
    """
    #### Dashboard 1: Análisis Temporal y por Industria del Mercado
En este primer dashboard, se examina la evolución del mercado de taxis en Nueva York desde 2021 a 2024, incluyendo el número de autos por industria, los ingresos generados y el volumen de viajes. Con segmentadores de tiempo e industria, permite una comparación detallada por año y sector de la industria.  
Asimismo, en el sector derecho del dashboard, se muestra un apartado interactivo donde se pueden seleccionar diferentes variantes sobre la cantidad de vehículos a incorporar y el promedio diario de viajes por cada uno, lo que permite evaluar ante las diversas alternativas si se cumplen los KPI's propuestos para la empresa.   
   """
)

# URL del dashboard de Power BI
power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiZmZmYzQ3NDgtOTI3MC00MDg0LWI2NDUtOTAxYWVlMThjZDU5IiwidCI6IjkyZTI3Mzg0LWI2YjAtNGIxMy05ZWU4LTFkOGY2ZGI5YzdmNSJ9"

# Inserta el iframe como HTML
iframe_html = f"""
<iframe
    src="{power_bi_url}"
    width="1000"
    height="800"
    frameborder="0"
    allowFullScreen="true">
</iframe>
"""
st.markdown(iframe_html, unsafe_allow_html=True)

st.markdown(
    """
    #### Dashboard 2: Análisis Georreferencial de Viajes
   """
)
# Crear un enlace a otra página
st.markdown("[Ir al Dashboard N°2](./pagina4)")

st.markdown(
    """
    #### Dashboard 3: Análisis Impacto Ambiental
   """
)
# Crear un enlace a otra página
st.markdown("[Ir al Dashboard N°3](./pagina5)")

st.markdown(
    """
    #### Dashboard 4: Análisis Financiero
   """
)
# Crear un enlace a otra página
st.markdown("[Ir al Dashboard N°4](./pagina6)")
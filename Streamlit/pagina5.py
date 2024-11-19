#pagina de dashboards
import streamlit as st

# Título de la aplicación
st.title("Dashboards interactivos")

st.markdown(
    """
    ####  Dashboard 1: Análisis Temporal y por Industria del Mercado
   """
)
# Crear un enlace a otra página
st.markdown("[Ir al Dashboard N°1](./pagina3)")

st.markdown(
    """
    ####  Dashboard 2:  Análisis Georreferencial de Viajes
   """
)
# Crear un enlace a otra página
st.markdown("[Ir al Dashboard N°1](./pagina3)")
st.markdown(
    """
    #### Dashboard 3: Análisis Impacto Ambiental
El tercer dashboard se centra en los aspectos ambientales del mercado de taxis, ofreciendo un análisis de impacto a corto y largo plazo.  
En el corto plazo se analiza el AQI (Índice de Calidad del Aire), comparando la evolución de sus valores máximos a lo largo de los años y el comportamiento de la categoría de los días con el paso del tiempo.  
En lo que respecta al largo plazo, se analizan contaminantes que afectan a la capa de ozono, y puntualmente nos estamos centrando en el CO2 (dióxido de carbono), el contaminante que es generado en gran medida por el tráfico vehicular.  
En la parte inferior se incorpora un KPI relevante para monitorear el rendimiento ambiental del proyecto y ayuda a identificar oportunidades de mejora en la sostenibilidad del mismo.
"""
)

# URL del dashboard de Power BI
power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiYTMxYjdhYWQtMzdlYS00YzFkLWI0YzgtNmY2NjU0ZmIyYTE2IiwidCI6IjkyZTI3Mzg0LWI2YjAtNGIxMy05ZWU4LTFkOGY2ZGI5YzdmNSJ9"


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
    #### Dashboard 4: Análisis Financiero
   """
)
# Crear un enlace a otra página
st.markdown("[Ir al Dashboard N°4](./pagina6)")
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
    #### Dashboard 2: Análisis Georreferencial de Viajes
Este dashboard ofrece una visión detallada de las áreas de mayor actividad de taxis en la ciudad, destacando las zonas de recogida (pick-up) y destino (drop-off) y las principales áreas dentro de cada borough. Los datos están segmentados por años y borough, permitiendo analizar cambios en las tendencias de demanda en diferentes ubicaciones clave.   """
)

# URL del dashboard de Power BI
power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiYmNmZWRkZjMtYzE0Ny00MGMzLTgyYzAtMzg5YWIxN2EwYzNhIiwidCI6IjkyZTI3Mzg0LWI2YjAtNGIxMy05ZWU4LTFkOGY2ZGI5YzdmNSJ9"

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
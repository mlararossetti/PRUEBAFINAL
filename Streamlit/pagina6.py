#pagina de dashboards
import streamlit as st

# Título de la aplicación
st.title("Dashboards interactivos")
st.subheader("")

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
import streamlit as st
#from streamlit_option_menu import option_menu  # Librería para el menú


# Configurar la página
st.set_page_config(page_title="Inicio", layout="wide")

# Agregar la imagen en la parte superior de la barra lateral
st.sidebar.image("Logo PNG WHITE.png", use_container_width=True)


# Incrustar CSS para personalizar estilos, incluyendo el menú lateral
st.markdown(
    """
    <style>
    /* Cambiar fondo de la aplicación */
    .stApp {
        background-color: #FFFFFF; /* Cambia este color al que desees */
        color: #1E1E1E; /* Cambia este color al del texto */
        font-family: 'Arial', sans-serif; /* Cambia la fuente si quieres */
    }

    /* Personalizar el fondo del menú lateral */
    .st-emotion-cache-6qob1r {
        background-color: #48448F;  /* Fondo del menú lateral */
        color: #FFFFFF;  /* Color de los textos en el menú lateral */
    }

    /* Personalizar los íconos en el menú lateral */
    .css-1jczs2c {
        color: #FF0037;  /* Color de los íconos en el menú */
    }
    /* Personalizar los nombres en el menú lateral */
    .st-emotion-cache-6tkfeg  {
        color: #FFFFFF;  /* Color de los íconos en el menú */
    }
    /* Personalizar los elementos del menú */
    .stSidebar .sidebar .sidebar-content .menu-item {
        background-color: #FFFFFF;  /* Fondo de cada opción en el menú */
        color: #FFFFFF;  /* Color del texto de las opciones del menú */
        border-radius: 8px;  /* Bordes redondeados para las opciones */
        margin-bottom: 5px;  /* Espaciado entre las opciones */
    }

    /* Cambiar el color cuando el usuario pasa el cursor sobre una opción del menú */
    .stSidebar .sidebar .sidebar-content .menu-item:hover {
        background-color: #FFFFFF;  /* Color de fondo al pasar el cursor */
        color: #000000;  /* Cambiar el color del texto cuando pasa el cursor */
    }

    /* Cambiar el color del menú activo */
    .stSidebar .sidebar .sidebar-content .menu-item-active {
        background-color: #FFFFFF;  /* Fondo para el ítem seleccionado */
        color: #FFFFFF;  /* Color de texto del ítem seleccionado */
    }

    /* Títulos y subtítulos */
    h1 {
        color: #48448F; /* Título principal */
    }
    h2, h3, h4 {
        color: #00a5bf; /* Otros encabezados */
    }

    /* Personalizar los enlaces */
    a {
        color: #e74c3c; /* Color de enlaces */
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Páginas

pagina1 = st.Page(
    page = 'pagina1.py',
    title = 'Home',
    icon = '📦', 
    default= True,)

pagina2 = st.Page(
     page = 'pagina2.py',
     title = 'Modelos de predicción',
     icon = '📈')


pagina3 = st.Page(
     page = 'pagina3.py',
     title = 'Análisis Temporal y por Industria',
     icon = '🚖')


pagina4 = st.Page(
     page = 'pagina4.py',
     title = 'Análisis Georreferencial de Viajes',
     icon = '🗺️')

pagina5 = st.Page(
     page = 'pagina5.py',
     title = 'Análisis Impacto Ambiental',
     icon = '🌎')

pagina6 = st.Page(
    page = 'pagina6.py',
    title ='Análsis Financiero',
    icon = '📈'
)

pg = st.navigation(pages=[pagina1, pagina2, pagina3, pagina4, pagina5,pagina6])
pg.run()


# Mostrar la imagen cargada

st.sidebar.text('DATABOX 2024')
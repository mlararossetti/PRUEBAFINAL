import streamlit as st 
# Título de la página
st.title("Bienvenidos a DataBox")

col1, col2 = st.columns(2, gap='small', vertical_alignment='center')

with col1:
    st.image('Logo PNG BLACK.png', width= 300)

with col2:
    st.header('¿Quiénes somos y qué hacemos?', anchor=False)
    st.markdown(
    """
    Somos DataBox y nuestro compromiso es “Convertir datos en valor". 
    En un mundo impulsado por la información, entendemos que los datos son más que números; son oportunidades. 
    Fundada con la misión de transformar la forma en que las empresas utilizan su información, DATABOX se posiciona como un líder en soluciones de análisis de datos y business intelligence. 
    Nuestra visión es empoderar a las organizaciones a tomar decisiones informadas, basadas en insights profundos y estrategias adaptadas a sus necesidades. 
    Con un equipo de expertos apasionados por la tecnología y la analítica, ofrecemos herramientas innovadoras que permiten a nuestros clientes extraer el máximo valor de sus datos.
    
   """
    
)

st.markdown(
    """
     ### Nuestro equipo
    """)
# Mostrar la imagen cargada
st.image("Nuestro Equipo.png", use_container_width=True)

st.markdown(
    """
     ### Proyecto de trabajo
    """)
# Mostrar la imagen cargada
st.image("Portada Readme.png", use_container_width=True)

st.subheader("Contacto")
st.write(
    """
    **DATABOX**  
    📧 Email: info@databox.com  
    📞 Teléfono: +1 234 567 890  
    """
)

# Mostrar la imagen cargada
st.image("Pie.png", use_container_width=True)
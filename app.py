import streamlit as st
from PIL import Image

st.title(" Mi Primera App!!")

st.header("Cuida los ojos y la visión")
st.write("El cuidado de los ojos consiste en mantenerlos sanos mediante buenos hábitos diarios, chequeos regulares y tratamiento cuando sea necesario. ")
image = Image.open('paolasuarez.jpg')
st.image(image, caption='Revisate la vista')

texto = st.text_input('Los ojos son una parte importante de la salud.', '¿Qué importancia tiene el cuidado de la vista?')
st.write('Algunas enfermedades oculares pueden provocar pérdida de la visión sin señales de advertencia tempranas, por lo que es importante detectarlas lo antes posible. Revise sus ojos con la frecuencia que le recomiende su profesional de la salud o si nota nuevos problemas de visión.')

st.subheader("Ahora usemos 2 Columnas")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Esta es la primera columna")
    st.write("Las interfaces multimodales mejoran la experiencia de usuario")
    resp = st.checkbox('Estoy de acuerdo')
    if resp:
       st.write('Correcto!')
  
with col2:
    st.subheader("Esta es la segunda columna")
    modo = st.radio("Que Modalidad es la principal en tu interfaz", ('Visual', 'auditiva', 'Táctil'))
    if modo == 'Visual':
       st.write('La vista es fundamental para tu interfaz')
    if modo == 'auditiva':
       st.write('La audición es fundamental para tu interfaz')
    if modo == 'Táctil':
       st.write('El tacto es fundamental para tu interfaz')

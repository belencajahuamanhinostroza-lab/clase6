import streamlit as st
from PIL import Image

st.title(" Mi Primera App!!")

st.header("Cuida los ojos y la visión")
st.write("El cuidado de los ojos consiste en mantenerlos sanos mediante buenos hábitos diarios, chequeos regulares y tratamiento cuando sea necesario. ")
image = Image.open('paolasuarez.jpg')
st.image(image, caption='Revisate la vista')

texto = st.text_input('Los ojos son una parte importante de la salud.', '¿Qué importancia tiene el cuidado de la vista?')
st.write('Algunas enfermedades oculares pueden provocar pérdida de la visión sin señales de advertencia tempranas, por lo que es importante detectarlas lo antes posible. Revise sus ojos con la frecuencia que le recomiende su profesional de la salud o si nota nuevos problemas de visión.')

st.subheader("En esta página")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Prevención y factores de riesgo")
    st.write("Dieta, nutrición y suplementos para la salud ocular, "Gafas de seguridad: Cómo prevenir lesiones oculares que pueden causar ceguera")
    resp = st.checkbox('Recibir información')
    if resp:
       st.write('Correcto!')
  
with col2:
    st.subheader("¿Cómo puedo mantener mis ojos sanos?")
    modo = st.radio("Hay muchas cosas que usted puede hacer para proteger sus ojos y ver lo mejor posible:", ('Dele un descanso a sus ojos', 'Use gafas de sol', 'Evite frotarse los ojos'))
    if modo == 'Dele un descanso a sus ojos':
       st.write('Pasar muchas horas frente a la computadora u otras pantallas digitales puede hacer que parpadee menos,')
    if modo == 'Use gafas de sol':
       st.write('Protéjase los ojos usando gafas de sol que bloqueen entre el 99 y el 100% de la radiación UV-A y UV-B')
    if modo == 'Evite frotarse los ojos':
       st.write('Frotarse los ojos puede transferir suciedad y bacterias que pueden causar irritación o provocar una infección')

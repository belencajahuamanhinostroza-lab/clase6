import streamlit as st
from PIL import Image

st.title(" Mi Primera App!!")

st.header("Cuida los ojos y la visión")
st.write("El cuidado de los ojos consiste en mantenerlos sanos mediante buenos hábitos diarios, chequeos regulares y tratamiento cuando sea necesario. ")
image = Image.open('paolasuarez.jpg')
st.image(image, caption='Revisate la vista')

texto = st.text_input('Los ojos son una parte importante de la salud.', 'Usted depende de ellos a diario para ver y comprender el mundo que le rodea.')
st.write('Que pueden ocasionar las enfermedades', texto)

import streamlit as st
from PIL import Image

st.title(" Mi Primera App!!")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open('paolasuarez.jpg')
st.image(image, caption='Interfaces multimodales')

texto = st.text_input('Una interfaz multimodal es un sistema digital que permite a los usuarios interactuar usando dos o más métodos de comunicación a la vez, como la voz, el tacto, los gestos y la mirada. Estos canales se combinan para dar una experiencia más natural.', 'Este es mi texto')
st.write('El texto escrito es', texto)

import json
import streamlit as st

def autenticacion_usuario():
    permiso_ingreso: bool = False
    correo_autenricacion = None
    # Lee el contenido del archivo JSON
    with open('formulario_data.json', 'r') as file:
        lista_de_diccionarios = json.load(file)


    with st.form('Autenticación'):
        correo_usuario: str = st.text_input('ingresa el correo')
        contraseña: str = st.text_input('iIngrese la contraseña', type="password")
        if st.form_submit_button('Autenticar'):
            for diccionario in lista_de_diccionarios:
                if diccionario['Correo'] == correo_usuario and diccionario['Correo'] == correo_usuario:
                    st.success('Usuario autenticado correctamente.')
                    permiso_ingreso = True 
                    break
                else:
                    continue
            if permiso_ingreso == False:
                st.error("No se pudo realizar la autenticación con los datos proporcionados. Verifiquelos o registrese.")
            
    return permiso_ingreso            
                    

                

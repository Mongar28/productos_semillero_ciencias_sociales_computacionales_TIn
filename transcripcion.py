import streamlit as st
import os
import json
from datetime import datetime
from maqueta.mensaje_principal import encabezado
from autenticacion.autenticar import autenticacion_usuario
from archivos.doc_transcripcion import transcripcion_doc
from donaciones.donaciones_sc2 import donaciones
from app_transcripcion.speach_to_text import (mensaje_intruncciones,
                                              importar_audio_file,
                                              procesamiento_audio)


# Importamos y corremos la funcion encabezado del modulo mensaje principal. 
encabezado()

# importamos y corremos la funcion mensaje_intruncciones  del modulo speach_to_text que contiene el mensaje y las instrucciones de la app
mensaje_intruncciones()

# importamos y corremos la funcion importar_audio_file del modulo speach_to_text que contiene la caja para subir el archivo de audio
nombre_archivo = importar_audio_file()

# importamos y corremos la funcion procesamiento_audio del modulo speach_to_text que contiene los scripts para procesar el audio con Whisper
list_transcripciones = procesamiento_audio(nombre_archivo)
formulario_enviado = False

# importamos y corremos la funci[on ]
if len(list_transcripciones) > 0:
    formulario_enviado, correo, nombre = autenticacion_usuario()
    
if formulario_enviado == True:
    transcripcion_doc(list_transcripciones)
    donaciones()
    
    archivo_json = 'historial_uso_app.json'
    if os.path.exists(archivo_json):
        with open(archivo_json, "r") as json_file:
            datos_uso = json.load(json_file)
    else:
        datos_uso = []  
        
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    datos = {
        'nombre_usuario': nombre,
        'correo' : correo,
        'fecha': fecha_actual,
        'aplicacion_usada': 'transcriptor'
    }

    datos_uso.append(datos)
    with open(archivo_json, "w", encoding="utf-8") as json_file:
        json.dump(datos_uso, json_file, indent=4, ensure_ascii=False)   


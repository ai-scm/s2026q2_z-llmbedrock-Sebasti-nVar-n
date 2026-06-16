import streamlit as st
import boto3
import os
from dotenv import load_dotenv

# 1. Configuración
load_dotenv()
st.set_page_config(page_title="Tutor AWS Cloud Practitioner", page_icon="☁️")

# 2. Configurar cliente de Bedrock
bedrock = boto3.client(
    service_name='bedrock-runtime',
    region_name=os.getenv('AWS_REGION')
)

# 3. Función para cargar el prompt estricto desde el archivo
def get_system_prompt():
    try:
        with open("prompts/system_prompt.txt", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Eres un asistente especializado en AWS Cloud Practitioner."

# 4. Inicializar historial y botón de limpieza
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Cloud Practitioner Tutor ☁️")

if st.button("Limpiar conversación"):
    st.session_state.messages = []
    st.rerun()

# 5. Mostrar historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. Lógica de chat
if prompt := st.chat_input("¿Qué duda tienes sobre AWS?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Preparar mensajes
    bedrock_messages = [
        {"role": m["role"], "content": [{"text": m["content"]}]}
        for m in st.session_state.messages
    ]

    # Generar respuesta
    with st.chat_message("assistant"):
        try:
            response = bedrock.converse(
                modelId=os.getenv('MODEL_ID'),
                messages=bedrock_messages,
                system=[{"text": get_system_prompt()}], # Prompt estricto
                inferenceConfig={"maxTokens": 2000, "temperature": 0.1} # Temp baja = más preciso
            )
            
            ai_text = response['output']['message']['content'][0]['text']
            st.markdown(ai_text)
            st.session_state.messages.append({"role": "assistant", "content": ai_text})
            
        except Exception as e:
            st.error(f"Error técnico: {e}")
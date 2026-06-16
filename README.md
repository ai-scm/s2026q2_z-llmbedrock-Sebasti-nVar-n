# 🚀 Asistente Inteligente AWS Cloud Practitioner 
# Proyecto: Semillero All Star - Blend360

# Este repositorio contiene la implementación de un agente conversacional especializado en el temario de la certificación AWS Certified Cloud Practitioner, desarrollado como parte del programa de formación técnica del Semillero.

# 📝 Parte A: Diseño del Agente
El agente ha sido diseñado bajo un enfoque de especialización técnica.

Perfil: Tutor experto en servicios Core de AWS (EC2, S3, IAM, Facturación, Well-Architected).

Restricciones: Se implementó un sistema de Guardrail Dinámico que analiza la intención del usuario antes de procesar cualquier respuesta. Si la consulta no está relacionada con el ecosistema AWS, el agente bloquea la interacción para evitar "alucinaciones" o desvíos del objetivo educativo.

Tono: Pedagógico, técnico y directo.

# 🛠️ Parte B: Implementación Técnica
La arquitectura sigue un patrón modular para asegurar escalabilidad y mantenibilidad:

Frontend: Streamlit para la interfaz de chat.

Motor de IA: Meta Llama 3 (vía Amazon Bedrock).

Gestión de Sesión: Manejo de historial persistente mediante session_state.

Seguridad: Implementación de variables de entorno para la gestión de credenciales (evitando hardcoding).

Estructura de archivos

# ├── prompts/              # Configuración de comportamiento (System Prompts)
# ├── services/             # Lógica de conexión con Amazon Bedrock
# ├── utils/                # Gestión de memoria y utilidades
# ├── app.py                # Interfaz principal de usuario
# ├── Dockerfile            # Configuración para contenerización
# └── requirements.txt      # Dependencias del proyecto

# ⚙️ Paso a paso: Ejecución local
Para poner en marcha el asistente en tu entorno local, sigue estas instrucciones:

1. Requisitos previos
Instalar Docker y Python 3.11+.

Configurar una cuenta de AWS con acceso a Amazon Bedrock (Modelos de Meta habilitados en tu región).

2. Configuración de credenciales
Crea un archivo .env en la raíz del proyecto y añade tus credenciales (asegúrate de que este archivo nunca se suba al repositorio):

AWS_ACCESS_KEY_ID=tu_access_key
AWS_SECRET_ACCESS_KEY=tu_secret_key
AWS_REGION=us-east-1
MODEL_ID=meta.llama3-70b-instruct-v1:0

3. Ejecución vía Docker (Recomendado)
Para asegurar que funcione igual en cualquier máquina, utiliza Docker:

Construir la imagen:

docker build -t aws-tutor-assistant .

2. **Ejecutar el contenedor:**
   ```bash
   docker run -p 8501:8501 --env-file .env aws-tutor-assistant

   Acceder a la app:
Abre tu navegador y dirígete a http://localhost:8501.

# 🤝 Autor
# Sebastián Varón 

# Programa: Programación de Software - SENA

# Mentoría: Semillero All Star - Blend360

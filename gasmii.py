import os
from dotenv import load_dotenv
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()

GOOGLE_AI_KEY = os.getenv("GOOGLE_AI_KEY")

genai.configure(api_key=GOOGLE_AI_KEY)

config_generacion = {
    "temperature": 0.8,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 2000,  # Más tokens para contexto extendido
}

seguridad = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"}
]

modelo_principal = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
    generation_config=config_generacion,
    safety_settings=seguridad
)
# Función para generar respuestas limitadas a plantas


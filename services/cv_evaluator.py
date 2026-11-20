from langchain_ollama import ChatOllama
from models.cv_model import AnalisisCV
from prompts.cv_prompts import crear_sistema_prompts

def crear_evaluator_cv():
    """Crea un evaluador de CV utilizando el modelo de lenguaje y los prompts especializados."""
    llm = ChatOllama(model="llama3.2", temperature=0.2)
    modelo_estructurado = llm.with_structured_output(AnalisisCV)
    chat_prompt = crear_sistema_prompts()
    cadena_evaluacion=chat_prompt | modelo_estructurado
    return cadena_evaluacion

def evaluar_candidato(texto_cv: str, descripcion_puesto: str)->AnalisisCV:
    """Función de ejemplo para evaluar un candidato utilizando el evaluador de CV."""
    try:
        cadena_evaluacion = crear_evaluator_cv()
        resultado=cadena_evaluacion.invoke({"texto_cv": texto_cv, "descripcion_puesto": descripcion_puesto})
        return resultado
    except Exception as e:
        
        return AnalisisCV(
            nombre_candidato="Error en procesamiento",
            experiecnia_años=0,
            habilidades_clave=["erro al procesar cv"],
            educacion="no se puede determinar",
            experiecnia_relevante="error duarante el analisis",
            fortalezas=["requiere revision manual del cv"],
            areas_mejora=["verificar formato y hanilidad del pdf"],
            porcentaje_ajuste=0
        )
       

    
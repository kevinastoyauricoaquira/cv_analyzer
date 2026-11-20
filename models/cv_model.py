from pydantic import BaseModel, Field

class AnalisisCV(BaseModel):
    
    """Modelo de datos para el análisis de un CV. Contiene información relevante extraída del CV del candidato."""

    nombre_candidato: str = Field(description="Nombre completo del candidato extraido del CV.")
    correo: str = Field(description="Correo electrónico del candidato")
    telefono: str = Field(description="Número de teléfono del candidato")
    experiencia_años: int = Field(description="Años totales de experiecnia laboral relevante.")
    habilidades_clave: list[str] = Field(description="Lista de las 5-7 habilidades del candidato mas relevantes para el puesto.")
    education: str = Field(description="Nivel eductivo mas alto y especializacion principal.")
    experiencia_relevante:str=Field(description="Resumen conciso de la experiencia mas relevante para el puesto especifico.")
    fortalezas:list[str]=Field(description="Lista de 3-5 principales fortalezas del candidato basadas en su perfil.")
    areas_mejora:list[str]=Field(description="2-4 áreas donde el candidato podria desarrolar o mejorar")
    porcentaje_ajuste:int = Field(description="Porcentaje de ajuste al puesto(0-100) basado en experiencia,habilidades y formación",ge=0,le=100)

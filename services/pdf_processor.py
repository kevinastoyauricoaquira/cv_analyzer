import PyPDF2
from io import BytesIO

def extraer_texto_pdf(archivo_pdf):
    try:
        # Leer el archivo PDF
        pdf_reader = PyPDF2.PdfReader(BytesIO(archivo_pdf.read()))

        texto_completo = ""
        
        # Extraer texto de cada página
        for numero_pagina,pagina in enumerate(pdf_reader.pages,1) :
            texto_pagina = pagina.extract_text()
            if texto_pagina.strip():  # Verificar si la página tiene texto
                texto_completo += f"\n--- Página {numero_pagina} --\n"
                texto_completo += texto_pagina+"\n"
        texto_completo=texto_completo.strip()  # Eliminar saltos de línea dobles
        if not texto_completo:
            return "error:El PDF no contiene texto extraíble."
        return texto_completo
    except Exception as e:
        return f"error:Error al procesar el archivo PDF: {str(e)}"
    

 

import pandas as pd
import re

def extraer_correo(texto):
    """Extrae el primer correo válido encontrado en el texto."""
    if pd.notna(texto) and '@' in str(texto):
        match = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', str(texto))
        return match.group() if match else ''
    return ''

def limpiar_rut(file_path, output_path):
    """Carga el Excel, extrae correos y guarda un archivo limpio sin RUT."""
    print("🔍 Iniciando el proceso...")
    print(f"📂 Cargando archivo: {file_path}")

    df = pd.read_excel(file_path)
    print("📑 Columnas detectadas:", list(df.columns))

    # Extraer correos
    df['Correo dirigente 1'] = df['Número y correo del dirigente 1'].apply(extraer_correo)
    df['Correo dirigente 2'] = df['Número y correo del dirigente 2'].apply(extraer_correo)

    # Eliminar datos sensibles
    df.drop(['Número y correo del dirigente 1', 'Número y correo del dirigente 2'], axis=1, inplace=True)

    # Guardar nuevo archivo
    df.to_excel(output_path, index=False)
    print(f"✅ Archivo limpio guardado como: {output_path}")

if __name__ == "__main__":
    try:
        limpiar_rut('Planilla_Respuesta.xlsx', 'Planilla_Respuesta_Sin_RUT.xlsx')
    except Exception as e:
        print(f"❌ Error: {e}")

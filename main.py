import gspread
import pandas as pd
import time
from oauth2client.service_account import ServiceAccountCredentials

# CONFIGURACIÓN
ARCHIVO_CREDENCIALES = "actualizador-sheets.json"  
ID_HOJA = "1qssPD7MdZZRvMxlJ_lLLdIx3guQ5CmMijk-fw9gX0zs"          
NOMBRES_HOJAS = ["Clientes", "Peso", "Ejemplo"]            # Las pestañas que quieras traer
INTERVALO_MINUTOS = 1  # Intervalo de actualización (en minutos)

# AUTENTICACIÓN
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credenciales = ServiceAccountCredentials.from_json_keyfile_name(ARCHIVO_CREDENCIALES, scope)
cliente = gspread.authorize(credenciales)

def actualizar_todo_en_un_excel():
    print("🔄 Iniciando descarga de todas las hojas en un solo archivo...")

    spreadsheet = cliente.open_by_key(ID_HOJA)

    with pd.ExcelWriter("reporte_completo.xlsx", engine="openpyxl") as writer:
        for nombre in NOMBRES_HOJAS:
            try:
                hoja = spreadsheet.worksheet(nombre)
                datos = hoja.get_all_records()
                df = pd.DataFrame(datos)
                df.to_excel(writer, sheet_name=nombre, index=False)
                print(f"✅ Hoja '{nombre}' agregada al archivo.")
            except Exception as e:
                print(f"❌ Error al procesar la hoja '{nombre}': {e}")

    print("✔️ Archivo 'reporte_completo.xlsx' generado exitosamente.\n")

while True:
    actualizar_todo_en_un_excel()
    print(f"⏳ Esperando {INTERVALO_MINUTOS} minuto(s)...\n")
    time.sleep(INTERVALO_MINUTOS * 60)

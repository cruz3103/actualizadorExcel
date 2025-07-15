import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# 👉 Reemplazá esto con el nombre de tu archivo JSON
ARCHIVO_CREDENCIALES = "actualizador-sheets.json"  
ID_HOJA = "1tJ34qnbbERsSTXIATWVlEMctI2lyXWq0sytRcCCOsYU"          

# 1. Autenticación con la cuenta de servicio
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credenciales = ServiceAccountCredentials.from_json_keyfile_name(ARCHIVO_CREDENCIALES, scope)
cliente = gspread.authorize(credenciales)

# 2. Abrir la hoja por ID
spreadsheet = cliente.open_by_key(ID_HOJA)

# 3. Seleccionar la pestaña llamada 'Clientes'
hoja = spreadsheet.worksheet("Clientes")

# 4. Obtener los datos como registros (diccionarios)
datos = hoja.get_all_records()

# 5. Convertir a DataFrame de pandas
df = pd.DataFrame(datos)

# 6. Guardar como archivo Excel
df.to_excel("datos_actualizados.xlsx", index=False)

print("✅ ¡Datos importados y guardados en 'datos_actualizados.xlsx'!")

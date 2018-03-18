import pandas as pd
from pymongo import MongoClient
from bson import BSON
from bson import json_util
import json


xl_reclamos = pd.ExcelFile("RECLAMOS_HACKATHON.xlsx")

df_reclamos = xl_reclamos.parse(xl_reclamos.sheet_names[0], converters={'DOCUMENTO IDENTIFICACIÓN (DNI/RUC)':str})


xl_sanciones = pd.ExcelFile("SANCIONES_HACKATHON.xlsx")
xl_sanciones.sheet_names

df_sanciones = xl_sanciones.parse(xl_sanciones.sheet_names[0], converters={'DOCUMENTO IDENTIFICACIÓN (DNI/RUC)':str})


client = MongoClient('localhost', 27017)
db = client['Indecopi']




records = json.loads(df_reclamos.T.to_json()).values()
db.Reclamos.insert(records)

records = json.loads(df_sanciones.T.to_json()).values()
db.Sanciones.insert(records)



#Lector de archivos de data

import csv
import json
import os

def read_users_csv():
    base = os.path.dirname(os.path.dirname(__file__)) #arma una ruta relativa parandose en este archivo y subiendo 2 niveles (1 por cada "os.path.dirname()")
    ruta = os.path.join(base, "data", "users.csv") #combina el nivel mas alto de carpeta "base" con data y users, se joinea así para evitar problemas entre OSs
    with open (ruta, newline="", encoding="utf-8") as file: 
        reader = csv.DictReader(file)  #DictReader guarda cada linea como si fuera un diccionario
        return list(reader)     

def read_json_files(archivo):
    base = os.path.dirname(os.path.dirname(__file__)) 
    ruta = os.path.join(base, "data", archivo)
    with open (ruta, encoding="utf-8") as file:
        return json.load(file)
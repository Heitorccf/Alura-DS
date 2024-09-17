import json
import csv

def leitura_json(path_json):
   dados_json=[]
   with open(path_json, "r") as file:
      dados_json=json.load(file)
   return dados_json

def leitura_csv(path_csv):
   dados_csv=[]
   with open(path_csv, "r") as file:
      spamreader=csv.DictReader(file, delimiter=",")
      for row in spamreader:
         dados_csv.append(row)
   return dados_csv

path_json="Pipeline/Documentos/Setores/unprocessed-data/files-comp-I.json"
path_csv="Pipeline/Documentos/Setores/unprocessed-data/files-comp-II.csv"

dados_json=leitura_json(path_json)
print(dados_json[0])

dados_csv=leitura_csv(path_csv)
print(dados_csv[0])
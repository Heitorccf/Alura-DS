import json

path_json="Pipeline/Documentos/Setores/unprocessed-data/files-comp-I.json"

def leitura_json(path_json):
   dados_json=[]
   with open(path_json, "r") as file:
      dados_json=json.load(file)
   return dados_json

dados_json=leitura_json(path_json)
print(dados_json[0])
import json
import csv

# Função para ler um arquivo JSON e retornar os dados
def leitura_json(path_json):
   dados_json = []  # Inicializa uma lista para armazenar os dados
   with open(path_json, "r") as file:  # Abre o arquivo JSON para leitura
      dados_json = json.load(file)  # Carrega os dados do JSON no formato de um dicionário/lista
   return dados_json  # Retorna os dados lidos

# Função para ler um arquivo CSV e retornar os dados
def leitura_csv(path_csv):
   dados_csv = []  # Inicializa uma lista para armazenar os dados
   with open(path_csv, "r") as file:  # Abre o arquivo CSV para leitura
      spamreader = csv.DictReader(file, delimiter=",")  # Lê o CSV como dicionário (cada linha é um dicionário)
      for row in spamreader:  # Itera por cada linha do CSV
         dados_csv.append(row)  # Adiciona cada linha à lista
   return dados_csv  # Retorna os dados lidos

# Função que decide qual tipo de arquivo ler (JSON ou CSV) baseado na extensão informada
def leitura_dados(path, tipo_arquivo):
   dados = []  # Inicializa uma lista para armazenar os dados
   if tipo_arquivo == "csv":  # Se o tipo for CSV
      dados = leitura_csv(path)  # Chama a função para ler CSV
   elif tipo_arquivo == "json":  # Se o tipo for JSON
      dados = leitura_json(path)  # Chama a função para ler JSON
   return dados  # Retorna os dados lidos

# Caminhos dos arquivos JSON e CSV
path_json = "Pipeline/Documentos/Setores/unprocessed-data/files-comp-I.json"
path_csv = "Pipeline/Documentos/Setores/unprocessed-data/files-comp-II.csv"

# Lê o arquivo JSON e imprime o primeiro item da lista
dados_json = leitura_dados(path_json, "json")
print(dados_json[0])

# Lê o arquivo CSV e imprime o primeiro item da lista
dados_csv = leitura_dados(path_csv, "csv")
print(dados_csv[0])

# Linhas comentadas que são duplicadas das funções acima:
# dados_json = leitura_json(path_json)
# print(dados_json[0])

# dados_csv = leitura_csv(path_csv)
# print(dados_csv[0])
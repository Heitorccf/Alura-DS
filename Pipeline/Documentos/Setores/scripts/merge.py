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

# Função para obter os nomes das colunas dos dados
def get_columns(dados):
    if dados:  # Verifica se a lista não está vazia
        return list(dados[0].keys())
    return []

# Função para obter o tamanho dos dados
def size_data(dados):
    return len(dados)

def join(dadosI, dadosII):
    combined_list=[]
    combined_list.extend(dadosI)
    combined_list.extend(dadosII)
    return combined_list

# Caminhos dos arquivos JSON e CSV
path_json = "Pipeline/Documentos/Setores/unprocessed-data/files-comp-I.json"
path_csv = "Pipeline/Documentos/Setores/unprocessed-data/files-comp-II.csv"

# Lê o arquivo JSON e imprime o primeiro item da lista
dados_json = leitura_dados(path_json, "json")
nome_colunas_json = get_columns(dados_json)
tamanho_dados_json = size_data(dados_json)
print(f"Nome colunas dados JSON: {nome_colunas_json}")
print(f"Tamanho dos dados JSON: {tamanho_dados_json}")

# Lê o arquivo CSV e imprime o primeiro item da lista
dados_csv = leitura_dados(path_csv, "csv")
nome_colunas_csv = get_columns(dados_csv)
tamanho_dados_csv = size_data(dados_csv)
print(f"Nome colunas dados CSV: {nome_colunas_csv}")
print(f"Tamanho dos dados CSV: {tamanho_dados_csv}")

# Mapeamento das chaves para renomeação
key_mapping = {
    "Nome do Item": "Nome do Produto",
    "Classificação do Produto": "Categoria do Produto",
    "Valor em Reais (R$)": "Preço do Produto (R$)",
    "Quantidade em Estoque": "Quantidade em Estoque",
    "Nome da Loja": "Filial",
    "Data da Venda": "Data da Venda"
}

# Função para renomear as colunas com base no mapeamento
def renaming_columns(dados, key_mapping):
    new_dados_csv = []
    for old_dict in dados:
        dict_temp = {}
        for old_key, value in old_dict.items():
            # Verifica se a chave antiga está no mapeamento
            if old_key in key_mapping:
                new_key = key_mapping[old_key]
                dict_temp[new_key] = value
            else:
                # Se a chave antiga não estiver no mapeamento, mantém a chave original
                dict_temp[old_key] = value
        new_dados_csv.append(dict_temp)
    
    return new_dados_csv

# Renomeia as colunas dos dados CSV
dados_csv = renaming_columns(dados_csv, key_mapping)
nome_colunas_csv = get_columns(dados_csv)
print(f"Nome colunas dados CSV após renomeação: {nome_colunas_csv}")

dados_merge=join(dados_json, dados_csv)
nome_colunas_merge=get_columns(dados_merge)
tamanho_dados_merge=size_data(dados_merge)

print(nome_colunas_merge)
print(tamanho_dados_merge)
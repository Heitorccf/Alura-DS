import json
import csv
import os

from data_handling import Dados

# # Função para ler um arquivo JSON e retornar os dados
# def leitura_json(path_json):
#     """
#     Lê os dados de um arquivo JSON e retorna como uma lista/dicionário.
#     """
#     with open(path_json, "r") as file:
#         return json.load(file)  # Carrega e retorna os dados do arquivo JSON


# # Função para ler um arquivo CSV e retornar os dados
# def leitura_csv(path_csv):
#     """
#     Lê os dados de um arquivo CSV e retorna como uma lista de dicionários.
#     """
#     dados_csv = []
#     with open(path_csv, "r") as file:
#         reader = csv.DictReader(file, delimiter=",")  # Lê o CSV como dicionário
#         for row in reader:
#             dados_csv.append(row)  # Adiciona cada linha à lista
#     return dados_csv


# # Função que decide qual tipo de arquivo ler (JSON ou CSV) baseado na extensão informada
# def leitura_dados(path, tipo_arquivo):
#     """
#     Decide qual tipo de arquivo ler, JSON ou CSV, com base na extensão do arquivo.
#     """
#     if tipo_arquivo == "csv":
#         return leitura_csv(path)
#     elif tipo_arquivo == "json":
#         return leitura_json(path)


# Função para obter os nomes das colunas dos dados
# def get_columns(dados):
#     """
#     Retorna uma lista com os nomes das colunas (chaves) do último item dos dados.
#     """
#     if dados:
#         return list(dados[-1].keys())  # Pega as chaves do último item da lista
#     return []


# Função para obter o tamanho dos dados
def size_data(dados):
    """
    Retorna o número de itens (linhas) nos dados.
    """
    return len(dados)


# Função para combinar (fazer join) de duas listas de dados
def join(dadosI, dadosII):
    """
    Combina (faz o join) de duas listas de dados.
    """
    return dadosI + dadosII  # Une as duas listas


# Função para transformar os dados em formato de tabela
def transformando_dados_tabela(dados, nomes_colunas):
    """
    Converte uma lista de dicionários em uma tabela (lista de listas),
    com a primeira linha contendo os nomes das colunas.
    """
    dados_combinados_tabela = [nomes_colunas]  # Adiciona cabeçalhos (nomes das colunas)

    for row in dados:
        linha = [row.get(coluna, "Indisponível") for coluna in nomes_colunas]  # Preenche a linha
        dados_combinados_tabela.append(linha)

    return dados_combinados_tabela


# Função para renomear as colunas com base em um dicionário de mapeamento
# def renaming_columns(dados, key_mapping):
#     """
#     Renomeia as colunas de um dicionário com base em um mapeamento de chaves.
#     """
#     new_dados = []
#     for old_dict in dados:
#         dict_temp = {}
#         for old_key, value in old_dict.items():
#             new_key = key_mapping.get(old_key, old_key)  # Renomeia ou mantém a chave
#             dict_temp[new_key] = value
#         new_dados.append(dict_temp)
#     return new_dados


# Função para salvar os dados combinados em um arquivo CSV
def salvando_dados(dados, path):
    """
    Salva uma lista de listas (tabela) em um arquivo CSV.
    """
    with open(path, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(dados)


# Caminhos dos arquivos JSON e CSV (corrigidos com base na localização do script)
base_dir = os.path.dirname(os.path.abspath(__file__))  # Diretório base onde o script está
path_json = os.path.join(base_dir, "../unprocessed-data/files-comp-I.json")
path_csv = os.path.join(base_dir, "../unprocessed-data/files-comp-II.csv")

dados_empresaI=Dados(path_json, "json")
print(dados_empresaI.nome_colunas)

dados_empresaII=Dados(path_csv, "csv")
print(dados_empresaII.nome_colunas)

# # Mapeamento das chaves para renomeação
key_mapping = {
    "Nome do Item": "Nome do Produto",
    "Classificação do Produto": "Categoria do Produto",
    "Valor em Reais (R$)": "Preço do Produto (R$)",
    "Quantidade em Estoque": "Quantidade em Estoque",
    "Nome da Loja": "Filial",
    "Data da Venda": "Data da Venda"
}

dados_empresaII.renaming_columns(key_mapping)
print(dados_empresaII.nome_colunas)


# # Lendo dados dos arquivos JSON e CSV
# dados_json = leitura_dados(path_json, "json")
# dados_csv = leitura_dados(path_csv, "csv")

# # Obtendo informações dos dados JSON
# nome_colunas_json = get_columns(dados_json)
# tamanho_dados_json = size_data(dados_json)
# print(f"Nome colunas dados JSON: {nome_colunas_json}")
# print(f"Tamanho dos dados JSON: {tamanho_dados_json}")

# # Renomeando colunas dos dados CSV e obtendo informações
# dados_csv = renaming_columns(dados_csv, key_mapping)
# nome_colunas_csv = get_columns(dados_csv)
# tamanho_dados_csv = size_data(dados_csv)
# print(f"Nome colunas dados CSV após renomeação: {nome_colunas_csv}")
# print(f"Tamanho dos dados CSV: {tamanho_dados_csv}")

# # Unindo (join) os dados JSON e CSV
# dados_merge = join(dados_json, dados_csv)
# nome_colunas_merge = get_columns(dados_merge)
# tamanho_dados_merge = size_data(dados_merge)
# print(f"Nome colunas dados combinados: {nome_colunas_merge}")
# print(f"Tamanho dos dados combinados: {tamanho_dados_merge}")

# # Transformando os dados combinados em tabela
# dados_merge_tabela = transformando_dados_tabela(dados_merge, nome_colunas_merge)

# # Caminho para salvar os dados combinados (corrigido)
# path_dados_combinados = os.path.join(base_dir, "../processed-data/combined-data.csv")

# # Salvando os dados combinados no arquivo CSV
# salvando_dados(dados_merge_tabela, path_dados_combinados)
# print(f"Dados combinados salvos em: {path_dados_combinados}")
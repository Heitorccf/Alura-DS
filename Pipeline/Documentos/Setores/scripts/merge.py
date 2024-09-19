import json
import csv
import os
from data_handling import Dados

# Define o caminho base onde o script está localizado
base_dir = os.path.dirname(os.path.abspath(__file__))

# Define o caminho dos arquivos JSON e CSV
path_json = os.path.join(base_dir, "../unprocessed-data/files-comp-I.json")
path_csv = os.path.join(base_dir, "../unprocessed-data/files-comp-II.csv")

# Criação da instância da classe Dados para o arquivo JSON
dados_empresaI = Dados(path_json, "json")
print(dados_empresaI.nome_colunas)  # Exibe as colunas dos dados JSON
print(dados_empresaI.qtd_linhas)    # Exibe a quantidade de linhas do arquivo JSON

# Criação da instância da classe Dados para o arquivo CSV
dados_empresaII = Dados(path_csv, "csv")
print(dados_empresaII.nome_colunas)  # Exibe as colunas dos dados CSV
print(dados_empresaII.qtd_linhas)    # Exibe a quantidade de linhas do arquivo CSV

# Mapeamento de colunas para renomeação
key_mapping = {
    "Nome do Item": "Nome do Produto",
    "Classificação do Produto": "Categoria do Produto",
    "Valor em Reais (R$)": "Preço do Produto (R$)",
    "Quantidade em Estoque": "Quantidade em Estoque",
    "Nome da Loja": "Filial",
    "Data da Venda": "Data da Venda"
}

# Aplica a renomeação das colunas no arquivo CSV usando o mapeamento fornecido
dados_empresaII.renaming_columns(key_mapping)
print(dados_empresaII.nome_colunas)  # Exibe as novas colunas após a renomeação

# Combina os dados do JSON e CSV em uma única estrutura
dados_merge = dados_empresaI.join(dados_empresaII)
print("Dados Combinados:")
print(dados_merge.nome_colunas)  # Exibe as colunas combinadas dos dados
print(dados_merge.qtd_linhas)    # Exibe a quantidade de linhas combinadas

# Define o caminho para salvar os dados combinados
path_dados_combinados = os.path.join(base_dir, "../processed-data/combined-data.csv")

# Salva os dados combinados no arquivo CSV
dados_merge.salvando_dados(path_dados_combinados)
print(f"Dados combinados salvos em: {path_dados_combinados}")
import json
import csv

class Dados:
    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados
        self.dados=self.leitura_dados()

    def leitura_json(self):
        """
        Lê os dados de um arquivo JSON e retorna como uma lista/dicionário.
        """
        try:
            with open(self.path, "r") as file:
                return json.load(file)  # Carrega e retorna os dados do arquivo JSON
        except FileNotFoundError:
            print(f"Erro: O arquivo {self.path} não foi encontrado.")
        except json.JSONDecodeError:
            print("Erro: O arquivo não está em um formato JSON válido.")

    def leitura_csv(self):
        """
        Lê os dados de um arquivo CSV e retorna como uma lista de dicionários.
        """
        dados_csv = []
        try:
            with open(self.path, "r") as file:
                reader = csv.DictReader(file, delimiter=",")  # Lê o CSV como dicionário
                for row in reader:
                    dados_csv.append(row)  # Adiciona cada linha à lista
            return dados_csv
        except FileNotFoundError:
            print(f"Erro: O arquivo {self.path} não foi encontrado.")
        except Exception as e:
            print(f"Erro ao ler o arquivo CSV: {e}")

    def leitura_dados(self):
        """
        Decide qual tipo de arquivo ler, JSON ou CSV, com base no tipo de dados informado.
        """
        if self.tipo_dados == "csv":
            return self.leitura_csv()
        elif self.tipo_dados == "json":
            return self.leitura_json()
        else:
            print("Erro: Tipo de arquivo não suportado. Use 'csv' ou 'json'.")
import json
import csv

class Dados:
    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados
        self.dados = self.leitura_dados()
        self.nome_colunas = self.get_columns()
        self.qtd_linhas = self.size_data()

    def leitura_json(self):
        try:
            with open(self.path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Erro: O arquivo {self.path} não foi encontrado.")
        except json.JSONDecodeError:
            print("Erro: O arquivo não está em um formato JSON válido.")

    def leitura_csv(self):
        dados_csv = []
        try:
            with open(self.path, "r") as file:
                reader = csv.DictReader(file, delimiter=",")
                for row in reader:
                    dados_csv.append(row)
            return dados_csv
        except FileNotFoundError:
            print(f"Erro: O arquivo {self.path} não foi encontrado.")
        except Exception as e:
            print(f"Erro ao ler o arquivo CSV: {e}")

    def leitura_dados(self):
        if self.tipo_dados == "csv":
            return self.leitura_csv()
        elif self.tipo_dados == "json":
            return self.leitura_json()
        elif self.tipo_dados == "list":
            return self.path  # Retorna a lista passada
        else:
            print("Erro: Tipo de arquivo não suportado. Use 'csv', 'json' ou 'list'.")

    def get_columns(self):
        if self.dados:
            return list(self.dados[0].keys())
        return []

    def renaming_columns(self, key_mapping):
        new_dados = []
        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                new_key = key_mapping.get(old_key, old_key)
                dict_temp[new_key] = value
            new_dados.append(dict_temp)
        self.dados = new_dados  # Atualiza os dados da instância
        self.nome_colunas = self.get_columns()  # Atualiza os nomes das colunas

    def size_data(self):
        return len(self.dados)

    def join(self, other):
        combined_list = self.dados + other.dados  # Combina os dados de ambas as instâncias
        return Dados(combined_list, "list")  # Retorna um novo objeto Dados com a lista combinada
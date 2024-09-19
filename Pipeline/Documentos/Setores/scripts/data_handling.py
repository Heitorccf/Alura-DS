import json
import csv

class Dados:
    def __init__(self, path, tipo_dados):
        """
        Inicializa a classe Dados, carregando o arquivo (JSON ou CSV) e configurando
        as propriedades como nome das colunas e quantidade de linhas.
        """
        self.path = path
        self.tipo_dados = tipo_dados
        self.dados = self.leitura_dados()
        self.nome_colunas = self.get_columns()  # Armazena os nomes das colunas
        self.qtd_linhas = self.size_data()      # Armazena a quantidade de linhas

    def leitura_json(self):
        """
        Lê e retorna os dados de um arquivo JSON. 
        Trata possíveis erros de arquivo não encontrado ou JSON inválido.
        """
        try:
            with open(self.path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Erro: O arquivo {self.path} não foi encontrado.")
        except json.JSONDecodeError:
            print("Erro: O arquivo não está em um formato JSON válido.")

    def leitura_csv(self):
        """
        Lê e retorna os dados de um arquivo CSV.
        Cada linha do CSV é lida como um dicionário.
        """
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
        """
        Decide qual método de leitura usar com base no tipo de arquivo (JSON ou CSV).
        Também aceita listas de dicionários como entrada.
        """
        if self.tipo_dados == "csv":
            return self.leitura_csv()
        elif self.tipo_dados == "json":
            return self.leitura_json()
        elif self.tipo_dados == "list":
            return self.path  # Se os dados forem passados como lista, apenas os retorna
        else:
            print("Erro: Tipo de arquivo não suportado. Use 'csv', 'json' ou 'list'.")

    def get_columns(self):
        """
        Retorna uma lista com os nomes das colunas (chaves) da primeira linha dos dados.
        Se não houver dados, retorna uma lista vazia.
        """
        if self.dados:
            return list(self.dados[0].keys())  # Pega as chaves da primeira linha
        return []

    def renaming_columns(self, key_mapping):
        """
        Renomeia as colunas dos dados conforme um mapeamento fornecido. 
        Atualiza tanto os dados quanto os nomes das colunas.
        """
        new_dados = []
        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                new_key = key_mapping.get(old_key, old_key)  # Usa o mapeamento ou mantém a chave original
                dict_temp[new_key] = value
            new_dados.append(dict_temp)
        self.dados = new_dados  # Atualiza os dados com as novas chaves
        self.nome_colunas = self.get_columns()  # Atualiza as colunas após renomeação

    def size_data(self):
        """
        Retorna o número de linhas dos dados.
        """
        return len(self.dados)

    def join(self, other):
        """
        Combina os dados desta instância com os dados de outra instância.
        Retorna um novo objeto Dados com o resultado combinado.
        """
        combined_list = self.dados + other.dados  # Combina as duas listas de dados
        return Dados(combined_list, "list")  # Retorna um novo objeto 'Dados' com o tipo 'list'
    
    def transformando_dados_tabela(self):
        """
        Converte os dados em formato de lista de dicionários para uma tabela (lista de listas),
        com a primeira linha contendo os nomes das colunas.
        """
        dados_combinados_tabela = [self.nome_colunas]  # Cabeçalho com os nomes das colunas

        # Preenche as linhas da tabela com os dados correspondentes às colunas
        for row in self.dados:
            linha = [row.get(coluna, "Indisponível") for coluna in self.nome_colunas]
            dados_combinados_tabela.append(linha)

        return dados_combinados_tabela
    
    def salvando_dados(self, path):
        """
        Salva os dados formatados como tabela (lista de listas) em um arquivo CSV.
        """
        dados_combinados_tabela = self.transformando_dados_tabela()  # Converte para formato de tabela
        with open(path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinados_tabela)  # Escreve os dados no CSV
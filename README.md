# **Pipeline de Dados com Python e Orientação a Objetos**

Este repositório contém os exercícios e projetos desenvolvidos durante o curso de **Engenharia de Dados** oferecido pela **Alura**. Ao longo do curso, foi construída uma solução para automatizar o processo de transformação de dados utilizando Python, com ênfase em boas práticas de **Orientação a Objetos (POO)** e na construção de pipelines modulares e reutilizáveis.

## **Visão Geral do Projeto**

O objetivo deste projeto é desenvolver um **pipeline de dados** eficiente e flexível, que possa ser aplicado a diferentes cenários de manipulação e transformação de dados. O pipeline processa arquivos JSON e CSV, combinando informações de múltiplas fontes, para gerar um arquivo final de dados processados. A implementação foca na modularidade do código, permitindo que novos módulos e funcionalidades sejam facilmente adicionados ou ajustados conforme a necessidade.

Este projeto reflete práticas que são essenciais em um ambiente de **Engenharia de Dados**, onde a automação, a reutilização de código e a organização eficiente são chave para o sucesso de operações escaláveis.

## **O que você aprenderá neste projeto**

1. **Construção de Pipeline de Dados Automatizado**  
   Com o uso de Python, o pipeline lida com diferentes formatos de dados (JSON e CSV) e aplica transformações automáticas, gerando um arquivo final consolidado.
   
2. **Aplicação de Princípios de Orientação a Objetos (POO)**  
   A refatoração do código usa conceitos de POO para garantir uma maior organização, clareza e reutilização, facilitando futuras expansões e a manutenção do pipeline.

3. **Transformação e Manipulação de Dados**  
   O pipeline automatiza tarefas como: leitura de arquivos, junção de dados, renomeação de colunas e exportação de arquivos processados. Isso tudo é feito através de código Python limpo e bem estruturado.

4. **Boas Práticas de Programação**  
   Cada módulo do pipeline foi desenvolvido com foco em boas práticas, como a **separação de responsabilidades**, **modularização** e **testes de validação**, garantindo um código de fácil manutenção.

5. **Documentação e Análise de Dados**  
   Além da implementação, notebooks interativos são usados para explicar e documentar as principais etapas do processo de desenvolvimento do pipeline, incluindo análises exploratórias e detalhamento das decisões técnicas tomadas.

## **Estrutura do Repositório**

- **notebooks/**: Contém notebooks interativos (`.ipynb`) que explicam o funcionamento do pipeline e exploram os dados processados.
  - `explanation.ipynb`: Apresenta uma introdução ao projeto e detalha os conceitos fundamentais de pipeline de dados.
  - `exploitation.ipynb`: Explica a aplicação prática do pipeline nos dados de exemplo, demonstrando os resultados gerados.
  
- **processed-data/**: Diretório onde os arquivos de dados processados são armazenados.
  - `combined-data.csv`: Arquivo resultante da junção e transformação dos dados.

- **scripts/**: Diretório com os scripts Python utilizados para a construção do pipeline.
  - `data_handling.py`: Contém as funções e classes responsáveis pela manipulação e transformação dos dados.
  - `merge.py`: Script principal para execução da fusão dos dados de diferentes fontes.

- **unprocessed-data/**: Diretório com os arquivos de dados brutos utilizados para o processamento.
  - `files-comp-I.json`: Arquivo JSON de exemplo.
  - `files-comp-II.csv`: Arquivo CSV de exemplo.

- **README.md**: Este documento que explica o propósito e a estrutura do projeto.

## **Tecnologias Utilizadas**

- **Linguagem**: Python 3.x  
- **Bibliotecas**:
  - **Pandas**: Manipulação de dados tabulares.
  - **NumPy**: Suporte a operações numéricas eficientes.
  - **CSV** e **JSON**: Para leitura e escrita de dados nos formatos CSV e JSON.

## **Benefícios do Projeto**

Este pipeline oferece uma estrutura clara e escalável para automatizar processos de dados, uma prática essencial em times de Engenharia de Dados. A modularidade do código facilita tanto a manutenção quanto a adaptação para novos cenários. Profissionais e empresas que buscam soluções para processar grandes volumes de dados de maneira eficiente encontrarão aqui uma abordagem sólida e adaptável às necessidades reais de negócio.

## **Colaboração e Contato**

Se você tem interesse em colaborar, melhorar ou utilizar esse projeto em um ambiente real, fique à vontade para abrir issues, enviar pull requests ou entrar em contato diretamente.

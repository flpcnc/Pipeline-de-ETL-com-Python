# Projeto de Pipeline de ETL com Python

## Descrição
Este projeto foi desenvolvido como parte do desafio de construir um pipeline de ETL (Extração, Transformação e Carga) com Python. O objetivo é extrair dados de um arquivo de texto, transformá-los em um formato adequado e carregá-los em um arquivo CSV.

## Componentes do Projeto
O projeto consiste nos seguintes componentes:

1. **Extrair (E)**: O arquivo de origem é `temp_umidade_DHT22.txt`, que contém dados de temperatura e umidade adquiridos de um sensor DHT22.

2. **Transformar (T)**: Utilizamos expressões regulares (regex) para identificar e extrair os valores de temperatura e umidade de cada linha do arquivo. Os dados extraídos são então processados e armazenados em listas.

3. **Carregar (L)**: Os dados transformados são carregados em um arquivo CSV chamado `dados_temp_umidade.csv` e em um DataFrame Pandas. O arquivo CSV é criado para facilitar a análise e compartilhamento dos dados.

## Pré-Requisitos
- Python (3.x recomendado)
- Bibliotecas Python: re, pandas

## Como Usar
1. Clone o repositório para sua máquina local.
2. Certifique-se de que o arquivo `temp_umidade_DHT22.txt` esteja na mesma pasta que o código.
3. Execute o código Python.
4. Os dados de temperatura e umidade serão extraídos, transformados e carregados em um arquivo CSV.
5. Os resultados podem ser encontrados no arquivo `dados_temp_umidade.csv`.

## Contribuições
Contribuições são bem-vindas. Sinta-se à vontade para abrir issues e pull requests para melhorias ou correções.


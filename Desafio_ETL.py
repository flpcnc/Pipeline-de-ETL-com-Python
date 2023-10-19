import re
import pandas as pd

temperaturas = []
umidades = []

                            # ETAPA EXTRACAO

# Abre o arquivo para leitura
with open('temp_umidade_DHT22.txt', 'r', encoding='utf-8') as file:
    linhas = file.readlines()


                            # ESTAPA TRANSFORMACAO
    
    for linha in linhas:
        print(linha)  # Exibe as linhas para verificar

        # Use regex para encontrar os valores de temperatura e umidade
        match = re.search(r'Temperatura: (\d+\.\d+)°C \| Umidade: (\d+\.\d+)%', linha)
        if match:
            temperatura = float(match.group(1))
            umidade = float(match.group(2))
            temperaturas.append(temperatura)
            umidades.append(umidade)


# Exibe as listas de temperaturas e umidades
print("Temperaturas:", temperaturas)
print("Umidades:", umidades)

                            # ETAPA CARGA

# Cria um DataFrame a partir das listas de temperaturas e umidades
df = pd.DataFrame({'Temperatura (C)': temperaturas, 'Umidade (%)': umidades})

# Salva os dados em um arquivo CSV
df.to_csv('dados_temp_umidade.csv', index=False)

# Exibe as primeiras linhas do DataFrame
print(df.head())

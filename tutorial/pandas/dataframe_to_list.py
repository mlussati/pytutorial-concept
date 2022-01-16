import pandas as pd

# Principal repository of data
# https://github.com/cs109
url="https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"


df = pd.read_csv(url)

# Total records dataset
print('Total records: ', len(df))

# Para converter uma coluna em lista
# Metodo usado é o to_list para converter uma coluna em lista
print(df['Country'].to_list())

cabecalho = df.columns.values.tolist()
corpo = df.values.tolist()
corpo.insert(0, cabecalho)

print(corpo)
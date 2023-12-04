import pandas as pd

# Substitua 'seu_arquivo.csv' pelo nome do seu arquivo CSV
nome_do_arquivo = 'arquivo_saida.csv'

# Carregue o arquivo CSV em um DataFrame
df = pd.read_csv(nome_do_arquivo)

# Especifique as colunas que deseja excluir
colunas_para_excluir = ['latitude', 'longitude']

# Remova as colunas do DataFrame
df = df.drop(columns=colunas_para_excluir)

# Salve o DataFrame modificado de volta no arquivo CSV
df.to_csv(nome_do_arquivo, index=False)

print(f'As colunas {colunas_para_excluir} foram removidas com sucesso do arquivo {nome_do_arquivo}.')

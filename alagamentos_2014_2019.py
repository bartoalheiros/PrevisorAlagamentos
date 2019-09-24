# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv('Alagamentos_2013_2019_Tratado.csv')

#separando o dia do campo data
#df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')
#df['Dia'] = df['Data'].dt.day

print(df)

#salvar como csv
#df.to_csv(r'Path where you want to store the exported CSV file\File Name.csv')

# Risco 1:
# Macaxeira, Apipucos, Água Fria, Imbiribeira, Cohab, Casa Amarela, Caçote
# Areias    

# substitui valores em uma coluna
#novodf = antigodf.apply(lambda x: x.replace('/','0'))
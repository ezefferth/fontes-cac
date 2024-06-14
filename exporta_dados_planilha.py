

import pandas as pd

excel_file = 'Valores_Lancados_TCRS.xlsx'
coluna_excel = 'Imóvel'
dados_excel = pd.read_excel(excel_file)[coluna_excel].dropna()

dados_excel_set = set(dados_excel)


with open('imoveis.txt', 'w') as file:
  for insc in dados_excel:
    if int(insc):
      aux = int(insc)
      file.write(f'{aux}\n')

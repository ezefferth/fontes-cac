import pandas as pd

with open('Dourados_TCRS_Arrecadação_.txt', 'r') as file:
  linhas_a= file.readlines()
  
with open('arquivo_sem_duplicatas_teste.txt', 'r') as file:
  linhas= file.readlines()

excel_file = 'Valores_Lancados_TCRS.xlsx'
coluna_excel = 'Insc. Imob.'
dados_excel = pd.read_excel(excel_file)[coluna_excel]


count = 0
count_not = 0

with open('imoveis_nao_gerados.txt', 'w') as file:
  for insc in dados_excel:
    if not any(insc.strip() in linha for linha in linhas) and not any(insc.strip() in linha for linha in linhas_a):
      file.write(f'{insc}\n')
      count += 1
    else:
      count_not += 1

print(f'Total de valores não encontrados: {count}')
print(f'Total de valores encontrados: {count_not}')
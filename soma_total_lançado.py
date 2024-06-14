
with open('Dourados_TCRS_Arrecadação_.txt', 'r') as file:
  linhas_a= file.readlines()
  
  
with open('arquivo_sem_duplicatas_teste.txt', 'r') as file:
  linhas_r = file.readlines()
  
  
def limpar_e_converter(valor_str):

  valor_str = valor_str.lstrip()

  valor_str = valor_str.replace(',', '.')

  partes = valor_str.split('.')
  if len(partes) > 2:
    valor_str = ''.join(partes[:-1]) + '.' + partes[-1]
  return float(valor_str)
  


valor_total = 0

  
for linha in linhas_r:
  valor1 = limpar_e_converter(linha[1504:1518])
  valor2 = 0.0
  if linha[1882:1893] != '           ':
    valor2 = limpar_e_converter(linha[1882:1893])
  valor3 = 0.0
  if linha[2345:2356] != '           ':
    valor3 = limpar_e_converter(linha[2345:2356])
  valor4 = 0.0
  if linha[2808:2819] != '           ':
    valor4 = limpar_e_converter(linha[2808:2819])
  valor5 = 0.0
  if linha[3271:3282] != '           ':
    valor5 = limpar_e_converter(linha[3271:3282])
  valor6 = 0.0
  if linha[3734:3745] != '           ':  
    valor6 = limpar_e_converter(linha[3271:3282])
    
  valor_total+= valor1 + valor2 + valor3 + valor4 + valor5 + valor6
  
for linha in linhas_a:
  valor1 = limpar_e_converter(linha[1419:1430])
  valor2 = 0.0
  if linha[1882:1893] != '           ':
    valor2 = limpar_e_converter(linha[1882:1893])
  valor3 = 0.0
  if linha[2345:2356] != '           ':
    valor3 = limpar_e_converter(linha[2345:2356])
  valor4 = 0.0
  if linha[2808:2819] != '           ':
    valor4 = limpar_e_converter(linha[2808:2819])
  valor5 = 0.0
  if linha[3271:3282] != '           ':
    valor5 = limpar_e_converter(linha[3271:3282])
  valor6 = 0.0
  if linha[3734:3745] != '           ':  
    valor6 = limpar_e_converter(linha[3271:3282])
    
  valor_total+= valor1 + valor2 + valor3 + valor4 + valor5 + valor6
  
print(valor_total)
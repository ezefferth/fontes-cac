from collections import Counter

# Lê o arquivo e conta as ocorrências de cada linha
with open('_1Complemento_Dourados_IPTU2025_Imobiliaria_ComRegistro.txt', 'r') as file:
  linhas1 = file.readlines()
with open('_2Complemento_02_Dourados_IPTU2025_Correios_ComRegistro.txt', 'r') as file:
  linhas2 = file.readlines()
with open('_3Complemento_01_Dourados_IPTU2025_Correios_ComRegistro.txt', 'r') as file:
  linhas3 = file.readlines()
with open('_4Dourados_IPTU2025_Imobiliaria_ComRegistro.txt', 'r') as file:
  linhas4 = file.readlines()
with open('_5Dourados_IPTU2025_Correios_ComRegistro.txt', 'r') as file:
  linhas5 = file.readlines()
with open('_6Dourados_Correios_IPTU00102024_Arrecadação.txt', 'r') as file:
  linhas6 = file.readlines()
with open('_7Dourados_Imobiliaria_IPTU00102024_Arrecadação.txt', 'r') as file:
  linhas7 = file.readlines()




# Abre o arquivo de saída para escrever as linhas duplicadas
def duplicadas(linhas):
  contador = Counter(linhas)
  
  count = 0
  count_total = 0
  count2 = 0
  count3 = 0
  count4 = 0
  count5 = 0
  count6 = 0
  count7 = 0
  count8 = 0
  count9 = 0
  for linha, contagem in contador.items():
      if contagem > 1:
        count += 1
        count_total += contagem
        if contagem == 2:
          count2 += 1
        if contagem == 3:
          count3 += 1
        if contagem == 4:
          count4 += 1
        if contagem == 5:
          count5 += 1
        if contagem == 6:
          count6 += 1
        if contagem == 7:
          count7 += 1
        if contagem == 8:
          count8 += 1
        if contagem == 9:
          count9 += 1
        parte1 = linha[9:17]
        parte4 = linha[1504:1515]
        parte2 = linha[26:48]
        parte3 = linha[51:84]
    
        print(f'{parte1}  {parte4}  {parte2}  {parte3} duplicado {contagem} vezes\n')
    
  print(f'\n\n\nTotal de duplicados:          {count}\n')
  print(f'Total de linhas duplicadas:   {count_total}\n')
  print(f'\n\nTotal com 2:                  {count2}\n')
  print(f'Total com 3:                  {count3}\n')
  print(f'Total com 4:                  {count4}\n')
  print(f'Total com 5:                  {count5}\n')
  print(f'Total com 6:                  {count6}\n')
  print(f'Total com 7:                  {count7}\n')
  print(f'Total com 8:                  {count8}\n')
  print(f'Total com 9:                  {count9}\n')
  print(f'Total:                        {count2+count3+count4+count5+count6+count7+count8+count9}\n')
  
  

duplicadas(linhas1)
duplicadas(linhas2)
duplicadas(linhas3)
duplicadas(linhas4)
duplicadas(linhas5)
duplicadas(linhas6)
duplicadas(linhas7)
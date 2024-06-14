from collections import Counter

# Lê o arquivo e conta as ocorrências de cada linha
with open('arquivo_ordenado_final.txt', 'r') as file:
  linhas = file.readlines()

# Conta as ocorrências de cada linha
contador = Counter(linhas)


# Abre o arquivo de saída para escrever as linhas duplicadas
with open('lançamentos_duplicados.txt', 'w') as file:
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
    
        file.write(f'{parte1}  {parte4}  {parte2}  {parte3} duplicado {contagem} vezes\n')
    
  file.write(f'\n\n\nTotal de duplicados:          {count}\n')
  file.write(f'Total de linhas duplicadas:   {count_total}\n')
  file.write(f'\n\nTotal com 2:                  {count2}\n')
  file.write(f'Total com 3:                  {count3}\n')
  file.write(f'Total com 4:                  {count4}\n')
  file.write(f'Total com 5:                  {count5}\n')
  file.write(f'Total com 6:                  {count6}\n')
  file.write(f'Total com 7:                  {count7}\n')
  file.write(f'Total com 8:                  {count8}\n')
  file.write(f'Total com 9:                  {count9}\n')
  file.write(f'Total:                        {count2+count3+count4+count5+count6+count7+count8+count9}\n')
  
  

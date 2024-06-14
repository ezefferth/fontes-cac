
with open('arquivo_ordenado_final.txt', 'r') as file:
#with open('Dourados_TCRS_Arrecadação_.txt', 'r') as file:
  linhas = file.readlines()
  
qtd0 = 0
qtd1 = 0
qtd2 = 0 
qtd3 = 0
qtd4 = 0
qtd5 = 0
qtd6 = 0
qtd7 = 0
qtd8 = 0
qtd9 = 0


with open('qtd_inscicao_imob.txt', 'w') as file:
  for linha in linhas:
    if linha[46:47] == '1':
      qtd1 += 1
    elif linha[46:47] == '2':
      qtd2 += 1
      #file.write(linha[9:17] + '  ' + linha[26:47] + '  ' + linha[51:111] + '\n')
    elif linha[46:47] == '3':
      qtd3 += 1
      #file.write(linha[9:17] + '  ' + linha[26:47] + '  ' + linha[51:111] + '\n')
    elif linha[46:47] == '4':
      qtd4 += 1
      #file.write(linha[9:17] + '  ' + linha[26:47] + '  ' + linha[51:111] + '\n')
    elif linha[46:47] == '5':
      qtd5 += 1
      #file.write(linha[9:17] + '  ' + linha[26:47] + '  ' + linha[51:111] + '\n')
    elif linha[46:47] == '6':
      qtd6 += 1
    elif linha[46:47] == '7':
      qtd7 += 1
    elif linha[46:47] == '8':
      qtd8 += 1
    elif linha[46:47] == '9':
      qtd9 += 1
    elif linha[46:47] == '0':
      qtd0 += 1
      
print('qtd0: ', qtd0)
print('qtd1: ', qtd1)
print('qtd2: ', qtd2)
print('qtd3: ', qtd3)
print('qtd4: ', qtd4)
print('qtd5: ', qtd5)
print('qtd6: ', qtd6)
print('qtd7: ', qtd7)
print('qtd8: ', qtd8)
print('qtd9: ', qtd9)



with open('arquivo_final.txt', 'r') as file:
    linhas = file.readlines()

def extrair_cep_posicao(linha):
    return linha[377:385]

count = 0

with open('arquivo_semEnd___x.txt', 'w') as file:
  for linha in linhas: 
    cep = extrair_cep_posicao(linha)
    if cep == '        ':
      file.write(linha)

with open('arquivo_semEnd.txt', 'w') as file:
  for linha in linhas: 
    cep = extrair_cep_posicao(linha)
    if cep == '        ':
      file.write(str(linha[9:17]) + ' ' + str(linha[26:48]) + ' ' + str(linha[51: 111]) + '\n')
      count += 1

with open('arquivo_soBic.txt', 'w') as file:
  for linha in linhas: 
    cep = extrair_cep_posicao(linha)
    if cep == '        ':
      file.write(str(linha[9:17]) + '\n')

with open('arquivo_semEndComZeros.txt', 'w') as file:
  for linha in linhas: 
    cep = extrair_cep_posicao(linha)
    if cep == '00000000':
      file.write(str(linha[9:17]) + ' ' + str(linha[26:48]) + ' ' + str(linha[51: 111]) + '\n')
      count += 1     


count2 = 0



with open('arquivo_semEnd___x.txt', 'r') as file:
    linhas = file.readlines()

with open('arquivo_semCepComEndereco.txt', 'w') as file:
  for linha in linhas: 
    end = linha[7720:7780]
    #print(end)
    if not end.startswith(' , Nº'):
      file.write(str(linha[9:17]) + ' ' + str(linha[26:48]) + ' ' + str(linha[51: 111]) + '\n')
      count2 += 1



print(count)
print(count2)
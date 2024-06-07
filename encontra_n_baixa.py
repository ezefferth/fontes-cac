
valor = str(input('Digite o que deseja encontrar nos arquivos: '))


with open('arquivo_final.txt', 'r') as file:
  linhas = file.readlines()

for linha in linhas:
  if valor in linha:
    print(linha[8:17]+ '    ' +linha[9250:9320])
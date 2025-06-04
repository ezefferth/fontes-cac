
valor = str(input('Digite o que deseja encontrar nos arquivos: '))


with open('Dourados_IPTU00102024_Unificado.txt', 'r') as file:
  linhas = file.readlines()


for linha in linhas:
  # if valor in linha:
  if valor in linha[8:17]:
    print(linha[8:17]+ '    ' +linha[9250:9320])

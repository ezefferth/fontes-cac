with open('arquivo_final.txt', 'r') as file:
  linhas = file.readlines()

# Função para extrair o CEP de uma linha com base na posição dos caracteres
def extrair_posicao(linha):
  cep = linha[377:385]
  bairro = linha[275:325]
  rua = linha[111:211]
  return (cep, bairro, rua)

# Ordenar as linhas com base nos CEPs
linhas_ordenadas = sorted(linhas, key=lambda x: extrair_posicao(x))

# Escrever as linhas ordenadas em um novo arquivo ou imprimir na tela

""" count=0
for linha in linhas_ordenadas:
  if linha[377:385] != '        ' and linha[377:385] != '00000000' and not str(linha[7720:7820]).startswith(' , Nº'):
    count += 1

print(count) """
with open('arquivo_ordenado_final.txt', 'w') as file:
  for linha in linhas_ordenadas:
    if linha[377:385] != '        ' and linha[377:385] != '00000000' and not str(linha[7720:7820]).startswith(' , Nº'):
      file.write(linha)
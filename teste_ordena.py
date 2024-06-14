with open("imoveis_nao_gerados copy.txt", 'r') as file:
  linhas = file.readlines()
  
  
def extrair_posicao(linha):
  return linha[1:21]  
  
linhas_ordenadas = sorted(linhas, key=lambda x: extrair_posicao(x))

with open("imoveis_nao_gerados_ordenado.txt", 'w') as file:
  for linha in linhas_ordenadas:
    file.write(linha)

valor = str(input('Digite o que deseja encontrar nos arquivos: '))


with open('arquivo_sem_duplicatas_teste.txt', 'r') as file:
  linhas = file.readlines()
with open('Dourados_TCRS_Arrecadação_.txt', 'r') as file:
  linhas_a = file.readlines()

for linha in linhas:
  if valor in linha:
    print(linha[8:17]+ '    ' +linha[9250:9320])
    
for linha in linhas_a:
  if valor in linha: 
    print(linha[8:17]+ '    ' +linha[9250:9320])
    

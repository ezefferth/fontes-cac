
with open('imoveis.txt', 'r') as file:
  imoveis = [linha.strip() for linha in file.readlines()]


with open('Dourados_TCRS_Arrecadação_.txt', 'r') as file:
  linhas_a= file.readlines()
  

with open('arquivo_sem_duplicatas_teste.txt', 'r') as file:
  linhas= file.readlines()
  

count = 0
count_not = 0


with open('imoveis_lancados.txt', 'w') as file:
  for linha in linhas:
    bic = linha[9:17].lstrip('0')
    file.write(f'{bic}\n')
  for linha in linhas_a:
    bic = linha[9:17].lstrip('0')
    file.write(f'{bic}\n')
    
    
with open('imoveis_nao_gerados2.txt', 'w', encoding='utf-8') as file:
    for i in imoveis:
        achou = False
        i_stripped = i.lstrip('0')
        
        for j in linhas:
            if i_stripped == j[9:17].lstrip('0'):
                achou = True
                break
        
        for k in linhas_a:
            if i_stripped == k[9:17].lstrip('0'):
                achou = True
                break
        
        if not achou:
            file.write(f'{i}\n')
            count_not += 1
        else:
            count += 1

print(f'Total de valores não encontrados: {count_not}')
print(f'Total de valores encontrados: {count}')

""" with open('imoveis_nao_gerados2.txt', 'w') as file:
  for bic in imoveis:
    bic_stripped = bic.lstrip('0')
    found_in_linhas = any(bic_stripped == linha[9:17].lstrip('0') for linha in linhas)
    found_in_linhas_a = any(bic_stripped == linha[9:17].lstrip('0') for linha in linhas_a)
    if not found_in_linhas and not found_in_linhas_a:
      file.write(f'{bic}\n')
      count_not += 1
    else:
      count += 1

print(f'Total de valores não encontrados: {count_not}')
print(f'Total de valores encontrados: {count}') """
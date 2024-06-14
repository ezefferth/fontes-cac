from collections import Counter

with open('arquivo_ordenado_teste.txt', 'r') as file:
  linhas = file.readlines()


contador = Counter(linhas)


with open('arquivo_sem_duplicatas_teste.txt', 'w') as file:
  count = 0
  count_total = 0
  count_linhas = 0
  for linha, contagem in contador.items():
      if contagem <= 1:
        file.write(linha)
        count_linhas += 1
      else:
        file.write(linha)
        count += 1
        count_total += contagem
        count_linhas += 1
        
    
print(count)
print(count_total)
print(count_total-count)

print(count_linhas)
print(count_linhas+(count_total-count))

        

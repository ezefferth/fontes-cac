

with open('Dourados_IPTU00102024.txt', 'r') as file:
  linhas = file.readlines()


faixas = {i: 0 for i in range(10000, 260000, 10000)}
# Processar cada linha
for linha in linhas:
    try:
        valor = int(linha[9:17])  # Extrai e converte o valor
        for faixa in range(10000, 260000, 10000):
            if valor < faixa:
                faixas[faixa] += 1
                break  # Evita continuar verificando após encontrar a faixa correta
    except ValueError:
        continue  # Pula linhas que não têm números válidos na faixa especificada

# Exibir resultados
total = 0
with open('resultado_faixas.txt', 'w') as resultado:
    resultado.write("Faixa\tContagem\n")
    for faixa, contagem in faixas.items():
        total += contagem
        resultado.write(f"{faixa} - {contagem}\n")
    
    resultado.write(f"Total = {total}\n")

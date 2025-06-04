# Abre o arquivo e lê todas as linhas
with open('Dourados_Correios_IPTU00102024_Comregistro.txt', 'r') as file:
  linhas = file.readlines()
with open('Dourados_Imobiliaria_IPTU00102024_Comregistro.txt', 'r') as file:
  linhas1 = file.readlines()

valores0 = []
valores1 = []
valores2 = []
valores3 = []
valores4 = []
valores5 = []

# Percorre as linhas e extrai números
def maior_menor(linhas):
  for linha in linhas:
    try:
        # Acessa diretamente a fatia desejada da string (linha)
        valor = linha[9250:9260].strip()  # Remove espaços em branco
        if valor:  # Verifica se não está vazio
            valores0.append(int(valor))
    except (ValueError, IndexError):
        continue  # Ignora erros de conversão ou índice fora do alcance
    try:
        # Acessa diretamente a fatia desejada da string (linha)
        valor = linha[9262:9272].strip()  # Remove espaços em branco
        if valor:  # Verifica se não está vazio
            valores1.append(int(valor))
    except (ValueError, IndexError):
        continue  # Ignora erros de conversão ou índice fora do alcance
    try:
        # Acessa diretamente a fatia desejada da string (linha)
        valor = linha[9274:9284].strip()  # Remove espaços em branco
        if valor:  # Verifica se não está vazio
            valores2.append(int(valor))
    except (ValueError, IndexError):
        continue  # Ignora erros de conversão ou índice fora do alcance
    try:
        # Acessa diretamente a fatia desejada da string (linha)
        valor = linha[9286:9296].strip()  # Remove espaços em branco
        if valor:  # Verifica se não está vazio
            valores3.append(int(valor))
    except (ValueError, IndexError):
        continue  # Ignora erros de conversão ou índice fora do alcance
    try:
        # Acessa diretamente a fatia desejada da string (linha)
        valor = linha[9298:9308].strip()  # Remove espaços em branco
        if valor:  # Verifica se não está vazio
            valores4.append(int(valor))
    except (ValueError, IndexError):
        continue  # Ignora erros de conversão ou índice fora do alcance
    try:
        # Acessa diretamente a fatia desejada da string (linha)
        valor = linha[9310:9320].strip()  # Remove espaços em branco
        if valor:  # Verifica se não está vazio
            valores5.append(int(valor))
    except (ValueError, IndexError):
        continue  # Ignora erros de conversão ou índice fora do alcance


maior_menor(linhas)
print("*Correios com registro*")

print("Maior valor0:", max(valores0))
print("Menor valor0:", min(valores0))
print("\n")
print("Maior valor1:", max(valores1))
print("Menor valor1:", min(valores1))
print("\n")
print("Maior valor2:", max(valores2))
print("Menor valor2:", min(valores2))
print("\n")
print("Maior valor3:", max(valores3))
print("Menor valor3:", min(valores3))
print("\n")
print("Maior valor4:", max(valores4))
print("Menor valor4:", min(valores4))
print("\n")
print("Maior valor5:", max(valores5))
print("Menor valor5:", min(valores5))


maior_menor(linhas1)

print("*Imobiliárias com registro*")

print("Maior valor0:", max(valores0))
print("Menor valor0:", min(valores0))
print("\n")
print("Maior valor1:", max(valores1))
print("Menor valor1:", min(valores1))
print("\n")
print("Maior valor2:", max(valores2))
print("Menor valor2:", min(valores2))
print("\n")
print("Maior valor3:", max(valores3))
print("Menor valor3:", min(valores3))
print("\n")
print("Maior valor4:", max(valores4))
print("Menor valor4:", min(valores4))
print("\n")
print("Maior valor5:", max(valores5))
print("Menor valor5:", min(valores5))

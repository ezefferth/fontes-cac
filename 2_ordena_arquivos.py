# Ler o arquivo e obter as linhas
with open('arquivo_concatenado.txt', 'r') as file:
    linhas = file.readlines()

# Função para extrair o CEP de uma linha com base na posição dos caracteres
# def extrair_bairro(linha):
#     return linha[275:325].strip()

# # Função para extrair o bairro de uma linha com base na posição dos caracteres
# def extrair_cep(linha):
#     return linha[377:385].strip()

# # Função para extrair a rua de uma linha com base na posição dos caracteres
# def extrair_rua(linha):
#     return linha[7720:7820].strip()

def extrair_bic(linha):
    return linha[9:18].strip()


# Ordenar as linhas com base no CEP, depois no bairro e, por fim, na rua
# linhas_ordenadas = sorted(linhas, key=lambda x: (extrair_cep(x), extrair_bairro(x), extrair_rua(x)))
linhas_ordenadas = sorted(linhas, key=lambda x: (extrair_bic(x)))

# linhas_ordenadas = sorted(linhas_ordenadas, key=extrair_cep)

# Escrever as linhas ordenadas em um novo arquivo
with open('arquivo_ordenado.txt', 'w') as file:
    for linha in linhas_ordenadas:
        file.write(linha)
        
        
        
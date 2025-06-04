# Ler o arquivo e obter as linhas
with open('Dourados_Correios_IPTU00102024_Comregistro.txt', 'r') as file:
  linhas = file.readlines()
with open('Dourados_Imobiliaria_IPTU00102024_Comregistro.txt', 'r') as file:
  linhas1 = file.readlines()

# Função para extrair o CEP de uma linha com base na posição dos caracteres
# def extrair_bairro(linha):
#     return linha[275:325].strip()

# # Função para extrair o bairro de uma linha com base na posição dos caracteres
# def extrair_cep(linha):
#     return linha[377:385].strip()

# # Função para extrair a rua de uma linha com base na posição dos caracteres
# def extrair_rua(linha):
#     return linha[7720:7820].strip()

def extrair_baixa(linha):
    return linha[9250:9260].strip()


# Ordenar as linhas com base no CEP, depois no bairro e, por fim, na rua
# linhas_ordenadas = sorted(linhas, key=lambda x: (extrair_cep(x), extrair_bairro(x), extrair_rua(x)))
linhas_ordenadas = sorted(linhas, key=lambda x: (extrair_baixa(x)))
linhas_ordenadas1 = sorted(linhas1, key=lambda x: (extrair_baixa(x)))

# linhas_ordenadas = sorted(linhas_ordenadas, key=extrair_cep)

# Escrever as linhas ordenadas em um novo arquivo
with open('arquivo_ordenado_baixa_correios.txt', 'w') as file:
    for linha in linhas_ordenadas:
        file.write(linha)
with open('arquivo_ordenado_baixa_imobiliarias.txt', 'w') as file:
    for linha in linhas_ordenadas1:
        file.write(linha)
        
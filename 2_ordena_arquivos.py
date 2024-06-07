with open('arquivo_concatenado.txt', 'r') as file:
    linhas = file.readlines()

# Função para extrair o CEP de uma linha com base na posição dos caracteres
def extrair_cep_posicao(linha):
    # A posição do CEP é do caractere 2 ao 9 (considerando a indexação 0)
    return linha[377:385]

# Ordenar as linhas com base nos CEPs
linhas_ordenadas = sorted(linhas, key=lambda x: extrair_cep_posicao(x))

# Escrever as linhas ordenadas em um novo arquivo ou imprimir na tela
with open('arquivo_ordenado.txt', 'w') as file:
    for linha in linhas_ordenadas:
        file.write(linha)

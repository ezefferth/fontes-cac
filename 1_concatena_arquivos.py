import os

# Lista para armazenar todas as linhas dos arquivos
todas_linhas = []

# Ler arquivos de 001 a 016 e armazenar as linhas na lista
for i in range(1, 18):
    arquivo_nome = f'files/Dourados_TCRS_ComRegistro{i:03}.txt'
    if os.path.exists(arquivo_nome):
        with open(arquivo_nome, 'r') as file:
            todas_linhas.extend(file.readlines())


with open('arquivo_concatenado.txt', 'w') as file:
    for linha in todas_linhas:
        file.write(linha)

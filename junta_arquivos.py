# Leitura dos arquivos e extração dos valores únicos
with open('Dourados_Correios_IPTU00102024_Arrecadação.txt', 'r') as file:
    linhas_a = file.readlines()

with open('Dourados_Imobiliaria_IPTU00102024_Arrecadação.txt', 'r') as file:
    linhas = file.readlines()

with open('Dourados_Correios_IPTU00102024_Comregistro.txt', 'r') as file:
    linhas_b = file.readlines()

with open('Dourados_Imobiliaria_IPTU00102024_Comregistro.txt', 'r') as file:
    linhas_c = file.readlines()


with open('Dourados_IPTU00102024_Unificado.txt', 'w') as file:
    file.writelines(linhas_a)  # Escreve as linhas do primeiro arquivo
    file.writelines(linhas)    # Escreve as linhas do segundo arquivo
    file.writelines(linhas_b)  # Escreve as linhas do terceiro arquivo
    file.writelines(linhas_c)  # Escreve as linhas do quarto arquivo
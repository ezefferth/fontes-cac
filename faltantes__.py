# Leitura dos arquivos e preparação dos dados
with open('imoveis.txt', 'r') as file:
    imoveis = {linha.strip().lstrip('0') for linha in file.readlines()}

with open('_1Complemento_Dourados_IPTU2025_Imobiliaria_ComRegistro.txt', 'r') as file:
  linhas1 = file.readlines()
with open('_2Complemento_02_Dourados_IPTU2025_Correios_ComRegistro.txt', 'r') as file:
  linhas2 = file.readlines()
with open('_3Complemento_01_Dourados_IPTU2025_Correios_ComRegistro.txt', 'r') as file:
  linhas3 = file.readlines()
with open('_4Dourados_IPTU2025_Imobiliaria_ComRegistro.txt', 'r') as file:
  linhas4 = file.readlines()
with open('_5Dourados_IPTU2025_Correios_ComRegistro.txt', 'r') as file:
  linhas5 = file.readlines()
with open('_6Dourados_Correios_IPTU00102024_Arrecadação.txt', 'r') as file:
  linhas6 = file.readlines()
with open('_7Dourados_Imobiliaria_IPTU00102024_Arrecadação.txt', 'r') as file:
  linhas7 = file.readlines()


conjunto_total = linhas1+linhas2+linhas3+linhas4+linhas5+linhas6+linhas7

# Inicializar contadores
count = 0
count_not = 0

# Comparar imóveis com os valores no conjunto unificado
with open('imoveis_nao_gerados.txt', 'w', encoding='utf-8') as file:
    for i in imoveis:
        if i not in conjunto_total:
            file.write(f'{i}\n')
            count_not += 1
        else:
            count += 1

# Salvar imóveis lançados
with open('imoveis_gerados.txt', 'w') as file:
    for bic in conjunto_total:
        file.write(f'{bic}\n')

# Exibir resultados
print(f'Total de valores não encontrados: {count_not}')
print(f'Total de valores encontrados: {count}')
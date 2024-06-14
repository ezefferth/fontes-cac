""" with open('Dourados_TCRS_Arrecadação.txt', 'r') as arquivo_ordenado, open('Dourados_TCRS_Arrecadação_.txt', 'w') as arquivo_sem_V2:
    # Ler cada linha do arquivo original
    for linha in arquivo_ordenado:
        # Verificar se a linha contém 'V2.2'
        if 'V2.2' not in linha:
            # Se não contém, escrever a linha no novo arquivo
            arquivo_sem_V2.write(linha) """
with open('arquivo_ordenado.txt', 'r') as arquivo_ordenado, open('arquivo_ordenado_teste.txt', 'w') as arquivo_sem_V2:
    # Ler cada linha do arquivo original
    for linha in arquivo_ordenado:
        # Verificar se a linha contém 'V2.2'
        if 'V2.2' not in linha:
            # Se não contém, escrever a linha no novo arquivo
            arquivo_sem_V2.write(linha)

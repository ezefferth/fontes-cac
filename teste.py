with open("arquivo_ordenado.txt", "r") as f:
    conteudo = f.readlines()


with open("codigos.txt", "w") as file:
    for linha in conteudo:
        cod = linha[0:20].strip()
        file.write(f"{cod}\n")


with open("codigos_pessoasFisicas.txt", "w") as file:
    for linha in conteudo:
        cpfCnpj = linha[220:240].strip()
        if len(cpfCnpj) == 11:
            file.write(f"{cpfCnpj}\n")

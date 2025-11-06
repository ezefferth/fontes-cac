with open("notificacaoAlvaraEfuncionamento_F.txt", "r") as file:
    linhas = file.readlines()


def extrair_bairro(linha):
    return linha[320:360].strip()


def extrair_cep(linha):
    return linha[390:400].strip()


def extrair_rua(linha):
    return linha[250:310].strip()


def extrair_numero(linha):
    return linha[310:320].strip()


linhas_ordenadas = sorted(
    linhas, key=lambda x: (extrair_cep(x), extrair_bairro(x), extrair_rua(x), extrair_numero(x))
)

with open("notificacaoAlvaraEfuncionamento_ordenado_f.txt", "w") as file:
    for linha in linhas_ordenadas:
        # cidade = linha[370:390].strip()
        # if cidade != "DOURADOS":
        #     file.write(linha)
        file.write(linha)

with open("notificacaoAlvaraEfuncionamento.txt", "r", encoding="latin-1") as file:
    linhas = file.readlines()


def extrai_valor(linha):
    # Extrai da posição 550 até 570 (lembrando que o índice inicial é 0)
    valor = linha[550:570].strip()
    # Remove pontos de milhar e substitui vírgula decimal por ponto
    valor = valor.replace(".", "").replace(",", ".")
    return valor


def extrai_valor_atual(linha):
    # Extrai da posição 550 até 570 (lembrando que o índice inicial é 0)
    valor = linha[570:590].strip()
    # Remove pontos de milhar e substitui vírgula decimal por ponto
    valor = valor.replace(".", "").replace(",", ".")
    return valor


soma = 0.0
soma_atual = 0.00
for linha in linhas:
    valor_str = extrai_valor(linha)
    if valor_str:  # Evita tentar converter string vazia
        try:
            soma += float(valor_str)
        except ValueError:
            # Ignora linhas com valores inválidos
            continue

    valor_str = extrai_valor_atual(linha)
    if valor_str:  # Evita tentar converter string vazia
        try:
            soma_atual += float(valor_str)
        except ValueError:
            # Ignora linhas com valores inválidos
            continue


print(f"Soma total dos valores: {soma:,.2f}")
print(f"Soma total corrigidos: {soma_atual:,.2f}")

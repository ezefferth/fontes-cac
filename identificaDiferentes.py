with open('TCRS - Correios Válidos.txt', 'r') as file:
    CInew = file.readlines()

with open('CCold.txt', 'r') as file:
    CIold = file.readlines()

with open('DiferentesCC.txt', 'w') as file:
    for i in CInew:
        achou = False  # deve ser reinicializado a cada nova linha de CInew
        for j in CIold:
            if i[0:100] == j[0:100]:
                achou = True
                break
        if not achou:
            file.write(i)

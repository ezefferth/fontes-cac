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
  
  
baixas = []


def extai_num_baixas(linhas):
  for linha in linhas:
    try:
      baixa = linha[9250:9260].strip()
      if baixa:  
        baixas.append(baixa)
    except (ValueError, IndexError):
        continue
    try:
      baixa = linha[9262:9272].strip()  
      if baixa:  
        baixas.append(baixa)
    except (ValueError, IndexError):
        continue  
    try:
      baixa = linha[9274:9284].strip() 
      if baixa: 
        baixas.append(baixa)
    except (ValueError, IndexError):
        continue  
    try:
      baixa = linha[9286:9296].strip() 
      if baixa: 
        baixas.append(baixa)
    except (ValueError, IndexError):
        continue  
    try:
      baixa = linha[9298:9308].strip()  
      if baixa:  
        baixas.append(baixa)
    except (ValueError, IndexError):
        continue 
    try:
      baixa = linha[9310:9320].strip()  
      if baixa:
        baixas.append(baixa)
    except (ValueError, IndexError):
        continue
      

extai_num_baixas(linhas1)
extai_num_baixas(linhas2)
extai_num_baixas(linhas3)
extai_num_baixas(linhas4)
extai_num_baixas(linhas5)

baixas = [linha.strip() for linha in baixas]
baixas.sort()


with open('baixas_todos_iptu25_segunda_remessa.txt', 'w') as file:
  for linha in baixas:
    file.write(linha+'\n')
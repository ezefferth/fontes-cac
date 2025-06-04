

with open('arquivo_ordenado_final.txt', 'r') as file:
  linhas = file.readlines()
g

qtd1 = 0
qtd2 = 0
qtd3 = 0
qtd4 = 0
qtd5 = 0
qtd6 = 0

qtd_parcela_1_esperado = 0
qtd_parcela_2_esperado = 0
qtd_parcela_3_esperado = 0
qtd_parcela_4_esperado = 0
qtd_parcela_5_esperado = 0
qtd_parcela_6_esperado = 0

qtd_parcela_1_esperado_total = 0
qtd_parcela_2_esperado_total = 0
qtd_parcela_3_esperado_total = 0
qtd_parcela_4_esperado_total = 0
qtd_parcela_5_esperado_total = 0
qtd_parcela_6_esperado_total = 0

valor_errado_total = 0
valor_errado = 0
valor_errado2 = 0
valor_errado3 = 0
valor_errado4 = 0
valor_errado5 = 0
valor_errado6 = 0

def limpar_e_converter(valor_str):

    valor_str = valor_str.lstrip()
 
    valor_str = valor_str.replace(',', '.')

    partes = valor_str.split('.')
    if len(partes) > 2:
        valor_str = ''.join(partes[:-1]) + '.' + partes[-1]
    return float(valor_str)
  
  
def valor_esperado(valor, parcela):
  global qtd_parcela_1_esperado
  global qtd_parcela_2_esperado
  global qtd_parcela_3_esperado
  global qtd_parcela_4_esperado
  global qtd_parcela_5_esperado
  global qtd_parcela_6_esperado
  
  if valor < 20:
    qtd_parcela_1_esperado += 1
    parcela = '1'
    return (f'{valor:.2f}', parcela)
  elif valor/3 <= 10:
    qtd_parcela_2_esperado += 1
    parcela = '2'
    return (f'{valor/2:.2f}', parcela)
  if valor/4 <= 10:
    qtd_parcela_3_esperado += 1
    parcela = '3'
    return (f'{valor/3:.2f}', parcela)
  if valor/5 <= 10:
    qtd_parcela_4_esperado += 1
    parcela = '4'
    return (f'{valor/4:.2f}', parcela)
  if valor/6 <= 10:
    qtd_parcela_5_esperado += 1
    parcela = '5'
    return (f'{valor/5:.2f}', parcela)
  else:
    qtd_parcela_6_esperado += 1
    parcela = '6'
    return (f'{valor/6:.2f}', parcela)

  
    

with open('arquivo_1parcela.txt', 'w') as file:
  with open('arquivo_1parcela_errado.txt', 'w') as file2:
    for linha in linhas:
      if linha[9262:9274] == '            ':
        qtd1 += 1
        valor = linha[1504:1515]
        file.write(linha)
        valor_real = limpar_e_converter(valor)
        parcela = '1'
        if valor_real >= 20:
          valor_errado += 1
        resultado_esperado = valor_esperado(valor_real, parcela)
        file2.write(linha[9:17] + ' ' + linha[26:48] + ' ' + linha[1504:1515] + '   parcela esperada: ' + resultado_esperado[1] + '   valor esperado: '+ resultado_esperado[0] + '\n')
    file2.write('\n' + '\n' +'total de imoveis registrados:        ' + str(qtd1))
    file2.write('\n' + 'total de imoveis errados:            ' + str(valor_errado) + '\n')
    file2.write('\n \n' + 'imoveis com 1 parcela:               ' + str(qtd_parcela_1_esperado) + '\n')
    file2.write('\n' + 'imoveis que deveriam ter 2 parcelas: ' + str(qtd_parcela_2_esperado))
    file2.write('\n' + 'imoveis que deveriam ter 3 parcelas: ' + str(qtd_parcela_3_esperado))
    file2.write('\n' + 'imoveis que deveriam ter 4 parcelas: ' + str(qtd_parcela_4_esperado))
    file2.write('\n' + 'imoveis que deveriam ter 5 parcelas: ' + str(qtd_parcela_5_esperado))
    file2.write('\n' + 'imoveis que deveriam ter 6 parcelas: ' + str(qtd_parcela_6_esperado))
    qtd_parcela_1_esperado_total += qtd_parcela_1_esperado
    qtd_parcela_2_esperado_total += qtd_parcela_2_esperado
    qtd_parcela_3_esperado_total += qtd_parcela_3_esperado
    qtd_parcela_4_esperado_total += qtd_parcela_4_esperado
    qtd_parcela_5_esperado_total += qtd_parcela_5_esperado
    qtd_parcela_6_esperado_total += qtd_parcela_6_esperado
    valor_errado_total += valor_errado
    

qtd_parcela_1_esperado = 0
qtd_parcela_2_esperado = 0
qtd_parcela_3_esperado = 0
qtd_parcela_4_esperado = 0
qtd_parcela_5_esperado = 0
qtd_parcela_6_esperado = 0

with open('arquivo_2parcela.txt', 'w') as file:
  with open('arquivo_2parcela_errado.txt', 'w') as file2:
    for linha in linhas:
      if linha[9262:9274] != '            ' and linha[9274:9286] == '            ':
        qtd2 += 1
        valor = linha[1881:1893]
        file.write(linha)
        valor_real = limpar_e_converter(valor)
        parcela = '2'
        if ((valor_real*2)/3) > 10:
          valor_errado2 += 1
        resultado_esperado = valor_esperado(valor_real*2, parcela)
        file2.write(linha[9:17] + ' ' + linha[26:48] + ' ' + linha[1504:1515] + '   parcela esperada: ' + resultado_esperado[1] + '   valor esperado: '+ resultado_esperado[0] + '\n')
    file2.write('\n' + 'total de valores registrados:        ' + str(qtd2))
    file2.write('\n' + 'total de valores errados:            ' + str(valor_errado2) + '\n')
    file2.write('\n \n' + 'imoveis com 2 parcelas:              ' + str(qtd_parcela_2_esperado) + '\n')
    file2.write('\n' + 'imoveis que deveriam ter 1 parcela:  ' + str(qtd_parcela_1_esperado))
    file2.write('\n' + 'imoveis que deveriam ter 3 parcelas: ' + str(qtd_parcela_3_esperado))
    file2.write('\n' + 'imoveis que deveriam ter 4 parcelas: ' + str(qtd_parcela_4_esperado))
    file2.write('\n' + 'imoveis que deveriam ter 5 parcelas: ' + str(qtd_parcela_5_esperado))
    file2.write('\n' + 'imoveis que deveriam ter 6 parcelas: ' + str(qtd_parcela_6_esperado))
    qtd_parcela_1_esperado_total += qtd_parcela_1_esperado
    qtd_parcela_2_esperado_total += qtd_parcela_2_esperado
    qtd_parcela_3_esperado_total += qtd_parcela_3_esperado
    qtd_parcela_4_esperado_total += qtd_parcela_4_esperado
    qtd_parcela_5_esperado_total += qtd_parcela_5_esperado
    qtd_parcela_6_esperado_total += qtd_parcela_6_esperado
    valor_errado_total += valor_errado2

qtd_parcela_1_esperado = 0
qtd_parcela_2_esperado = 0
qtd_parcela_3_esperado = 0
qtd_parcela_4_esperado = 0
qtd_parcela_5_esperado = 0
qtd_parcela_6_esperado = 0

with open('arquivo_3parcela.txt', 'w') as file:
  with open('arquivo_3parcela_errado.txt', 'w') as file2:
    for linha in linhas:
      if linha[9262:9274] != '            ' and linha[9274:9286] != '            ' and linha[9286:9298] == '            ':
        qtd3 += 1
        valor = linha[1881:1893]
        file.write(linha)
        valor_real = limpar_e_converter(valor)
        parcela = '3'
        if ((valor_real*3)/4) > 10:
          valor_errado3 += 1
        resultado_esperado = valor_esperado(valor_real*3, parcela)
        file2.write(linha[9:17] + ' ' + linha[26:48] + ' ' + linha[1504:1515] + '   parcela esperada: ' + resultado_esperado[1] + '   valor esperado: '+ resultado_esperado[0] + '\n')
    file2.write('\n' + 'total de valores registrados:        ' + str(qtd3))
    file2.write('\n' + 'total de valores errados:            ' + str(valor_errado3) + '\n')
    file2.write('\n \n' + 'imoveis com 3 parcelas:              ' + str(qtd_parcela_3_esperado)+'\n')
    file2.write('\n' + 'imoveis que deveriam ter 1 parcela:  ' + str(qtd_parcela_1_esperado))
    file2.write('\n' + 'imoveis que deveriam ter 2 parcelas: ' + str(qtd_parcela_2_esperado))
    file2.write('\n' + 'imoveis que deveriam ter 4 parcelas: ' + str(qtd_parcela_4_esperado))
    file2.write('\n' + 'imoveis que deveriam ter 5 parcelas: ' + str(qtd_parcela_5_esperado))
    file2.write('\n' + 'imoveis que deveriam ter 6 parcelas: ' + str(qtd_parcela_6_esperado))
    qtd_parcela_1_esperado_total += qtd_parcela_1_esperado
    qtd_parcela_2_esperado_total += qtd_parcela_2_esperado
    qtd_parcela_3_esperado_total += qtd_parcela_3_esperado
    qtd_parcela_4_esperado_total += qtd_parcela_4_esperado
    qtd_parcela_5_esperado_total += qtd_parcela_5_esperado
    qtd_parcela_6_esperado_total += qtd_parcela_6_esperado
    valor_errado_total += valor_errado3
    
qtd_parcela_1_esperado = 0
qtd_parcela_2_esperado = 0
qtd_parcela_3_esperado = 0
qtd_parcela_4_esperado = 0
qtd_parcela_5_esperado = 0
qtd_parcela_6_esperado = 0


with open('arquivo_4parcela.txt', 'w') as file:
  with open('arquivo_4parcela_errado.txt', 'w') as file2:
    for linha in linhas:
      if linha[9262:9274] != '            ' and linha[9274:9286] != '            ' and linha[9286:9298] != '            ' and linha[9298:9310] == '            ':
        qtd4 += 1
        valor = linha[1881:1893]
        file.write(linha)
        valor_real = limpar_e_converter(valor)
        parcela = '4'
        if ((valor_real*4)/5) > 10:
          valor_errado4 += 1
        resultado_esperado = valor_esperado(valor_real*4, parcela)
        file2.write(linha[9:17] + ' ' + linha[26:48] + ' ' + linha[1504:1515] + '   parcela esperada: ' + resultado_esperado[1] + '   valor esperado: '+ resultado_esperado[0] + '\n')
    file2.write('\n' + 'total de valores registrados:        ' + str(qtd4))
    file2.write('\n' + 'total de valores errados:            ' + str(valor_errado4))
    file2.write('\n \n' + 'imoveis com 4 parcelas:              ' + str(qtd_parcela_4_esperado)+'\n')
    file2.write('\n' + 'imoveis que deveriam ter 1 parcela:  ' + str(qtd_parcela_1_esperado))
    file2.write('\n' + 'imoveis que deveriam ter 2 parcelas: ' + str(qtd_parcela_2_esperado))
    file2.write('\n' + 'imoveis que deveriam ter 3 parcelas: ' + str(qtd_parcela_3_esperado))
    file2.write('\n' + 'imoveis que deveriam ter 5 parcelas: ' + str(qtd_parcela_5_esperado))
    file2.write('\n' + 'imoveis que deveriam ter 6 parcelas: ' + str(qtd_parcela_6_esperado))
    qtd_parcela_1_esperado_total += qtd_parcela_1_esperado
    qtd_parcela_2_esperado_total += qtd_parcela_2_esperado
    qtd_parcela_3_esperado_total += qtd_parcela_3_esperado
    qtd_parcela_4_esperado_total += qtd_parcela_4_esperado
    qtd_parcela_5_esperado_total += qtd_parcela_5_esperado
    qtd_parcela_6_esperado_total += qtd_parcela_6_esperado
    valor_errado_total += valor_errado4
    
qtd_parcela_1_esperado = 0
qtd_parcela_2_esperado = 0
qtd_parcela_3_esperado = 0
qtd_parcela_4_esperado = 0
qtd_parcela_5_esperado = 0
qtd_parcela_6_esperado = 0

with open('arquivo_5parcela.txt', 'w') as file:
  with open('arquivo_5parcela_errado.txt', 'w') as file2:
    for linha in linhas:
      if linha[9262:9274] != '            ' and linha[9274:9286] != '            ' and linha[9286:9298] != '            ' and linha[9298:9310] != '            ' and linha[9310:9322] == '            ':
        qtd5 += 1
        valor = linha[1881:1893]
        file.write(linha)
        valor_real = limpar_e_converter(valor)
        parcela = '5'
        if ((valor_real*5)/6) > 10:
          valor_errado5 += 1
        resultado_esperado = valor_esperado(valor_real*5, parcela)
        file2.write(linha[9:17] + ' ' + linha[26:48] + ' ' + linha[1504:1515] + '   parcela esperada: ' + resultado_esperado[1] + '   valor esperado: '+ resultado_esperado[0] + '\n')
    file2.write('\n' + 'total de valores registrados:        ' + str(qtd5))
    file2.write('\n' + 'total de valores errados:            ' + str(valor_errado5))
    file2.write('\n \n' + 'imoveis com 5 parcelas:              ' + str(qtd_parcela_5_esperado)+ '\n')
    file2.write('\n' + 'imoveis que deveriam ter 1 parcela:  ' + str(qtd_parcela_1_esperado))
    file2.write('\n' + 'imoveis que deveriam ter 2 parcelas: ' + str(qtd_parcela_2_esperado))
    file2.write('\n' + 'imoveis que deveriam ter 3 parcelas: ' + str(qtd_parcela_3_esperado))
    file2.write('\n' + 'imoveis que deveriam ter 4 parcelas: ' + str(qtd_parcela_4_esperado))
    file2.write('\n' + 'imoveis que deveriam ter 6 parcelas: ' + str(qtd_parcela_6_esperado))
    qtd_parcela_1_esperado_total += qtd_parcela_1_esperado
    qtd_parcela_2_esperado_total += qtd_parcela_2_esperado
    qtd_parcela_3_esperado_total += qtd_parcela_3_esperado
    qtd_parcela_4_esperado_total += qtd_parcela_4_esperado
    qtd_parcela_5_esperado_total += qtd_parcela_5_esperado
    qtd_parcela_6_esperado_total += qtd_parcela_6_esperado
    valor_errado_total += valor_errado5 

qtd_parcela_1_esperado = 0
qtd_parcela_2_esperado = 0
qtd_parcela_3_esperado = 0
qtd_parcela_4_esperado = 0
qtd_parcela_5_esperado = 0
qtd_parcela_6_esperado = 0
    
with open('arquivo_6parcela.txt', 'w') as file:
  with open('arquivo_6parcela_errado.txt', 'w') as file2:
    for linha in linhas:
      if linha[9262:9274] != '            ' and linha[9274:9286] != '            ' and linha[9286:9298] != '            ' and linha[9298:9310] != '            ' and linha[9310:9322] != '            ':
        qtd6 += 1
        valor = linha[1881:1893]
        file.write(linha)
        valor_real = limpar_e_converter(valor)
        parcela = '6'
        if valor_real < 10:
          valor_errado6 += 1
        resultado_esperado = valor_esperado(valor_real*6, parcela)
        file2.write(linha[9:17] + ' ' + linha[26:48] + ' ' + linha[1504:1515] + '   parcela esperada: ' + resultado_esperado[1] + '   valor esperado: '+ resultado_esperado[0] + '\n')
    file2.write('\n' + 'total de valores registrados:        ' + str(qtd6))
    file2.write('\n' + 'total de valores errados:            ' + str(valor_errado6))
    file2.write('\n \n' + 'imoveis com 6 parcelas:              ' + str(qtd_parcela_6_esperado)+'\n')
    file2.write('\n' + 'imoveis que deveriam ter 1 parcela:  ' + str(qtd_parcela_1_esperado))
    file2.write('\n' + 'imoveis que deveriam ter 2 parcelas: ' + str(qtd_parcela_2_esperado))
    file2.write('\n' + 'imoveis que deveriam ter 3 parcelas: ' + str(qtd_parcela_3_esperado))
    file2.write('\n' + 'imoveis que deveriam ter 4 parcelas: ' + str(qtd_parcela_4_esperado))
    file2.write('\n' + 'imoveis que deveriam ter 5 parcelas: ' + str(qtd_parcela_5_esperado))
    qtd_parcela_1_esperado_total += qtd_parcela_1_esperado
    qtd_parcela_2_esperado_total += qtd_parcela_2_esperado
    qtd_parcela_3_esperado_total += qtd_parcela_3_esperado
    qtd_parcela_4_esperado_total += qtd_parcela_4_esperado
    qtd_parcela_5_esperado_total += qtd_parcela_5_esperado
    qtd_parcela_6_esperado_total += qtd_parcela_6_esperado
    valor_errado_total += valor_errado6
    
    
with open('relatorio_final.txt', 'w') as file:
    t_i = qtd1 + qtd2 + qtd3 + qtd4 + qtd5 + qtd6
    t_i_e = valor_errado + valor_errado2 + valor_errado3 + valor_errado4 + valor_errado5 + valor_errado6
    q1 = qtd_parcela_1_esperado_total
    q2 = qtd_parcela_2_esperado_total
    q3 = qtd_parcela_3_esperado_total
    q4 = qtd_parcela_4_esperado_total
    q5 = qtd_parcela_5_esperado_total
    q6 = qtd_parcela_6_esperado_total
    
    file.write('Total de imóveis:                 ' + str(t_i) + '\n')
    file.write('Total de imóveis com erro:        ' + str(t_i_e) + '\n')
    file.write('Imóveis com 1 parcela esperada:   ' + str(q1) + '\n')
    file.write('Imóveis com 2 parcelas esperadas: ' + str(q2) + '\n')
    file.write('Imóveis com 3 parcelas esperadas: ' + str(q3) + '\n')
    file.write('Imóveis com 4 parcelas esperadas: ' + str(q4) + '\n')
    file.write('Imóveis com 5 parcelas esperadas: ' + str(q5) + '\n')
    file.write('Imóveis com 6 parcelas esperadas: ' + str(q6) + '\n')


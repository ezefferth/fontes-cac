import pandas as pd

def gerar_inserts_from_xlsx(xlsx_file, table_name):
    # Lê o arquivo Excel
    df = pd.read_excel(xlsx_file, engine='openpyxl')
    
    if table_name == 'assunto':
    # Abre um arquivo de saída para salvar os inserts
        with open(f'{table_name}_inserts.sql', 'w', encoding='utf-8') as file:
        # Gera o comando INSERT INTO para cada linha
            for index, row in df.iterrows():
                linha = f"INSERT INTO {table_name} (id, nome, \"categoriaId\", \"createdAt\", \"updatedAt\") VALUES ('{row['id']}', '{row['nome']}', '{row['categoriaId']}', '{row['createdAt']}', '{row['updatedAt']}');\n"
                file.write(linha)
                
    elif table_name == 'categoria' or table_name == 'tipo_patrimonio':
        with open(f'{table_name}_inserts.sql', 'w', encoding='utf-8') as file:
            for index, row in df.iterrows():
                linha = f"INSERT INTO {table_name} (id, nome, \"createdAt\", \"updatedAt\") VALUES ('{row['id']}', '{row['nome']}', '{row['createdAt']}', '{row['updatedAt']}');\n"
                file.write(linha)
                
    elif table_name == 'chamado':
        with open(f'{table_name}_inserts.sql', 'w', encoding='utf-8') as file:
            for index, row in df.iterrows():
                finalizadoPor = 'NULL' if pd.isna(row['finalizadoPor']) or row['finalizadoPor'] == '' else f"'{row['finalizadoPor']}'"
                finishedAt = 'NULL' if pd.isna(row['finishedAt']) or row['finishedAt'] == '' else f"'{row['finishedAt']}'"
                linha = f"INSERT INTO {table_name} (id, \"assuntoId\", \"usuarioId\", \"setorId\", descricao, \"createdAt\", \"updatedAt\", \"finishedAt\", \"prioridadeId\", \"statusId\", \"finalizadoPor\") VALUES ('{row['id']}', '{row['assuntoId']}', '{row['usuarioId']}', '{row['setorId']}', '{row['descricao']}', '{row['createdAt']}', '{row['updatedAt']}', {finishedAt}, '{row['prioridadeId']}', '{row['statusId']}', {finalizadoPor});\n"
                
                file.write(linha)
                
    elif table_name == 'comentario':
        with open(f'{table_name}_inserts.sql', 'w', encoding='utf-8') as file:
            for index, row in df.iterrows():
                linha = f"INSERT INTO {table_name} (id, comentario, \"createdAt\", \"updatedAt\", \"chamadoId\",\"usuarioId\") VALUES ('{row['id']}', '{row['comentario']}','{row['createdAt']}', '{row['updatedAt']}', '{row['chamadoId']}', '{row['usuarioId']}');\n"
                file.write(linha)
                
    elif table_name == 'prioridade' or table_name == 'status':
        with open(f'{table_name}_inserts.sql', 'w', encoding='utf-8') as file:
            for index, row in df.iterrows():
                linha = f"INSERT INTO {table_name} (id, nome, cor, \"createdAt\", \"updatedAt\") VALUES ('{row['id']}', '{row['nome']}', '{row['cor']}','{row['createdAt']}', '{row['updatedAt']}');\n"
                file.write(linha)
                
    elif table_name == 'setor':
        with open(f'{table_name}_inserts.sql', 'w', encoding='utf-8') as file:
            for index, row in df.iterrows():
                linha = f"INSERT INTO {table_name} (id, nome, status, \"createdAt\", \"updatedAt\") VALUES ('{row['id']}', '{row['nome']}', '{row['status']}','{row['createdAt']}', '{row['updatedAt']}');\n"
                file.write(linha)
                
    elif table_name == 'usuario':
        with open(f'{table_name}_inserts.sql', 'w', encoding='utf-8') as file:
            for index, row in df.iterrows():
                avatar = 'NULL' if pd.isna(row['avatar']) or row['avatar'] == '' else f"'{row['avatar']}'"
                status = 'NULL' if pd.isna(row['status']) or row['status'] == '' else f"'{row['status']}'"
                linha = f"INSERT INTO {table_name} (id, nome, \"nomeUsuario\", senha, \"createdAt\", \"updatedAt\", admin, avatar, status) VALUES ('{row['id']}', '{row['nome']}', '{row['nomeUsuario']}', '{row['senha']}', '{row['createdAt']}', '{row['updatedAt']}', '{row['admin']}', {avatar}, {status});\n"
                file.write(linha)

# Caminho para o arquivo Excel
xlsx_file = 'files/assunto.xlsx'  # Substitua pelo caminho do seu arquivo Excel
table_name = 'assunto'  # Nome da tabela no banco de dados
gerar_inserts_from_xlsx(xlsx_file, table_name)


xlsx_file = 'files/categoria.xlsx'
table_name = 'categoria'
gerar_inserts_from_xlsx(xlsx_file, table_name)


xlsx_file = 'files/chamado.xlsx'
table_name = 'chamado'
gerar_inserts_from_xlsx(xlsx_file, table_name)


xlsx_file = 'files/comentario.xlsx'
table_name = 'comentario'
gerar_inserts_from_xlsx(xlsx_file, table_name)


xlsx_file = 'files/prioridade.xlsx'
table_name = 'prioridade'
gerar_inserts_from_xlsx(xlsx_file, table_name)


xlsx_file = 'files/setor.xlsx'
table_name ='setor'
gerar_inserts_from_xlsx(xlsx_file, table_name)


xlsx_file = 'files/status.xlsx'
table_name ='status'
gerar_inserts_from_xlsx(xlsx_file, table_name)


xlsx_file = 'files/tipo_patrimonio.xlsx'
table_name ='tipo_patrimonio'
gerar_inserts_from_xlsx(xlsx_file, table_name)


xlsx_file = 'files/usuario.xlsx'
table_name ='usuario'
gerar_inserts_from_xlsx(xlsx_file, table_name)

print("Arquivo de inserts gerado com sucesso!")

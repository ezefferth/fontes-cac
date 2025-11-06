from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter

from reportlab.platypus import Image
import io
import os
import re


def mascarar_cpf_cnpj(valor: str) -> str:
    """Aplica máscara conforme o tamanho do número: CPF (11) ou CNPJ (14)."""
    if not valor:
        return ""
    numeros = re.sub(r"\D", "", valor)  # mantém apenas dígitos

    if len(numeros) == 11:  # CPF
        return f"{numeros[:3]}.{numeros[3:6]}.{numeros[6:9]}-{numeros[9:]}"
    elif len(numeros) == 14:  # CNPJ
        return f"{numeros[:2]}.{numeros[2:5]}.{numeros[5:8]}/{numeros[8:12]}-{numeros[12:]}"
    else:
        return valor.strip()  # retorna como está se for inválido


def mascarar_cep(valor: str) -> str:
    """Formata o CEP no padrão 00000-000."""
    if not valor:
        return ""
    numeros = re.sub(r"\D", "", valor)
    if len(numeros) == 8:
        return f"{numeros[:5]}-{numeros[5:]}"
    else:
        return valor.strip()


# ====== CONFIGURAÇÕES ======
# ARQUIVO_TXT = "notificacaoAlvaraEfuncionamento.txt"
ARQUIVO_TXT = "arquivo_ordenado.txt"
ARTE_PDF = "CARTA_NOT_DEB_V1.5.pdf"
PASTA_SAIDA = "pdfs_gerados"

if not os.path.exists(PASTA_SAIDA):
    os.makedirs(PASTA_SAIDA)

DADOS_IMOVEL = [
    ("Enumerador", 1, 10),
    ("Código do mobiliário", 11, 30),
    ("Nome do econômico", 31, 130),
    ("Nome fantasia", 131, 230),
    ("CPF/CNPJ", 231, 250),
    ("Tipo logradouro", 251, 260),
    ("Logradouro", 261, 340),
    ("Número", 341, 350),
    ("Complemento", 351, 410),
    ("Bairro", 411, 470),
    ("UF", 471, 480),
    ("Cidade", 481, 520),
    ("CEP", 521, 540),
    ("Endereço completo", 541, 740),
    ("Data de geração", 741, 760),
    ("Valor total", 761, 780),
    ("Valor total corrigido", 781, 800),
]

DEBITO_CAMPOS = [
    ("Ano", 800, 810),
    # ("Abreviatura receita", 811, 820),
    ("Descrição receita", 820, 870),
    ("Parcela", 870, 880),
    ("Data vencimento", 880, 900),
    ("Valor original", 900, 920),
    # ("Valor juro", 921, 940),
    # ("Valor multa", 941, 960),
    ("Valor corrigido", 960, 980),
]

BLOCO_P_INICIO = 800
BLOCO_P_TAMANHO = 180
QTD_BLOCOS = 16


# ====== EXTRAÇÃO ======
def extrair_dados(linha):
    dados = {}
    # ====== Extrai os dados do imóvel ======
    for nome, inicio, fim in DADOS_IMOVEL:
        dados[nome] = linha[inicio - 1 : fim].strip()

    debitos = []
    # ====== Extrai os blocos de débitos ======
    for i in range(QTD_BLOCOS):
        base = BLOCO_P_INICIO + (i * BLOCO_P_TAMANHO)
        bloco = linha[base : base + BLOCO_P_TAMANHO]

        # Ignora blocos vazios
        if bloco.strip() == "":
            continue

        info = {}
        # Corrige os índices para posições relativas dentro do bloco
        for nome, ini, fim in DEBITO_CAMPOS:
            rel_ini = ini - BLOCO_P_INICIO
            rel_fim = fim - BLOCO_P_INICIO
            info[nome] = bloco[rel_ini:rel_fim].strip()

        debitos.append(info)

    return dados, debitos


# ====== GERA A ARTE COM ENDEREÇO ======
def gerar_arte_com_endereco(
    codContrib, contribuinte, nomeFantasia, endereco_texto, endereco_texto2
):
    reader = PdfReader(ARTE_PDF)
    page = reader.pages[0]

    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=A4)
    c.setFont("Helvetica-Bold", 11)

    # POSIÇÃO DO ENDEREÇO NA ARTE (ajuste aqui)
    ##c.drawString(6 * cm, 9.7 * cm, codContrib)
    c.drawString(5 * cm, 9.5 * cm, contribuinte)
    c.drawString(5 * cm, 9 * cm, nomeFantasia)
    c.drawString(5 * cm, 8.5 * cm, endereco_texto)
    c.drawString(5 * cm, 8 * cm, endereco_texto2)
    c.save()
    packet.seek(0)

    overlay = PdfReader(packet)
    page.merge_page(overlay.pages[0])

    writer = PdfWriter()
    writer.add_page(page)
    temp_stream = io.BytesIO()
    writer.write(temp_stream)
    temp_stream.seek(0)
    return temp_stream


# ====== GERA O CORPO DO PDF ======
def gerar_pdf_corpo(dados, debitos):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        leftMargin=1.2 * cm,
        rightMargin=1.2 * cm,
        topMargin=0.5 * cm,
        bottomMargin=0.5 * cm,
    )

    elementos = []
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="titulo",
            fontSize=12,
            alignment=1,
            textColor="#303474",
            fontName="Helvetica-Bold",
        )
    )
    styles.add(ParagraphStyle(name="normal", fontSize=9, leading=12, alignment=0))
    styles.add(
        ParagraphStyle(
            name="negrito", fontSize=9, leading=16, alignment=0, spaceAfter=12
        )
    )
    styles.add(ParagraphStyle(name="rodape", fontSize=9, alignment=1, leading=18))
    styles.add(
        ParagraphStyle(
            name="subtitulo",
            fontSize=10,
            alignment=1,
            textColor="#303474",
            fontName="Helvetica-Bold",
            spaceAfter=12,
        )
    )
    # styles.add(
    #     ParagraphStyle(
    #         name="subtitulo",
    #         fontSize=12,
    #         leading=16,
    #         alignment=1,
    #         textColor=colors.black,
    #         spaceAfter=12,
    #     )
    # )
    try:
        logo = Image("LOGO-DOURADOS-POSITIVO.png", width=7.5 * cm, height=2.25 * cm)
    except Exception as e:
        print(f"⚠️ Erro ao carregar logo PNG: {e}")
        logo = Paragraph("PREFEITURA MUNICIPAL DE DOURADOS", styles["titulo"])

    # Textos da direita
    texto_direita = [
        Paragraph("SECRETARIA MUNICIPAL DE FAZENDA", styles["titulo"]),
        Paragraph("SUPERINTENDÊNCIA DE ADMINISTRAÇÃO TRIBUTÁRIA", styles["subtitulo"]),
    ]

    # Tabela com logo à esquerda e textos à direita
    cabecalho = Table(
        [[logo, texto_direita]], colWidths=[7.5 * cm, 11 * cm], hAlign="LEFT"
    )

    # Estilo da tabela (borda entre as colunas, espaçamento)
    cabecalho.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                (
                    "LINEBEFORE",
                    (1, 0),
                    (1, 0),
                    1,
                    colors.HexColor("#ffffff"),
                ),  # linha divisória amarela
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    styles.add(
        ParagraphStyle(
            name="centralizado",
            fontSize=10,
            leading=14,
            alignment=1,  # 0=left, 1=center, 2=right, 4=justify
            spaceBefore=6,
            spaceAfter=12,
        )
    )
    elementos.append(cabecalho)
    elementos.append(Spacer(1, 10))

    elementos.append(Paragraph(f"NOTIFICAÇÃO DE DÉBITOS Nº {dados.get('Enumerador', '')}/2025", styles["subtitulo"]))
    elementos.append(Spacer(1, 5))

    # Dados contribuinte
    nome = dados.get("Nome do econômico") or dados.get("Nome fantasia", "")
    cpf = mascarar_cpf_cnpj(dados.get("CPF/CNPJ", ""))
    endereco = dados.get("Endereço completo", "")
    inscricao = dados.get("Código do mobiliário", "")
    elementos.append(Paragraph(f"<b>Nome/Razão Social:</b> {nome}", styles["normal"]))
    elementos.append(Paragraph(f"<b>Inscrição Municipal:</b> {inscricao}", styles["normal"]))
    elementos.append(Paragraph(f"<b>CPF/CNPJ:</b> {cpf}", styles["normal"]))
    elementos.append(Paragraph(f"<b>Endereço:</b> {endereco}", styles["normal"]))
    elementos.append(Spacer(1, 10))

    # Texto introdutório
    elementos.append(
        Paragraph(
            "<b>Assunto:</b> Notificação de Débitos Tributários - Taxa de Fiscalização de Localização, Instalação e Funcionamento",
            styles["negrito"],
        )
    )
    elementos.append(Paragraph(f"Senhor(a) Contribuinte {nome},", styles["normal"]))
    elementos.append(
        Paragraph(
            "Em atenção aos registros constantes no Sistema Tributário Municipal, notificamos Vossa Senhoria "
            "acerca da existência de débitos pendentes junto à Fazenda Pública Municipal de Dourados/MS, "
            "referentes aos tributos abaixo discriminados:",
            styles["normal"],
        )
    )
    elementos.append(Spacer(1, 10))

    # Tabela de débitos
    if debitos:
        cabecalho = [campo[0] for campo in DEBITO_CAMPOS]
        linhas = [cabecalho] + [[d[c] for c in cabecalho] for d in debitos]
        tabela = Table(linhas, colWidths=[40, 180, 40, 70, 70, 70])
        tabela.setStyle(
            TableStyle(
                [
                    ("FONTSIZE", (0, 0), (-1, -1), 8),
                    ("LEADING", (0, 0), (-1, -1), 8),
                    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
                    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ]
            )
        )
        valorTotal = dados.get("Valor total")
        valorCorrigido = dados.get("Valor total corrigido")
        data = dados.get("Data de geração")
        elementos.append(tabela)
        elementos.append(Spacer(1, 6))
        elementos.append(
            Paragraph(
                f"Os débitos acima relacionados possuem valor original total de <b>R$ {valorTotal}</b>, "
                f"e encontram-se <b>atualizados até a data de {data}</b>, "
                f"resultando em um valor corrigido total de <b>R$ {valorCorrigido}</b>.",
                styles["normal"],
            )
        )
        elementos.append(Spacer(1, 5))
    else:
        elementos.append(Paragraph("Nenhum débito encontrado.", styles["Normal"]))

    # elementos.append(Spacer(1, 10))

    texto_final = """
    Os referidos débitos encontram-se em aberto, sujeitos à atualização monetária, juros e multa, conforme legislação tributária vigente.
    Solicitamos que a regularização seja efetuada, sob pena de inscrição em Dívida Ativa e posterior Solicitamos que a regularização seja efetuada, sob pena de inscrição em Dívida Ativa e Protesto e Execução Fiscal.<br/>
    A guia de recolhimento poderá ser emitida junto aos setores de atendimento da Prefeitura: na Central de Atendimento ao Cidadão, localizada na Avenida Presidente Vargas, nº 309, Jardim América, Dourados/MS, ou, se preferir, por meio do WhatsApp da Unidade de Cobrança, nos números (67) 2222-1921 e (67) 98163-0490, ou por e-mail cobrancasemfaz@dourados.ms.gov.br.<br/><br/>
    Em caso de quitação anterior, desconsiderar esta notificação.
    """
    elementos.append(Paragraph(texto_final, styles["normal"]))
    elementos.append(Spacer(1, 10))
    elementos.append(Paragraph("Atenciosamente,", styles["normal"]))
    elementos.append(Spacer(1, 10))
    
    try:
        assinatura = Image("Digitalizado_20251105-0933.png", width=5 * cm, height=1 * cm)
        assinatura.hAlign = "CENTER"
        elementos.append(assinatura)
    except Exception as e:
        print(f"⚠️ Erro ao carregar assinatura PNG: {e}")
        elementos.append(Paragraph("[Assinatura não disponível]", styles["rodape"]))
    
    elementos.append(
        Paragraph("<b>Prefeitura Municipal de Dourados</b>", styles["rodape"])
    )
    elementos.append(
        Paragraph("<b>Secretaria Municipal de Fazenda</b>", styles["rodape"])
    )
    elementos.append(
        Paragraph("<b>Superintendência de Administração Tributária</b>", styles["rodape"])
    )

    doc.build(elementos)
    buffer.seek(0)
    return buffer


# ====== COMBINAR ======
def combinar_pdf(arte_stream, corpo_stream, caminho_saida):
    arte_stream.seek(0)
    corpo_stream.seek(0)
    reader_arte = PdfReader(arte_stream)
    reader_corpo = PdfReader(corpo_stream)
    writer = PdfWriter()

    writer.add_page(reader_arte.pages[0])
    for page in reader_corpo.pages:
        writer.add_page(page)

    with open(caminho_saida, "wb") as f:
        writer.write(f)


# ====== PROGRAMA PRINCIPAL ======
with open(ARQUIVO_TXT, "r", encoding="iso-8859-1") as f:
    linhas = f.readlines()

for idx, linha in enumerate(linhas):
    print(f"\n📄 Gerando notificação {idx+1}/{len(linhas)}...")
    dados, debitos = extrair_dados(linha)
    codigo = dados.get("Código do mobiliário", "")
    nome = dados.get("Nome do econômico") or dados.get("Nome fantasia", "")
    tipoLogradouro = dados.get("Tipo logradouro", "")
    logradouro = dados.get("Logradouro", "")
    numero = dados.get("Número", "")
    bairro = dados.get("Bairro", "")
    cidade = dados.get("Cidade", "")
    complemento = dados.get("Complemento", "")
    uf = dados.get("UF", "")
    cep = dados.get("CEP", "")
    cep = mascarar_cep(cep)
    codContrib = f"Código: {codigo}"
    contribuinte = f"{nome}"
    nomeFantasia = dados.get("Nome fantasia", "")
    endereco_texto = f"{tipoLogradouro}. {logradouro}, {numero}, {complemento}"
    endereco_texto2 = f"{bairro} - {cep} - {cidade}/{uf}"

    print("🖼️  Criando página de arte com endereço...")
    arte_stream = gerar_arte_com_endereco(
        codContrib, contribuinte, nomeFantasia, endereco_texto, endereco_texto2
    )

    print("🧾  Gerando corpo da notificação...")
    corpo_stream = gerar_pdf_corpo(dados, debitos)

    caminho_pdf_final = os.path.join(PASTA_SAIDA, f"notificacao_{idx+1}.pdf")

    print("🪶  Combinando arte e corpo...")
    combinar_pdf(arte_stream, corpo_stream, caminho_pdf_final)

    print(f"✅ PDF salvo em: {os.path.abspath(caminho_pdf_final)}")

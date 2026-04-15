import pdfplumber
import json

arquivos_pdf = {
    "01": "NF 1 - ANA CAROLINA LOPES OLIVEIRA FIGUEIREDO.pdf",
    "02": "NF 1 - BANACH E FRANCA - CELINALDO ALVES DOS SANTOS - R$ 100,00 - 06.03.2026.pdf",
    "03": "NF 3 - DANIEL GONCALVES RANGEL - DRIELLE MILAGRE DOS SANTOS - R$ 150,00 - 24.02.2026.pdf",
    "04": "NF 5 - F E K COMERCIO E SERVICOS VETERINARIOS.pdf"
}


def extrair_por_geometria(caminho_pdf):
    with pdfplumber.open(caminho_pdf) as pdf:
        pagina = pdf.pages[0]
        
        # O pdfplumber "enxerga" as linhas que formam a tabela
        tabela = pagina.extract_table({
            "vertical_strategy": "lines",
            "horizontal_strategy": "lines",
        })
        
        # Se ele encontrar a estrutura de grade, os dados vêm organizados
        # sem você precisar "caçar" palavras soltas no texto.
        return json.dumps(tabela, indent=4, ensure_ascii=False)
    
def extrair_por_regex(caminho_pdf):
    
    #fazer logica de extrair usando regex

    return    

def extrair(caminho_pdf):
    
    """
    caso extrair_por_geometria() retorne um null, extrair_por_regex()
    """
    
    return


"""
TODO: def extrair_por_regex(caminho_pdf) -> a ser executada quando extrair_por_geometria nos retornar um null
normalizar o output do json para coincidirem, nao importando por qual funcao ela passou
"""

for i in arquivos_pdf:
    arquivo = arquivos_pdf[i]

    with open(arquivo+".json", "w", encoding="utf-8") as f:
        f.write(extrair_por_geometria(arquivo))
        print("extracted '"+arquivo+"' to json")
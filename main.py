import pdfplumber
import json

NOTA = "NF 1 - BANACH E FRANCA - CELINALDO ALVES DOS SANTOS - R$ 100,00 - 06.03.2026.pdf"

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

"""
TODO: def extrair_por_regex(caminho_pdf) -> a ser executada quando extrair_por_geometria nos retornar um null
normalizar o output do json para coincidirem, nao importando por qual funcao ela passou
"""

# Teste com a nota de Itajuípe, que é bem quadriculada
print(extrair_por_geometria(NOTA))

# Se quiser salvar o resultado em um arquivo .json com o mesmo nome da nota:
with open("resultado_nota.json", "w", encoding="utf-8") as f:
    f.write(extrair_por_geometria(NOTA))
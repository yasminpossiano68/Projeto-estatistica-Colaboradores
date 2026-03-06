dados_sujos = [10 , " erro ", 20 , 30 , 40 , None , 50 , 15 , " falha ", 25]

def limpar_dados(lista):
    dados_limpos = []
    for item in lista:
        if isinstance(item, (int, float)):
            dados_limpos.append(item)
    return dados_limpos


def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)

    if n % 2 == 0:
        meio1 = lista_ordenada[n//2 - 1]
        meio2 = lista_ordenada[n//2]
        return (meio1 + meio2) / 2
    else:
        return lista_ordenada[n//2]


dados = limpar_dados(dados_sujos)

print(f"Dados processados: {dados}")
print(f"Mediana: {calcular_mediana(dados)}")

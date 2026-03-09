# Projeto Colaborativo - Ciencia de Dados
dados_sujos = [10, " erro ", 20, 30, 40, None, 50, 15, " falha ", 25]

def limpar_dados():
    # Retorne uma lista apenas com int ou float
    pass

def calcular_media():
    pass

# igor mediana vini
def calcular_mediana(dados):
    dados_ordenados = sorted(dados)
    n = len(dados_ordenados)

    if n % 2 == 0:
        meio1 = dados_ordenados[n//2 - 1]
        meio2 = dados_ordenados[n//2]
        return (meio1 + meio2) / 2
    else:
        return dados_ordenados[n//2]

mediana = calcular_mediana(dados)
print(f"Dados processados: {dados}")
print(f"Mediana dos dados: {mediana}")

def calcular_variancia():
    pass

def obter_extremos():
    pass

dados = limpar_dados(dados_sujos)   
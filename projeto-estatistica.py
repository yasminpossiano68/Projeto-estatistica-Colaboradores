# Projeto Colaborativo - Ciencia de Dados
dados_sujos = [10 , " erro ", 20 , 30 , 40 , None , 50 , 15 , " falha ", 25]

def limpar_dados():
    # Retorne uma lista apenas com int ou float
    pass

def calcular_media():
    pass

def calcular_mediana():
    pass

def calcular_variancia():
    pass

def obter_extremos(dados):
    menor = min(dados)
    maior = max(dados)
    return menor, maior

dados = limpar_dados(dados_sujos)

menor, maior = obter_extremos(dados)

print(f" Dados processados : {dados}")
print(f"Menor valor é: {menor}")
print(f"Maior valor é: {maior}")
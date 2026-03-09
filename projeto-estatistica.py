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
    media = float = sum(dados) / len(dados)
    soma_quadrados = sum((x - media) ** 2 for x in dados)
    variancia = soma_quadrados / len(dados)
    return variancia       
    pass

def obter_extremos(dados):
    menor = min(dados)
    maior = max(dados)
    return menor, maior

dados = limpar_dados(dados_sujos)
variancia = calcular_variancia(dados)

print(f" Dados processados : {dados}")
print(f"Variancia dos dados processados: {variancia} ")

menor, maior = obter_extremos(dados)

print(f"Menor valor é: {menor}")
print(f"Maior valor é: {maior}")

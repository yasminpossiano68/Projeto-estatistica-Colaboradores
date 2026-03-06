# Projeto Colaborativo - Ciencia de Dados
dados_sujos = [10 , " erro ", 20 , 30 , 40 , None , 50 , 15 , " falha ", 25]

def limpar_dados():
    # Retorne uma lista apenas com int ou float
    pass

def calcular_media():
 
    soma = 0
    quantidade = 0

    for valor in dados:
        soma += valor
        quantidade += 1

    media = soma / quantidade
    return media

dados = limpar_dados(dados_sujos)

media = calcular_media(dados)

print(f"Dados processados: {dados}")
print(f"Média dos dados: {media}")

def calcular_mediana():
    pass

def calcular_variancia():
    pass

def obter_extremos():
    pass

dados = limpar_dados(dados_sujos)

print(f" Dados processados : {dados}")
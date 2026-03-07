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

def calcular_mediana(dados):
    dados_ordenados = sorted(dados)
    n = len(dados_ordenados)

    if n % 2 == 0:
        meio1 = dados_ordenados[n//2 - 1]
        meio2 = dados_ordenados[n//2]
        return (meio1 + meio2) / 2
    else:
        return dados_ordenados[n//2]

# Calculo de Variancia Gustavo e Pedro (os 00 da parada)
def calcular_variancia():
    media = sum(dados) / len(dados)
    soma_quadrados = sum((x - media) ** 2 for x in dados)
    variancia = soma_quadrados / len(dados)
    return variancia       
pass

def obter_extremos(dados):
    menor = min(dados)
    maior = max(dados)
    return menor, maior

dados = limpar_dados(dados_sujos)
mediana = calcular_mediana(dados)
print(f" Dados processados : {dados}")

print(f"Mediana dos dados: {mediana}")

# Projeto Colaborativo - Ciencia de Dados
dados_sujos = [10, " erro ", 20, 30, 40, None, 50, 15, " falha ", 25]

def limpar_dados(dados):
    dados_limpos = []
    
    for item in dados:
        if isinstance(item, (int, float)):
            dados_limpos.append(item)
    
    return dados_limpos

def calcular_media(dados):
    soma = sum(dados)
    quantidade = len(dados)
    media = soma / quantidade
    return media

# igor mediana 
def calcular_mediana(dados):
    dados_ordenados = sorted(dados)
    n = len(dados_ordenados)

    if n % 2 == 0:
        meio1 = dados_ordenados[n//2 - 1]
        meio2 = dados_ordenados[n//2]
        return (meio1 + meio2) / 2
    else:
        return dados_ordenados[n//2]

def calcular_variancia(dados):
    media = sum(dados) / len(dados)
    soma_quadrados = sum((x - media) ** 2 for x in dados)
    variancia = soma_quadrados / len(dados)
    return variancia

def obter_extremos(dados):
    menor = min(dados)
    maior = max(dados)
    return menor, maior


dados = limpar_dados(dados_sujos)

media = calcular_media(dados)
variancia = calcular_variancia(dados)
mediana = calcular_mediana(dados)

print(f"Dados processados: {dados}")
print(f"Média dos dados: {media}")
print(f"Mediana dos dados: {mediana}")
print(f"Variancia dos dados processados: {variancia}")

menor, maior = obter_extremos(dados)

print(f"Menor valor é: {menor}")
print(f"Maior valor é: {maior}")
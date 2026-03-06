# Projeto Colaborativo - Ciencia de Dados

dados_sujos = [10 , " erro ", 20 , 30 , 40 , None , 50 , 15 , " falha ", 25]

# Função para limpar os dados
def limpar_dados(lista):
    dados_limpos = []

    for item in lista:
        if type(item) == int or type(item) == float:
            dados_limpos.append(item)

    return dados_limpos


# Função para calcular a média
def calcular_media(lista):
    soma = 0
    for num in lista:
        soma = soma + num

    media = soma / len(lista)
    return media


# Função para calcular a mediana
def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    tamanho = len(lista_ordenada)
    meio = tamanho // 2

    if tamanho % 2 == 0:
        mediana = (lista_ordenada[meio - 1] + lista_ordenada[meio]) / 2
    else:
        mediana = lista_ordenada[meio]

    return mediana


# Função para calcular a variância
def calcular_variancia(lista):
    media = calcular_media(lista)
    soma = 0

    for num in lista:
        soma = soma + (num - media) ** 2

    variancia = soma / len(lista)
    return variancia


# Função para obter mínimo e máximo
def obter_extremos(lista):
    menor = min(lista)
    maior = max(lista)

    return menor, maior


# Execução do programa
dados = limpar_dados(dados_sujos)

print(f"Dados processados: {dados}")
print(f"Média: {calcular_media(dados)}")
print(f"Mediana: {calcular_mediana(dados)}")
print(f"Variância: {calcular_variancia(dados)}")

menor, maior = obter_extremos(dados)
print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
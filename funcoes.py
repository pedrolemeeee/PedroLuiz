import random

def rolar_dados(quantidade):
    resultados = []
    for _ in range(quantidade):
        resultado = random.randint(1, 6)
        resultados.append(resultado)
    return resultados

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dado = dados_rolados[dado_para_guardar]
    dados_no_estoque.append(dado)
    dados_rolados.pop(dado_para_guardar)
    return [dados_rolados, dados_no_estoque]

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    dados_rolados.append(dados_no_estoque[dado_para_remover])
    dados_no_estoque = [dado for i, dado in enumerate(dados_no_estoque) if i != dado_para_remover]
    return [dados_rolados, dados_no_estoque]

def calcula_pontos_regra_simples(dados):
    pontos = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for numero in dados:
        if numero in pontos:
            pontos[numero] = pontos[numero] + numero
    return pontos

def calcula_pontos_soma(dados):
    total = 0
    for numero in dados:
        total = total + numero
    return total

def calcula_pontos_sequencia_baixa(dados):
    dados_unicos = []
    for numero in dados:
        if numero not in dados_unicos:
            dados_unicos.append(numero)
    dados_ordenados = sorted(dados_unicos)

    contador = 1
    for i in range(1, len(dados_ordenados)):
        if dados_ordenados[i] == dados_ordenados[i - 1] + 1:
            contador = contador + 1
            if contador >= 4:
                return 15
        else:
            contador = 1
    return 0

def calcula_pontos_sequencia_alta(dados):
    dados_unicos = []
    for numero in dados:
        if numero not in dados_unicos:
            dados_unicos.append(numero)

    for i in range(len(dados_unicos)):
        for j in range(i + 1, len(dados_unicos)):
            if dados_unicos[j] < dados_unicos[i]:
                temp = dados_unicos[i]
                dados_unicos[i] = dados_unicos[j]
                dados_unicos[j] = temp

    contador = 1
    for i in range(1, len(dados_unicos)):
        if dados_unicos[i] == dados_unicos[i - 1] + 1:
            contador = contador + 1
            if contador >= 5:
                return 30
        else:
            contador = 1
    return 0

def calcula_pontos_full_house(dados):
    numeros_usados = []
    contagem_2 = False
    contagem_3 = False

    for numero in dados:
        if numero not in numeros_usados:
            quantidade = dados.count(numero)
            if quantidade == 2:
                contagem_2 = True
            elif quantidade == 3:
                contagem_3 = True
            numeros_usados.append(numero)

    if contagem_2 and contagem_3:
        total = 0
        for numero in dados:
            total = total + numero
        return total
    return 0

def calcula_pontos_quadra(dados):
    frequencias = {}
    total = 0
    for valor in dados:
        total += valor
        if valor in frequencias:
            frequencias[valor] += 1
        else:
            frequencias[valor] = 1
    for valor in frequencias:
        if frequencias[valor] >= 4:
            return total
    return 0

def calcula_pontos_quina(dados):
    frequencias = {}
    for valor in dados:
        if valor in frequencias:
            frequencias[valor] += 1
        else:
            frequencias[valor] = 1
    for valor in frequencias:
        if frequencias[valor] >= 5:
            return 50
    return 0

def calcula_pontos_regra_avancada(dados):
    return {
        'cinco_iguais': calcula_pontos_quina(dados),
        'full_house': calcula_pontos_full_house(dados),
        'quadra': calcula_pontos_quadra(dados),
        'sem_combinacao': calcula_pontos_soma(dados),
        'sequencia_alta': calcula_pontos_sequencia_alta(dados),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(dados)
    }

def faz_jogada(dados, categoria, cartela_de_pontos):
    if categoria in cartela_de_pontos['regra_avancada']:
        pontos = calcula_pontos_regra_avancada(dados)
        cartela_de_pontos['regra_avancada'][categoria] = pontos[categoria]
    else:
        pontos = calcula_pontos_regra_simples(dados)
        cartela_de_pontos['regra_simples'][categoria] = pontos[categoria]
    return cartela_de_pontos
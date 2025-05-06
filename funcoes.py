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
    if dados.count(dados[0]) == 3 or dados.count(dados[0]) == 2:
        return sum(dados)
    return 0
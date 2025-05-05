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
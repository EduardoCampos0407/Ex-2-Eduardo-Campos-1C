import random

def rolar_dados(n):
    dados_rolados = []
    for i in range(n):
        dado = random.randint(1, 6)
        dados_rolados.append(dado)
    return dados_rolados


def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dado = dados_rolados[dado_para_guardar]
    dados_no_estoque.append(dado)
    dados_rolados.pop(dado_para_guardar)
    return [dados_rolados, dados_no_estoque]

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    dado = dados_no_estoque.pop(dado_para_remover)
    dados_rolados.append(dado)
    return [dados_rolados, dados_no_estoque]

def calcula_pontos_regra_simples(dados):  
    resultado = {}
    for face in range(1, 7):
        soma = 0
        for dado in dados:
            if dado == face:
                soma += dado 
        resultado[face] = soma
    return resultado

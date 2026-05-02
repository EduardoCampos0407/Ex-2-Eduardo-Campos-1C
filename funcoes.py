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

def calcula_pontos_soma(dados):
    soma = 0
    for dado in dados:
        soma += dado
    return soma

def calcula_pontos_sequencia_baixa(dados):
    if 1 in dados and 2 in dados and 3 in dados and 4 in dados:
        return 15
    
    if 2 in dados and 3 in dados and 4 in dados and 5 in dados:
        return 15
    
    if 3 in dados and 4 in dados and 5 in dados and 6 in dados:
        return 15
    
    return 0

def calcula_pontos_sequencia_alta(dados):
    if 1 in dados and 2 in dados and 3 in dados and 4 in dados and 5 in dados:
        return 30
    
    if 2 in dados and 3 in dados and 4 in dados and 5 in dados and 6 in dados:
        return 30
   
    return 0

def calcula_pontos_full_house(dados):
    v_unicos = []
    for d in dados:
        if d not in v_unicos:
            v_unicos.append(d)
    if len(v_unicos) != 2:
        return 0
    cont1 = dados.count(v_unicos[0])
    cont2 = dados.count(v_unicos[1])
    if (cont1 == 3 and cont2 == 2) or (cont1 == 2 and cont2 == 3):    
        soma = 0
        for d in dados:
            soma += d
        return soma
    return 0 

def calcula_pontos_quadra(dados):
    for v in dados:
        cont = 0
        for d in dados:
            if d == v:
                cont += 1
        if cont >= 4:
            soma = 0
            for d in dados:
                soma += d
            return soma
    return 0

def calcula_pontos_quina(dados):
    for valor in dados:
        cont = 0
        for d in dados:
            if d == valor:
                cont += 1
        if cont >= 5:
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
    pontos_simples = calcula_pontos_regra_simples(dados)
    pontos_avancada = calcula_pontos_regra_avancada(dados)
    if categoria in ['1', '2', '3', '4', '5', '6']:
        categoria = int(categoria)
    if categoria in pontos_simples:
        cartela_de_pontos['regra_simples'][categoria] = pontos_simples[categoria]
    else:
        cartela_de_pontos['regra_avancada'][categoria] = pontos_avancada[categoria]
    return cartela_de_pontos

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)

import random

def rolar_dados(n):
    dados_r = []
    
    for i in range(n):
        dado = random.randint(1, 6)
        dados_r.append(dado)
    
    return dados_r



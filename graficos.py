import matplotlib.pyplot as plt
import numpy as np

# Dados das execuções
dados = {
    "Backtracking": [
        {"Tempo": 0.0002, "Fator de Ramificação": 2.93, "Nós Visitados": 15, "Nós Expandidos": 14, "Profundidade": 14, "Custo": 0},
        {"Tempo": 0.0003, "Fator de Ramificação": 4.36, "Nós Visitados": 37, "Nós Expandidos": 36, "Profundidade": 36, "Custo": 0},
        {"Tempo": 0.0017, "Fator de Ramificação": 5.66, "Nós Visitados": 148, "Nós Expandidos": 147, "Profundidade": 147, "Custo": 0}
    ],
    "Busca em Largura": [
        {"Tempo": 0.0002, "Fator de Ramificação": 2.69, "Nós Visitados": 35, "Nós Expandidos": 13, "Profundidade": 3, "Custo": 0},
        {"Tempo": 0.0003, "Fator de Ramificação": 4.16, "Nós Visitados": 241, "Nós Expandidos": 58, "Profundidade": 4, "Custo": 0},
        {"Tempo": 0.0020, "Fator de Ramificação": 5.74, "Nós Visitados": 2340, "Nós Expandidos": 408, "Profundidade": 6, "Custo": 0}
    ],
    "Busca em Profundidade": [
        {"Tempo": 0.0001, "Fator de Ramificação": 1.47, "Nós Visitados": 22, "Nós Expandidos": 15, "Profundidade": 14, "Custo": 0},
        {"Tempo": 0.0002, "Fator de Ramificação": 1.78, "Nós Visitados": 66, "Nós Expandidos": 37, "Profundidade": 36, "Custo": 0},
        {"Tempo": 0.0011, "Fator de Ramificação": 2.09, "Nós Visitados": 309, "Nós Expandidos": 148, "Profundidade": 147, "Custo": 0}
    ],
    "Busca Ordenada": [
        {"Tempo": 0.0001, "Fator de Ramificação": 0.78, "Nós Visitados": 14, "Nós Expandidos": 18, "Profundidade": 3, "Custo": 5},
        {"Tempo": 0.0006, "Fator de Ramificação": 0.59, "Nós Visitados": 92, "Nós Expandidos": 156, "Profundidade": 5, "Custo": 9},
        {"Tempo": 0.0108, "Fator de Ramificação": 0.36, "Nós Visitados": 609, "Nós Expandidos": 1673, "Profundidade": 7, "Custo": 17}
    ],
    "Busca Gulosa": [
        {"Tempo": 0.0003, "Fator de Ramificação": 2.72, "Nós Visitados": 68, "Nós Expandidos": 25, "Profundidade": 13, "Custo": 19},
        {"Tempo": 0.0008, "Fator de Ramificação": 4.22, "Nós Visitados": 494, "Nós Expandidos": 117, "Profundidade": 12, "Custo": 23},
        {"Tempo": 0.0042, "Fator de Ramificação": 5.70, "Nós Visitados": 2971, "Nós Expandidos": 521, "Profundidade": 18, "Custo": 43}
    ],
    "Busca A*": [
        {"Tempo": 0.0002, "Fator de Ramificação": 1.50, "Nós Visitados": 21, "Nós Expandidos": 14, "Profundidade": 3, "Custo": 5},
        {"Tempo": 0.0003, "Fator de Ramificação": 3.20, "Nós Visitados": 80, "Nós Expandidos": 25, "Profundidade": 4, "Custo": 9},
        {"Tempo": 0.0017, "Fator de Ramificação": 2.76, "Nós Visitados": 439, "Nós Expandidos": 159, "Profundidade": 6, "Custo": 17}
    ],
    "Busca IDA*": [
        {"Tempo": 0.0005, "Fator de Ramificação": 1.01, "Nós Visitados": 115, "Nós Expandidos": 114, "Profundidade": 3, "Custo": 5},
        {"Tempo": 0.0124, "Fator de Ramificação": 1.00, "Nós Visitados": 3794, "Nós Expandidos": 3793, "Profundidade": 4, "Custo": 9},
        {"Tempo": 12.5832, "Fator de Ramificação": 1.00, "Nós Visitados": 3444094, "Nós Expandidos": 3444093, "Profundidade": 6, "Custo": 17}
    ]
}

# Função para calcular a média
def calcular_media(dados):
    medias = {}
    for algoritmo, execucoes in dados.items():
        medias[algoritmo] = {chave: np.mean([execucao[chave] for execucao in execucoes]) for chave in execucoes[0].keys()}
    return medias

# Calcular médias
medias = calcular_media(dados)

# Preparar dados para os gráficos
algoritmos = list(medias.keys())
tempo = [medias[alg][ "Tempo"] for alg in algoritmos]
fator_ramificacao = [medias[alg]["Fator de Ramificação"] for alg in algoritmos]
nos_visitados = [medias[alg]["Nós Visitados"] for alg in algoritmos]
nos_expandidos = [medias[alg]["Nós Expandidos"] for alg in algoritmos]
profundidade = [medias[alg]["Profundidade"] for alg in algoritmos]
custo = [medias[alg]["Custo"] for alg in algoritmos]

# Plotar gráficos
fig, axs = plt.subplots(2, 3, figsize=(25, 20))

# Gráfico de Tempo
axs[0, 0].bar(algoritmos, tempo, color='skyblue')
axs[0, 0].set_title('Tempo de Execução (média)')
axs[0, 0].set_ylabel('Tempo (s)')
axs[0, 0].tick_params(axis='x', rotation=60)

# Gráfico de Fator de Ramificação
axs[0, 1].bar(algoritmos, fator_ramificacao, color='salmon')
axs[0, 1].set_title('Fator de Ramificação (média)')
axs[0, 1].set_ylabel('Fator de Ramificação')
axs[0, 1].tick_params(axis='x', rotation=45)

# Gráfico de Nós Visitados
axs[0, 2].bar(algoritmos, nos_visitados, color='lightgreen')
axs[0, 2].set_title('Nós Visitados (média)')
axs[0, 2].set_ylabel('Número de Nós Visitados')
axs[0, 2].tick_params(axis='x', rotation=45)

# Gráfico de Nós Expandidos
axs[1, 0].bar(algoritmos, nos_expandidos, color='orange')
axs[1, 0].set_title('Nós Expandidos (média)')
axs[1, 0].set_ylabel('Número de Nós Expandidos')
axs[1, 0].tick_params(axis='x', rotation=45)

# Gráfico de Profundidade
axs[1, 1].bar(algoritmos, profundidade, color='purple')
axs[1, 1].set_title('Profundidade (média)')
axs[1, 1].set_ylabel('Profundidade')
axs[1, 1].tick_params(axis='x', rotation=45)

# Gráfico de Custo
axs[1, 2].bar(algoritmos, custo, color='teal')
axs[1, 2].set_title('Custo (média)')
axs[1, 2].set_ylabel('Custo')
axs[1, 2].tick_params(axis='x', rotation=45)

# Ajustar layout
plt.tight_layout()
plt.show()

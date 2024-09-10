import time
from puzzle import ReguaPuzzle
from algorithms.bfs import breadth_first_search
from algorithms.dfs_limited import depth_limited_search
from algorithms.greedy_search import greedy_search
from algorithms.a_star_search import a_star_search
from algorithms.backtracking_search import backtracking_search
from algorithms.uniform_cost_search import uniform_cost_search
from algorithms.ida_star_search import ida_star_search
from utils import print_statistics

def main():
    # Entrada do usuário para o estado inicial (sem o estado objetivo)
    initial_state = tuple(input("Digite o estado inicial da régua-puzzle (Ex: B A - A B): ").split())
    
    # Inicializa o puzzle com o estado inicial
    puzzle = ReguaPuzzle(initial_state)
    
    # Exibe os possíveis estados objetivo
    print(f"\nEstados objetivo possíveis: {[' '.join(state) for state in puzzle.goal_state]}")
    
    # Dicionário de algoritmos disponíveis
    algorithms = {
        "1": ("Backtracking", backtracking_search),
        "2": ("Busca em Largura (BFS)", breadth_first_search),
        "3": ("Busca em Profundidade Limitada (DFS)", depth_limited_search),
        "4": ("Busca Ordenada (Uniform Cost)", uniform_cost_search),
        "5": ("Busca Gulosa", greedy_search),
        "6": ("Busca A*", a_star_search),
        "7": ("Busca IDA*", ida_star_search)
    }
    
    while True:
        # Exibição das opções para o usuário escolher o algoritmo
        print("\nEscolha o algoritmo de busca:")
        for key, (name, _) in algorithms.items():
            print(f"{key}. {name}")
        print("0. Sair")
        
        # Entrada do usuário para selecionar o algoritmo
        choice = input("Digite o número do algoritmo escolhido: ")
        
        if choice == "0":
            print("Encerrando o programa.")
            break
        
        if choice not in algorithms:
            print("Escolha inválida. Tente novamente.")
            continue
        
        # Obter o nome e a função do algoritmo escolhido
        algorithm_name, algorithm_function = algorithms[choice]
        
        # Se for DFS, perguntar sobre o limite de profundidade
        if algorithm_name == "Busca em Profundidade Limitada (DFS)":
            limit = int(input("Digite o limite de profundidade: "))
        
        print(f"\nExecutando {algorithm_name}...\n")
        
        # Usando time.perf_counter() para medir o tempo de execução com mais precisão
        start_time = time.perf_counter()
        if algorithm_name == "Busca em Profundidade Limitada (DFS)":
            result = algorithm_function(puzzle, limit=limit)  # Passar o limite para DFS
        else:
            result = algorithm_function(puzzle)
        end_time = time.perf_counter()
        
        # Calcular o tempo de execução
        elapsed_time = end_time - start_time
        result['tempo_execucao'] = elapsed_time
        
        # Exibir as estatísticas
        print_statistics(algorithm_name, result)

if __name__ == "__main__":
    main()

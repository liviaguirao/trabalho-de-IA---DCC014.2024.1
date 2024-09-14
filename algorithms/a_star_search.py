import heapq
import time
from heuristics import heuristic_manhattan

def a_star_search(puzzle):
    # Marca o tempo de início da execução
    start_time = time.time()
    start_state = puzzle.initial_state  # Estado inicial do quebra-cabeça
    
    # Seleciona o primeiro estado objetivo da lista de estados possíveis
    goal_state = puzzle.goal_state[0]
    
    # Inicializa a fila de prioridade (heap), armazenando (f, g, estado_atual, caminho)
    heap = []
    # Empilha o estado inicial com f = h(start_state), g = 0 (custo até o estado inicial)
    heapq.heappush(heap, (heuristic_manhattan(start_state, goal_state), 0, start_state, [start_state]))
    
    # Dicionário para armazenar os menores custos de cada estado já visitado
    visited = {}
    
    # Converte o estado inicial para tupla para ser usado como chave no dicionário
    start_state = tuple(start_state)

    # Inicializa contadores para estatísticas
    nodes_expanded = 0  # Contador para nós expandidos
    nodes_visited = 0  # Contador para nós visitados (sucessores gerados)

    # Laço principal da busca
    while heap:
        # Remove o estado com menor valor de f da heap (min-heap)
        f, g, current_state, path = heapq.heappop(heap)
        nodes_expanded += 1  # Incrementa o contador de nós expandidos
        
        # Verifica se o estado atual é o objetivo
        if puzzle.is_goal(current_state):
            end_time = time.time()  # Marca o tempo de término
            # Retorna as informações relevantes ao encontrar o estado objetivo
            return {
                'caminho': path,  # Caminho até o estado objetivo
                'profundidade': len(path) - 1,  # Profundidade (número de passos)
                'custo': g,  # Custo acumulado do caminho (g)
                'nodos_expandidos': nodes_expanded,  # Total de nós expandidos
                'nodos_visitados': nodes_visited,  # Total de nós visitados
                'fator_ramificacao': nodes_visited / nodes_expanded if nodes_expanded else 0,  # Fator de ramificação médio
                'tempo_execucao': end_time - start_time  # Tempo total de execução
            }
        
        # Converte o estado atual em tupla para consistência
        current_state = tuple(current_state)
        
        # Verifica se já visitou o estado com um custo menor ou igual
        if current_state in visited and visited[current_state] <= g:
            continue  # Se o estado já foi visitado com menor custo, ignora-o
        
        # Atualiza o custo do estado atual
        visited[current_state] = g
        
        # Para cada sucessor do estado atual
        for successor, move_cost in puzzle.get_successors(current_state):
            successor = tuple(successor)  # Converte o sucessor em tupla
            nodes_visited += 1  # Incrementa o contador de sucessores gerados
            # Calcula o novo custo g (custo do caminho até o sucessor)
            new_g = g + move_cost
            # Calcula o valor de f (g + h) para o sucessor
            new_f = new_g + heuristic_manhattan(successor, goal_state)
            # Empilha o sucessor na heap com seu f, g, estado e caminho atualizado
            heapq.heappush(heap, (new_f, new_g, successor, path + [successor]))

    # Se a busca falhar em encontrar o objetivo, retorna um dicionário indicando falha
    end_time = time.time()  # Marca o tempo de término
    return {
        'caminho': None,  # Não encontrou caminho
        'profundidade': 0,
        'custo': 0,
        'nodos_expandidos': nodes_expanded,  # Nós expandidos até a falha
        'nodos_visitados': nodes_visited,  # Sucessores visitados até a falha
        'fator_ramificacao': nodes_visited / nodes_expanded if nodes_expanded else 0,  # Fator de ramificação médio
        'tempo_execucao': end_time - start_time  # Tempo total de execução
    }

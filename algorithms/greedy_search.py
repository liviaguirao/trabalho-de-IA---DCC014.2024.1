# algorithms/greedy_search.py
import heapq
from heuristics import heuristic_hamming  # Importa a heurística de Hamming

def greedy_search(puzzle):
    # Estado inicial e objetivo do quebra-cabeça
    start_state = puzzle.initial_state
    goal_state = puzzle.goal_state
    
    # Inicializa a heap (fila de prioridade), com o estado inicial e sua heurística
    # A heap é baseada apenas na heurística (h), ignorando o custo acumulado (g)
    heap = []
    heapq.heappush(heap, (heuristic_hamming(start_state, goal_state), start_state, [start_state], 0))
    
    # Conjunto de estados visitados para evitar reexploração
    visited = set([start_state])
    
    # Contadores para nós expandidos e visitados
    nodes_expanded = 0  # Número de nós expandidos
    nodes_visited = 0  # Número de sucessores gerados

    # Laço principal da busca gulosa
    while heap:
        # Remove o estado com menor valor de heurística (h) da heap
        h, current_state, path, cost = heapq.heappop(heap)
        nodes_expanded += 1  # Conta um nó expandido
        
        # Verifica se o estado atual é o estado objetivo
        if puzzle.is_goal(current_state):
            # Retorna as informações relevantes ao encontrar a solução
            return {
                'caminho': path,  # Caminho percorrido até o objetivo
                'profundidade': len(path) - 1,  # Profundidade do caminho
                'custo': cost,  # Custo acumulado do caminho
                'nodos_expandidos': nodes_expanded,  # Número de nós expandidos
                'nodos_visitados': nodes_visited,  # Número de sucessores visitados
                'fator_ramificacao': nodes_visited / nodes_expanded if nodes_expanded else 0,  # Fator de ramificação médio
                'tempo_execucao': 0  # O cálculo do tempo não está implementado
            }

        # Expande o nó atual obtendo seus sucessores
        for successor, move_cost in puzzle.get_successors(current_state):
            nodes_visited += 1  # Conta um sucessor gerado
            # Se o sucessor ainda não foi visitado, adiciona-o à heap
            if successor not in visited:
                visited.add(successor)  # Marca o sucessor como visitado
                # Empilha o sucessor com base apenas no valor da heurística h (busca gulosa ignora o custo g)
                heapq.heappush(heap, (heuristic_hamming(successor, goal_state), successor, path + [successor], cost + move_cost))


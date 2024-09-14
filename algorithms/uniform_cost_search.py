import heapq
import time

def uniform_cost_search(puzzle):
    # Define o estado inicial do quebra-cabeça
    start_state = puzzle.initial_state
    
    # Lista de estados objetivos (pode haver mais de um objetivo)
    goal_states = puzzle.goal_state
    
    # Inicializa a heap (fila de prioridade) com o estado inicial
    # A heap contém tuplas (custo, estado, caminho)
    heap = []
    heapq.heappush(heap, (0, start_state, [start_state]))  # O custo inicial é 0
    
    # Dicionário para armazenar os estados visitados e o menor custo associado a cada um
    visited = {}
    
    # Contadores para nós expandidos e visitados
    nodes_expanded = 0  # Contador de nós que foram expandidos
    nodes_visited = 0  # Contador de nós que foram gerados como sucessores

    # Marca o tempo de início da execução
    start_time = time.time()

    # Laço principal da busca de custo uniforme
    while heap:
        # Remove o estado com o menor custo da heap
        cost, current_state, path = heapq.heappop(heap)
        nodes_expanded += 1  # Incrementa o contador de nós expandidos
        
        # Verifica se o estado atual é o objetivo
        if puzzle.is_goal(current_state):
            end_time = time.time()  # Marca o tempo de fim da execução
            # Retorna o resultado se o objetivo for encontrado
            return {
                'caminho': path,  # Caminho até o estado objetivo
                'profundidade': len(path) - 1,  # Profundidade é o tamanho do caminho - 1
                'custo': cost,  # Custo total acumulado do caminho
                'nodos_expandidos': nodes_expanded,  # Número total de nós expandidos
                'nodos_visitados': nodes_visited,  # Número total de nós visitados (sucessores gerados)
                'fator_ramificacao': nodes_visited / nodes_expanded if nodes_expanded > 0 else 0,  # Fator de ramificação médio
                'tempo_execucao': end_time - start_time  # Tempo total de execução
            }
        
        # Verifica se o estado atual já foi visitado com um custo menor ou igual
        if current_state in visited and visited[current_state] <= cost:
            continue  # Ignora estados que foram visitados com um custo melhor
        
        # Atualiza o custo do estado atual no dicionário de visitados
        visited[current_state] = cost
        nodes_visited += 1  # Conta o nó como visitado (sucessor gerado)

        # Expande o estado atual, explorando seus sucessores
        for successor, move_cost in puzzle.get_successors(current_state):
            # Verifica se o sucessor ainda não foi visitado ou se um caminho mais barato foi encontrado
            if successor not in visited or visited[successor] > cost + move_cost:
                # Adiciona o sucessor na heap com seu custo atualizado
                heapq.heappush(heap, (cost + move_cost, successor, path + [successor]))

    # Se nenhum estado objetivo for encontrado, retorna os resultados indicando falha
    end_time = time.time()  # Marca o tempo de fim da execução
    return {
        'caminho': None,  # Não foi encontrada uma solução
        'profundidade': 0,
        'custo': 0,  # O custo é zero, pois não foi encontrada uma solução
        'nodos_expandidos': nodes_expanded,  # Número total de nós expandidos
        'nodos_visitados': nodes_visited,  # Número total de nós visitados
        'fator_ramificacao': nodes_visited / nodes_expanded if nodes_expanded > 0 else 0,  # Fator de ramificação médio
        'tempo_execucao': end_time - start_time  # Tempo total de execução
    }

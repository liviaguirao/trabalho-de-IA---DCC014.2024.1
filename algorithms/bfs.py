import time
from collections import deque

def breadth_first_search(puzzle):
    # Marca o início do tempo de execução
    start_time = time.time()
    
    # Estado inicial do quebra-cabeça
    start_state = puzzle.initial_state
    
    # Inicializa a fila (queue) para a busca, com o estado inicial e seu caminho correspondente
    queue = deque([(start_state, [start_state], 0)])
    
    # Inicializa o conjunto de estados visitados para evitar repetições
    visited = set([tuple(start_state)])  # Converte o estado inicial para tupla para ser hashable

    # Inicializa contadores para nós expandidos e visitados
    nodes_expanded = 0  # Contador para nós expandidos
    nodes_visited = 0  # Contador para sucessores gerados

    # Laço principal da busca em largura
    while queue:
        # Remove o primeiro estado da fila (FIFO)
        current_state, path,g = queue.popleft()
        nodes_expanded += 1  # Contabiliza o nó expandido
        
        # Verifica se o estado atual é o estado objetivo
        if puzzle.is_goal(current_state):
            # Calcula o tempo final de execução
            end_time = time.time()
            # Retorna as informações do caminho e estatísticas
            return {
                'caminho': path,  # O caminho percorrido até o objetivo
                'profundidade': len(path) - 1,  # Profundidade do caminho
                'custo': g,
                'nodos_expandidos': nodes_expanded,  # Número total de nós expandidos
                'nodos_visitados': nodes_visited,  # Número total de nós visitados (sucessores gerados)
                'fator_ramificacao': nodes_visited / nodes_expanded if nodes_expanded else 0,  # Fator de ramificação médio
                'tempo_execucao': end_time - start_time  # Tempo total de execução
            }
        
        # Expande o nó atual obtendo seus sucessores
        for successor, move_cost in puzzle.get_successors(current_state):
            successor = tuple(successor)  # Converte o sucessor para tupla para ser armazenado no conjunto visited
            nodes_visited += 1  # Contabiliza o nó visitado
            
            # Se o sucessor ainda não foi visitado, adiciona na fila para exploração futura
            if successor not in visited:
                visited.add(successor)  # Marca o sucessor como visitado
                queue.append((successor, path + [successor], g + move_cost))  # Adiciona o sucessor e o caminho atualizado na fila

    # Se a fila esvaziar e nenhum estado objetivo for encontrado, retorna o resultado de falha
    end_time = time.time()  # Marca o tempo final
    return {
        'caminho': None,  # Não encontrou solução
        'profundidade': 0,
        'custo': 0,
        'nodos_expandidos': nodes_expanded,  # Nós expandidos durante a busca
        'nodos_visitados': nodes_visited,  # Nós visitados (sucessores gerados) durante a busca
        'fator_ramificacao': nodes_visited / nodes_expanded if nodes_expanded else 0,  # Fator de ramificação médio
        'tempo_execucao': end_time - start_time  # Tempo total de execução
    }

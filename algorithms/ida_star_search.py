# algorithms/ida_star_search.py
import time
from heuristics import heuristic_hamming 

def ida_star_search(puzzle):
    # Marca o tempo de início da execução
    start_time = time.time()

    # Define o estado inicial e o estado objetivo do quebra-cabeça
    start_state = puzzle.initial_state
    goal_state = puzzle.goal_state

    # Calcula o limite inicial baseado na heurística (f = h(n)) para o estado inicial
    threshold = heuristic_hamming(start_state, goal_state)  # Usa a heurística de Hamming.

    # O caminho começa com o estado inicial
    path = [start_state]
    
    # Contadores para nós expandidos e visitados
    nodes_expanded = 0
    nodes_visited = 1

    # Função recursiva que realiza a busca com limitação de profundidade iterativa
    def search(state, g, threshold, path, visited):
        nonlocal nodes_expanded, nodes_visited  # Permite modificar as variáveis externas

        # Calcula f(n) = g(n) + h(n), onde g é o custo do caminho até aqui e h é a heurística
        f = g + heuristic_hamming(state, goal_state)
        
        # Se f(n) for maior que o threshold atual, retorna f para ajustar o limite
        if f > threshold:
            return f

        # Se o estado atual for o estado objetivo, retorna o caminho e o custo
        if puzzle.is_goal(state):
            return {'caminho': path, 'profundidade': len(path) - 1, 'custo': g}
        
        min_threshold = float('inf')  # Inicializa o próximo limite como infinito

        # Expande o nó atual, explorando seus sucessores
        for successor, move_cost in puzzle.get_successors(state):
            if successor not in visited:  # Verifica se o sucessor já foi visitado
                visited.add(successor)  # Marca o sucessor como visitado
                nodes_expanded += 1  # Conta um nó expandido
                nodes_visited += 1  # Conta um sucessor visitado

                # Chama recursivamente o `search` para explorar o sucessor
                result = search(successor, g + move_cost, threshold, path + [successor], visited)  # Custo de cada movimento é 1.
                
                # Se o resultado for uma solução (dicionário), retorna-o
                if isinstance(result, dict):
                    return result
                
                # Atualiza o próximo limite (threshold) com o menor valor de f
                if result < min_threshold:
                    min_threshold = result
                
                # Remove o sucessor do conjunto de visitados para permitir outras explorações
                visited.remove(successor)

        # Retorna o menor valor de f para atualizar o threshold
        return min_threshold

    # Laço principal para controle do limite de profundidade
    while True:
        visited = set([tuple(start_state)])  # Usar tuplas para garantir hashability.
        
        # Inicia a busca com o limite atual (threshold)
        result = search(tuple(start_state), 0, threshold, path, visited)
        
        # Se o resultado for uma solução (dicionário), retorna as estatísticas
        if isinstance(result, dict):
            end_time = time.time()
            return {
                **result, 
                'nodos_expandidos': nodes_expanded,  # Total de nós expandidos
                'nodos_visitados': nodes_visited,  # Total de nós visitados
                'fator_ramificacao': nodes_visited / nodes_expanded if nodes_expanded else 0,  # Fator de ramificação médio
                'tempo_execucao': end_time - start_time  # Tempo total de execução
            }
        
        # Se o limite for infinito, significa que não há solução
        if result == float('inf'):
            return {}

        # Atualiza o threshold para o próximo valor mínimo retornado
        threshold = result

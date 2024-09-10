def backtracking_search(puzzle):
    from collections import deque

    # Inicializa os contadores para análise do desempenho
    nodes_expanded = 0  # Contador para nós expandidos
    nodes_visited = set()  # Conjunto para rastrear estados já visitados
    total_successors = 0  # Contador para o total de sucessores gerados

    def backtrack(state, path, visited):
        nonlocal nodes_expanded, total_successors  # Permite modificar variáveis de fora da função

        # Verifica se o estado atual é o objetivo
        if puzzle.is_goal(state):
            # Calcula o fator de ramificação (número médio de sucessores por nó expandido)
            branching_factor = (total_successors / nodes_expanded) if nodes_expanded > 0 else 0
            # Retorna os resultados relevantes ao encontrar o estado objetivo
            return {
                'caminho': path,  # Caminho percorrido até o estado objetivo
                'profundidade': len(path) - 1,  # Profundidade do estado objetivo
                'nodos_expandidos': nodes_expanded,  # Total de nós expandidos
                'nodos_visitados': len(visited),  # Total de estados visitados
                'fator_ramificacao': branching_factor  # Fator de ramificação calculado
            }

        # Incrementa o número de nós expandidos a cada chamada
        nodes_expanded += 1
        # Obtém todos os sucessores do estado atual
        successors = puzzle.get_successors(state)
        # Atualiza o número total de sucessores gerados
        total_successors += len(successors)

        # Para cada sucessor, verifica se ele já foi visitado
        for successor, _ in successors:
            if successor not in visited:
                visited.add(successor)  # Marca o sucessor como visitado
                # Realiza a chamada recursiva para explorar o sucessor
                result = backtrack(successor, path + [successor], visited)
                # Se encontrar uma solução, retorna o resultado
                if result:
                    return result
                # Se não encontrar, remove o sucessor do conjunto de visitados para explorar outros caminhos
                visited.remove(successor)
        
        # Retorna None se nenhum sucessor levar ao estado objetivo
        return None

    # Estado inicial do puzzle
    start_state = puzzle.initial_state
    visited = set()  # Conjunto para armazenar estados visitados
    visited.add(start_state)  # Adiciona o estado inicial como visitado
    # Inicia o processo de backtracking a partir do estado inicial
    result = backtrack(start_state, [start_state], visited)
    
    # Se uma solução for encontrada, atualiza os dados finais
    if result:
        result['nodos_expandidos'] = nodes_expanded
        result['nodos_visitados'] = len(visited)
        # O fator de ramificação já foi calculado dentro da função `backtrack`

    # Retorna o resultado final ou um dicionário vazio se nenhuma solução foi encontrada
    return result if result else {}

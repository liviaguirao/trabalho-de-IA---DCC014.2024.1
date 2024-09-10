import time

def depth_limited_search(puzzle, limit=50):
    # Marca o tempo de início da execução
    start_time = time.time()
    
    # Inicializa os contadores para nós expandidos e visitados
    nodes_expanded = 0  # Contador para o número de nós expandidos
    nodes_visited = 0  # Contador para o número de sucessores gerados

    # Função auxiliar recursiva que realiza a busca limitada por profundidade
    def recursive_dls(state, path, depth, visited):
        nonlocal nodes_expanded, nodes_visited  # Acessa as variáveis externas
        nodes_expanded += 1  # Incrementa o número de nós expandidos

        # Verifica se o estado atual é o estado objetivo
        if puzzle.is_goal(state):
            end_time = time.time()  # Marca o tempo de fim
            # Retorna as informações relevantes se o objetivo for encontrado
            return {
                'caminho': path,  # O caminho até o estado objetivo
                'profundidade': depth,  # Profundidade do caminho
                'nodos_expandidos': nodes_expanded,  # Número total de nós expandidos
                'nodos_visitados': nodes_visited,  # Número total de nós visitados
                'fator_ramificacao': nodes_visited / nodes_expanded if nodes_expanded else 0,  # Fator de ramificação médio
                'tempo_execucao': end_time - start_time  # Tempo total de execução
            }

        # Verifica se a profundidade atingiu o limite
        if depth == limit:
            return None  # Retorna None se o limite de profundidade foi atingido
        
        # Expande o estado atual, gerando seus sucessores
        for successor, _ in puzzle.get_successors(state):
            successor = tuple(successor)  # Converte o sucessor para tupla
            nodes_visited += 1  # Contabiliza os sucessores visitados
            # Verifica se o sucessor já foi visitado
            if successor not in visited:
                visited.add(successor)  # Marca o sucessor como visitado
                # Chama recursivamente para explorar o sucessor
                result = recursive_dls(successor, path + [successor], depth + 1, visited)
                if result:  # Se encontrar o objetivo, retorna o resultado
                    return result
        return None  # Retorna None se não houver solução dentro do limite de profundidade

    # Estado inicial do quebra-cabeça
    start_state = puzzle.initial_state
    # Conjunto para armazenar estados visitados, evitando loops
    visited = set([tuple(start_state)])  # Converte o estado inicial para tupla
    # Chama a função recursiva de busca limitada por profundidade a partir do estado inicial
    result = recursive_dls(start_state, [start_state], 0, visited)

    # Calcula o tempo total de execução
    end_time = time.time()
    # Se o resultado foi encontrado, retorna-o
    if result:
        return result
    # Caso contrário, retorna informações indicando falha
    return {
        'caminho': None,  # Não encontrou solução
        'profundidade': 0,
        'nodos_expandidos': nodes_expanded,  # Nós expandidos durante a busca
        'nodos_visitados': nodes_visited,  # Nós visitados durante a busca
        'fator_ramificacao': nodes_visited / nodes_expanded if nodes_expanded else 0,  # Fator de ramificação médio
        'tempo_execucao': end_time - start_time  # Tempo total de execução
    }

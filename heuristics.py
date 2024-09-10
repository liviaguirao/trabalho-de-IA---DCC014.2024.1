# heuristics.py
def heuristic_hamming(state, goal):
    return sum(1 for s, g in zip(state, goal) if s != g)

# heuristics.py
def heuristic_manhattan(state, goal):
    # Verifique se todos os caracteres do estado inicial estão no estado objetivo
    if set(state) != set(goal):
        raise ValueError(f"Os caracteres no estado inicial {state} e no estado final {goal} não coincidem.")
    
    # Calcula a soma das distâncias das posições de cada bloco até a posição correta
    distance = 0
    for i, char in enumerate(state):
        if char != '-':  # Ignorar o espaço vazio
            goal_idx = goal.index(char)
            distance += abs(i - goal_idx)
    return distance



def heuristic_custom(state: str, goal: str) -> int:
    """
    Heurística personalizada: combinação das heurísticas de Hamming e Manhattan.
    """
    return 0.5 * heuristic_hamming(state, goal) + 0.5 * heuristic_manhattan(state, goal)
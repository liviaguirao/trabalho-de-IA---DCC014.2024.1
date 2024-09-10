class ReguaPuzzle:
    def __init__(self, initial_state):
        # O estado inicial do quebra-cabeça é armazenado como uma tupla (imutável)
        self.initial_state = tuple(initial_state)
        # Gera os possíveis estados objetivo com base nos blocos do estado inicial
        self.goal_state = self.generate_goal_state()

    def generate_goal_state(self):
        # Filtra os blocos (A e B), ignorando o espaço vazio '-'
        blocks = [x for x in self.initial_state if x != '-']
        # Conta a quantidade de blocos 'B' e 'A'
        num_b = blocks.count('B')
        num_a = blocks.count('A')
        
        # Cria a sequência de blocos objetivo com 'B' seguido por 'A'
        goal_blocks = ['B'] * num_b + ['A'] * num_a
        
        goal_states = []
        # Gera todos os possíveis estados objetivo inserindo o espaço vazio '-' em todas as posições possíveis
        for i in range(len(goal_blocks) + 1):
            # Insere o espaço vazio '-' na posição `i`
            goal_state = goal_blocks[:i] + ['-'] + goal_blocks[i:]
            goal_states.append(tuple(goal_state))  # Armazena o estado como tupla
        return goal_states  # Retorna a lista de possíveis estados objetivo

    def is_goal(self, state):
        # Verifica se o estado atual está na lista de estados objetivo gerados
        return state in self.goal_state

    def get_successors(self, state):
        # Verifica se há um espaço vazio '-' no estado
        if '-' not in state:
            return []
        
        # Encontra a posição do espaço vazio '-'
        empty_pos = state.index('-')
        successors = []
        
        # Converte o estado atual para uma lista mutável
        state_list = list(state)

        # Gera os sucessores possíveis ao trocar o espaço vazio com qualquer outro bloco
        for i in range(len(state_list)):
            if state_list[i] != '-':
                # Cria uma nova configuração trocando o espaço vazio com o bloco na posição `i`
                new_state = state_list[:]
                new_state[empty_pos], new_state[i] = new_state[i], new_state[empty_pos]
                # Adiciona o novo estado gerado como um sucessor (custo de movimento = 1)
                successors.append((tuple(new_state), 1))  # O custo de mover um bloco é 1
        return successors  # Retorna a lista de sucessores

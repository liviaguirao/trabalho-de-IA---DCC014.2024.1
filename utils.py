# utils.py
def print_statistics(algorithm_name, result):
    print(f"### {algorithm_name}")
    if not result or result['caminho'] is None:
        print("Solução não encontrada.\n")
        return
    
    # Converte as tuplas do caminho em strings para exibir corretamente
    caminho_formatado = [' '.join(state) for state in result['caminho']]
    
    print(f"Caminho: {' -> '.join(caminho_formatado)}")
    print(f"Profundidade: {result.get('profundidade', 'N/A')}")
    print(f"Custo: {result.get('custo', 'N/A')}")
    print(f"Nós Expandidos: {result.get('nodos_expandidos', 'N/A')}")
    print(f"Nós Visitados: {result.get('nodos_visitados', 'N/A')}")
    print(f"Fator de Ramificação: {result.get('fator_ramificacao', 'N/A'):.2f}")
    print(f"Tempo de Execução: {result['tempo_execucao']:.4f} segundos\n")

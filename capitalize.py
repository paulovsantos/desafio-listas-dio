def filtrar_visuais(lista_visuais):
    # Converter a string de entrada em uma lista
    visuais = lista_visuais.split(", ")
    
    # TODO: Normalize e remova duplicatas usando um conjunto
    titulo_capitalizado = [s.strip().title() for s in visuais]
    lista_final = set(titulo_capitalizado)
    lista_ordenada = sorted(lista_final)
    
    # TODO: Converta o conjunto de volta para uma lista ordenada:
    
    
    # Unir a lista em uma string, separada por vírgulas
    return ", ".join(lista_ordenada)

# Capturar a entrada do usuário
entrada_usuario = input("Digite o tipo de visuais: ")

# Processar a entrada e obter a saída
saida = filtrar_visuais(entrada_usuario)
print(saida)
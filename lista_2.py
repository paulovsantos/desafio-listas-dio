def produto_mais_vendido(produtos):
    contagem = {} #dicionário
    
    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1
    
    max_produto = None
    max_count = 0
    
    for produto, count in contagem.items():
        # TODO: Encontre o produto com a maior contagem:
            if count > max_count:
                max_count = count
                max_produto = produto
    
    return max_produto

def obter_entrada_produtos():
    # Solicita a entrada do usuário em uma única linha
    entrada = input("Digite: ")
    produtos = [valor.strip() for valor in entrada.split(',')]
   
    return produtos

produtos = obter_entrada_produtos()
print(produto_mais_vendido(produtos))
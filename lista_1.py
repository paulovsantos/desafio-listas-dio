def analise_vendas(vendas):
   
    total_vendas = sum(vendas)  # Calcula o total de vendas
    media_vendas = total_vendas / len(vendas) if vendas else 0  # Calcula a média mensal

    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
   
    entrada = input("Digite os valores de vendas separados por espaço: ")
    # Divide a entrada e converte cada valor para inteiro
    vendas = [int(valor) for valor in entrada.split(',')]
    
    return vendas

# Obtém a entrada do usuário
vendas = obter_entrada_vendas()
# Analisa as vendas e exibe o resultado
print(analise_vendas(vendas))

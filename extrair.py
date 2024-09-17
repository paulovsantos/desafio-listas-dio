def extrair_anos(datas):
    # Divide a string de datas em uma lista
    lista_datas = datas.split(", ")
   
    # TODO: Extraia o ano de cada data e cria uma nova lista com os anos
   
    anos = [lista_data[:4] for lista_data in lista_datas]
    
    # Junta os anos em uma string separada por vírgula e retorna
    return ", ".join(anos)


entrada = input("Digite as datas: ")

# TODO: Chame a função para imprimir o resultado:
saida = extrair_anos(entrada)
print(saida)
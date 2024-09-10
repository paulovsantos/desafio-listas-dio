class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Relatorio:
    def __init__(self):
        self.vendas = []

    def adicionar_venda(self, venda):
        if isinstance(venda, Venda):
            self.vendas.append(venda)
        
        
    def calcular_total_vendas(self):
        total = 0
        for venda in self.vendas:
            total += venda.quantidade * venda.valor
        return total

def main():
    relatorio = Relatorio()
    
    for _ in range(3):
        produto = input("Produto: ")
        quantidade = int(input("Quantidade: "))
        valor = float(input("Valor: "))
        venda = Venda(produto, quantidade, valor)
        relatorio.adicionar_venda(venda)
        
    total_de_vendas = relatorio.calcular_total_vendas()
    print(f"Total de vendas: {total_de_vendas:.1f}")

if __name__ == "__main__":
    main()

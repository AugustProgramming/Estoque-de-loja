class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, nome, quantidade, preco):
        if nome not in self.produtos:
            self.produto[nome] = {"quantidade": quantidade, "preco": preco}
        else:
            print("Este produto já foi adicionado a lista")

    def remover_produto(self, nome):
        try:
            self.produtos.pop(nome)
            print(f"{nome} removido!")
        except KeyError:
            print(f"O '{nome}' não está na lista")
    
    def exibir_estoque(self):
        for nome, dados in self.produtos.items():
            print(f"{nome}: {dados['quantidade']} unidades - R$ {dados['preco']}")

    def produto_mais_caro(self):
        try:
            caro = max(self.produtos, key=lambda nome: self.produtos[nome]["preco"])
            return caro
        except KeyError:
            return "Não há nenhum produto no estoque"
        
loja = Estoque()
loja.adicionar_produto("arroz", 50, 6.90)
loja.adicionar_produto("feijão", 30, 8.50)
loja.adicionar_produto("azeite", 30, 24.90)
loja.exibir_estoque()
loja.remover_produto("feijão")
loja.remover_produto("sal")
loja.exibir_estoque()
print(loja.produto_mais_caro())
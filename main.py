produtos = {}

def adicionar_produto(nome, quantidade, preco):
    if nome in produtos:
        print(f'{nome} já está registrado')
    else:
        produtos[nome] = {"quantidade": quantidade, "preco": preco}

def remover_produtos(nome):
    if nome in produtos:
        print(f"{nome} removido")
        produtos.pop(nome)
    else:
        print('Produto não encontrado!')

def exibir_estoque():
    for nome, dados in produtos.items():
        print(f"{nome}: {dados['quantidade']} unidades - R$ {dados['preco']}")

def produto_mais_caro():
    caro = max(produtos, key=lambda nome: produtos[nome]["preco"])
    return caro

mais_caro = produto_mais_caro()
print(f"Produto mais caro: {mais_caro} - R$ {produtos[mais_caro]['preco']}")
# 🏪 Estoque de Loja

Sistema de estoque simples em Python para adicionar, remover e consultar produtos, desenvolvido para praticar listas, dicionários e funções.

## 📚 Conceitos praticados

- Dicionários e dicionários aninhados
- Funções com `def` e `return`
- Condicionais (`if/else`)
- Manipulação de dicionários (`pop`, `update`, `items`)
- `lambda` e `max()` com `key`

## ⚙️ Funcionalidades

- Adicionar produto com nome, quantidade e preço
- Remover produto do estoque
- Exibir estoque completo formatado
- Consultar o produto mais caro

## ▶️ Como executar

1. Certifique-se de ter o [Python](https://www.python.org/) instalado
2. Clone o repositório:
   ```bash
   git clone https://github.com/AugustProgramming/estoque-loja.git
   ```
3. Acesse a pasta:
   ```bash
   cd estoque-loja
   ```
4. Execute o arquivo:
   ```bash
   python main.py
   ```

## 💡 Exemplo de uso

```python
adicionar_produto("arroz", 50, 6.90)
adicionar_produto("feijão", 30, 8.50)
adicionar_produto("azeite", 15, 24.90)

exibir_estoque()
# arroz: 50 unidades - R$ 6.9
# feijão: 30 unidades - R$ 8.5
# azeite: 15 unidades - R$ 24.9

mais_caro = produto_mais_caro()
print(f"Produto mais caro: {mais_caro} - R$ {produtos[mais_caro]['preco']}")
# Produto mais caro: azeite - R$ 24.9

remover_produto("feijão")
# feijão removido
```

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)

---

Desenvolvido durante estudos de Python 🐍

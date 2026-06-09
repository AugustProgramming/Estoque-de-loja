# 🏪 Estoque de Loja

Sistema de estoque em Python para adicionar, remover e consultar produtos. O projeto evoluiu de funções simples para uma estrutura orientada a objetos com tratamento de erros.

## 📈 Evolução do projeto

| Versão | Descrição |
|--------|-----------|
| v1.0 | Funções simples com dicionários e listas |
| v2.0 | Refatorado com POO (classes) e `try/except` |

## 📚 Conceitos praticados

- Dicionários e dicionários aninhados
- Funções com `def` e `return`
- Orientação a Objetos (`class`, `__init__`, `self`)
- Tratamento de erros (`try/except`, `KeyError`)
- `lambda` e `max()` com `key`

## ⚙️ Funcionalidades

- Adicionar produto com nome, quantidade e preço
- Remover produto do estoque com mensagem de erro amigável
- Exibir estoque completo formatado
- Consultar o produto mais caro
- Tratamento de erros em todas as operações

## ▶️ Como executar

1. Certifique-se de ter o [Python](https://www.python.org/) instalado
2. Clone o repositório:
   ```bash
   git clone https://github.com/AugustProgramming/Estoque-de-loja.git
   ```
3. Acesse a pasta:
   ```bash
   cd Estoque-de-loja
   ```
4. Execute o arquivo:
   ```bash
   python main.py
   ```

## 💡 Exemplo de uso

```python
loja = Estoque()
loja.adicionar_produto("arroz", 50, 6.90)
loja.adicionar_produto("feijão", 30, 8.50)
loja.adicionar_produto("azeite", 15, 24.90)

loja.exibir_estoque()
# arroz: 50 unidades - R$ 6.9
# feijão: 30 unidades - R$ 8.5
# azeite: 15 unidades - R$ 24.9

loja.remover_produto("feijão")   # feijão removido!
loja.remover_produto("sal")      # Produto 'sal' não encontrado!

print(loja.produto_mais_caro())  # azeite
```

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)

---

Desenvolvido durante estudos de Python 🐍
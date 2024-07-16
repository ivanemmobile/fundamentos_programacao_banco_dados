# Definindo o inventário com tuplas
inventario = [
    ("Maçã", 50, 0.75),
    ("Banana", 30, 0.50),
    ("Laranja", 20, 0.80),
    ("Morango", 100, 0.25)
]

# Função para exibir o inventário
def exibir_inventario(inventario):
    print("Inventário de Produtos:")
    for produto in inventario:
        nome, quantidade, preco = produto
        print(f"Produto: {nome}, Quantidade: {quantidade}, Preço: R${preco:.2f}")
    print()

# Função para adicionar um novo produto ao inventário
def adicionar_produto(inventario, nome, quantidade, preco):
    novo_produto = (nome, quantidade, preco)
    inventario.append(novo_produto)

# Função para atualizar a quantidade de um produto
def atualizar_quantidade(inventario, nome, nova_quantidade):
    for i, produto in enumerate(inventario):
        if produto[0] == nome:
            inventario[i] = (produto[0], nova_quantidade, produto[2])
            break

# Função para remover um produto do inventário
def remover_produto(inventario, nome):
    inventario[:] = [produto for produto in inventario if produto[0] != nome]

# Exibir o inventário inicial
exibir_inventario(inventario)

# Adicionar um novo produto
adicionar_produto(inventario, "Uva", 40, 1.00)
exibir_inventario(inventario)

# Atualizar a quantidade de um produto
atualizar_quantidade(inventario, "Banana", 25)
exibir_inventario(inventario)

# Remover um produto
remover_produto(inventario, "Laranja")
exibir_inventario(inventario)

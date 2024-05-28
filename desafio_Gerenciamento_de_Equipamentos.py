# Cria uma lista 'itens' para armazenar os equipamentos
itens = []

# Loop para solicitar os itens ao usuário
for i in range(3):
    # Solicita o item e armazena na variável "item"
    item = input(f"Informe o {i+1}º equipamento: ")
    # Adiciona o item à lista "itens"
    itens.append(item)

# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")

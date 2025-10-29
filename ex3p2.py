inventario = ["elmo", "chapeu", "espada", "botas"]

busca = input("Qual item você quer procurar? ")

for item in inventario:
    if item == busca:
        print(busca + " foi encontrada!")
        break
else:
    print(busca + " não está no inventário.")

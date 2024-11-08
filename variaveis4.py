alimentos = ["Maçã","Arroz","Feijão"]
categoria = ("Grãos", "Frutas","Legumes")
pessoa={"Nome":"Paula","Idade":"38","Altura":"1.65"}

print(alimentos)
print(type(alimentos))
print(len(alimentos))

# Adicionar mais um alimento
alimentos.append("Macarrão") # append-> adicionar
print(alimentos)
print(len(alimentos))

print(categoria)
print(type(categoria))
print(len(categoria))

print(pessoa)
print(type(pessoa))
print(len(pessoa))
# Adicionar um item à pessoa
# Adicionar uma nova chave com o seu respectivo valor
# está sendo adicionado a chave email com o valor email da pessoa
pessoa["email"]="paula@gmail.com"
print(pessoa)
print(len(pessoa))
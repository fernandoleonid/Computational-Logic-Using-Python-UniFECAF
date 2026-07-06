# Manipulando dicionários

cliente = {
    "nome": "Leonid", 
    "cidade": "São Roque",
    "ano_nasc": 1976,
    "ativo": False
}
print(cliente["nome"])

cliente["ano_nasc"] = 2000
print (cliente)

del cliente["cidade"]
print(cliente)

if "ano_nasc" in cliente:
    print(f"O cliente nasceu em: {cliente['ano_nasc']}")
else:
    print(f"Não existe a chave ano_nasc")

print (f"Lista de Valores:")
for valor in cliente.values():
    print(valor)

print (f"Lista de chaves:")
for chave, valor in cliente.items():
    print(chave)
# - Variaveis e tipos de dados -

# 1 - O que é uma variável?
# É um espaço reservado na memória, que serve para
# armazenar qualquer tipo de dado.

# 2 - O que é tipagem dinâmica?
# Significa que não necessário especificar, na
# declaração, o tipo de variável.

# Exemplo de nome de variável (snake case) :
nome_aluno = "Fernando"
nota_aluno = 8

# 3 - Quais os tipos de dados em Python?
# Inteiro (int), Decimal (float), Complexo (complex),
# String (str), Boolean (bool), list, tuple, sets e dictionary
# Exemplos:
ano_atual = 2023
desconto = 15.59
cidade = "Jandira"
filhos = False
cores = ["branco", "azul", "vermelho"]
frutas = ("banana", "uva")
notas = {5, 10, 30}
cliente = {
    "nome": "Maria",
    "altura": 1.95,
    "peso": 60.00
}

# 4 - O que é tipagem forte?
numero1 = 23
numero2 = 100
print (numero1 + numero2)

# 5 - Como trocar o tipo de variável?
preco_produto = 1.90
preco_produto = str(preco_produto)
preco_produto = float(preco_produto)

print (type (preco_produto))

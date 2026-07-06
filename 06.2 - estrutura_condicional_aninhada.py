nota = float(input("Digite sua nota: "))
frequencia = int(input("Digite sua frequência: "))

if nota >= 5 and frequencia >= 75:
    situacao = "aprovado"
elif nota >= 5 or frequencia >= 75:
    situacao = "na recuperação"
else:
    situacao = "reprovado"

print(f"Você está {situacao}!")
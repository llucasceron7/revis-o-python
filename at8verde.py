nota = float(input("Digite a nota do aluno (0 a 10): "))

if nota >= 9:
    conceito = "A"
elif nota >= 7:
    conceito = "B"
else:
    conceito = "C"

print(f"O conceito final do aluno é: {conceito}")

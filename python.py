import statistics

# Coleta de dados
alunos = []
notas = []
quantidade = int(input("Quantos alunos? "))

for i in range(quantidade):
    nome = input(f"Nome do aluno {i+1}: ")
    nota = float(input(f"Nota de {nome}: "))
    alunos.append(nome)
    notas.append(nota)

# Média
media = sum(notas) / len(notas)

# Alunos com nota acima da média
acima_media = [notas[i] for i in range(len(notas)) if notas[i] > media]

# Porcentagem de alunos com nota > 7
maior_que_7 = len([n for n in notas if n > 7])
porcentagem_maior_que_7 = (maior_que_7 / len(notas)) * 100

# Aprovados (nota >= 6)
aprovados = len([n for n in notas if n >= 6])

# Maior e menor nota
maior_nota = max(notas)
menor_nota = min(notas)
aluno_maior = alunos[notas.index(maior_nota)]
aluno_menor = alunos[notas.index(menor_nota)]

# Desvio padrão
desvio_padrao = statistics.stdev(notas)

# Resultados
print(f"\nMédia da turma: {media:.2f}")
print(f"Alunos com nota maior que a média: {len(acima_media)}")
print(f"Porcentagem com nota > 7: {porcentagem_maior_que_7:.1f}%")
print(f"Alunos aprovados (nota >= 6): {aprovados}")
print(f"Desvio padrão das notas: {desvio_padrao:.2f}")
print(f"Aluno com maior nota: {aluno_maior} ({maior_nota})")
print(f"Aluno com menor nota: {aluno_menor} ({menor_nota})")

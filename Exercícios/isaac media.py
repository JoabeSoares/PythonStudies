nota = []
n = 0
print('-=' * 20)
aluno = str(input('Aluno: '))
materia = str(input('Matéria: '))
print('-=' * 20)
for c in range(0, 4):
    nota.append(float(input(f'Nota {c+1}: ')))
print('-=' * 20)
print(f'O aluno {aluno} ficou com média em {materia} de: {sum(nota)/4}')
print('-=' * 20)


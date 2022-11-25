from time import sleep
situacao = dict()
resultado = []
situacao['nome'] = str(input('Qual o nome do aluno? '))
situacao['nota'] = float(input('Qual a média do aluno? '))
resultado.append(situacao.copy())
print('-=-' * 30)
print(f'Aluno: {situacao["nome"]}.')
print(f'Média de {(situacao["nome"])}: {situacao["nota"]}.')
sleep(2)
print('-=-' * 30)
if situacao["nota"] >= 7:
    print(f'O aluno {situacao["nome"]} está APROVADO!')
else:
    print(f'O aluno {situacao["nome"]} está REPROVADO!')

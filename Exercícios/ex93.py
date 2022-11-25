dados = dict()
gols = list()
dados['Jogador'] = str(input('Qual o nome do jogador? '))
dados['Partidas'] = int(input('Quantas partidas ele jogou? '))
partidas = dados['Partidas']
for partidas in range(0, partidas):
    gols.append(int(input(f'Quantos gols ele fez na {partidas+1} partida?: ')))
dados['Gols'] = sum(gols[:])
print('-=' * 25)
print(dados)
print('-=' * 25)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}.')
print('-=' * 30)
print(f'O jogador {dados["Jogador"]} jogou {len(gols)} partidas.')
for i, v in enumerate(gols):
    print(f'   ===> Na partida {i+1}, fez {v} gols.')
print(f'   ===> Foi um total de {sum(gols)} gols.')
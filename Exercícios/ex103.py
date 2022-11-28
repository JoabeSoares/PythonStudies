def ficha(nome, gols):
    nome = str(input('Nome do jogador: '))
    gols = int(input('Gols marcados: '))
    s = gols
    print('-' * 30)
    print(f'O jogador {nome} fez {gols} gol(s).')
    return s


nome = 0
gols = 0
ficha(nome, gols)
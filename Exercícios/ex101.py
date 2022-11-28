def voto(v):
    v = int(input('Ano de nascimento: '))
    v = 2022 - v
    print('-' * 30)
    print(f'Com {v} anos: ', end='')
    if v in range(18, 65):
        print('Voto obrigatório.')
    if v < 16:
        print('Voto negado.')
    if 16 <= v < 18 or v > 65:
        print('Voto Facultativo.')
    print('-' * 30)


v = 0
voto(v)

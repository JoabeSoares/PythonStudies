def leiaFloat(msg):
    while True:
        try:
            f = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: porfavor, digite um número real válido.')
            continue
        else:
            return f



def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('-=ERRO: porfavor, digite um número inteiro válido.=-')
            continue
        else:
            return n



num = leiaInt('Digite um valor inteiro: ')
flo = leiaFloat('Digite outro valor real: ')
print(f'Os valores digitados foram {num} e {flo}')
from time import sleep


def maior(* núm):
    cont = maior = 0
    print('-' * 30)
    print('Analisando os valores passados... ')
    print('-' * 30)
    for valor in núm:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'\nO maior valor encontrado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
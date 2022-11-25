num = []
pos = 0
while True:
    num.append(int(input('Digite um valor: ')))
    res = str(input('Deseja continuar? [S/N] ')).upper()
    if res not in 'Nn':
        continue
    break
print('-=' * 30)
print(f'{len(num)} números foram digitados.')
num.sort(reverse=True)
print(f'Esses números foram {num}')
if 5 in num:
    print('O valor 5 faz parte da lista. E está na posição ', end='')
    for pos in enumerate(num):
        if 5 in num:
            print(f'{pos}...')
else:
    print('O valor 5 não foi encontrado na lista.')

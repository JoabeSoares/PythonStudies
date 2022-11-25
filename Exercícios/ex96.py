def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a}m2.')


print(' Controle de Terrenos')
print('-' * 20)
l = float(input('Digite a Largura: '))
c = float(input('Digite o comprimento: '))
área(l, c)
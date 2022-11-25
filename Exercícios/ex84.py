dados = []
prin = []
maior = menor = 0
while True:
     dados.append(str(input('Digite seu nome: ')))
     dados.append(float(input('Digite seu peso: ')))
     if len(prin) == 0:
          maior = menor = dados[1]
     else:
          if dados[1] > maior:
               maior = dados[1]
          if dados [1] < menor:
               menor = dados[1]
     prin.append(dados[:])
     dados.clear()
     resp = str(input('Deseja continuar? [S/N] ')).upper()
     if resp in 'Nn':
          break

print('-=' * 30)
print(f'Você cadastrou {len(prin)} pessoas.')
print(f'O maior peso foi de {maior} kg. Peso de ', end='')
for p in prin:
     if p[1] == maior:
          print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor} kg. Peso de ', end='')
for p in prin:
     if p[1] == menor:
          print(f'[{p[0]}] ', end='')
print()
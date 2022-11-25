galera = []
dado = []
totmai = totmen = 0
for contador in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]}  é maior de idade.')
        totmai += 1
    else:
        print(f'{pessoa[0]}  é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')

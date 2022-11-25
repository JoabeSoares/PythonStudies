dados = {}
lista = []
soma = média = 0
while True:
    dados['nome'] = str(input('Digite um nome: '))
    while True:
        dados['sexo'] = str(input(f'Digite o sexo de {dados["nome"]} [M/F]: ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')
    dados['idade'] = int(input(f'Digite a idade de {dados["nome"]}: '))
    soma += dados['idade']
    lista.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo temos {len(lista)} pessoas cadastradas.')
média = soma / len(lista)
print(f'A média de idade é de {média:5.2f} anos.')
print(f'As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] >= média:
        print('', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<Encerrado>>')

from datetime import datetime
dados = {}
dados['nome'] = str(input('Qual o nome do beneficiário? '))
dados['idade'] = int(input('Em qual ano ele(a) nasceu? '))
dados['carteira'] = int(input('Carteira de Trabalho? [0 não tem] '))
dados['idade'] = datetime.now().year - dados['idade']
dados['aposentadoria'] = dados['idade'] + (dados['contrato'] + 35) - datetime.now().year

if dados['carteira'] != 0:
    dados['contrato'] = int(input('Qual ano começou a trabalhar? '))
    dados['salario'] = float(input('Qual o salário atual? '))

for k, v in dados.items():
    print(f'{k}: {v}')
    print('-=' * 30)
if dados['carteira'] != 0:
    print(f'Faltam {65 - (2022 - dados["contrato"])} anos para {dados["nome"]} se aposentar.')
    print('-=' * 30)

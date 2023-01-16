lista = []
preço = []
while True:
    print('-=' * 30)
    lista.append(str(input("Qual o nome do produto você deseja comprar? ")))
    preço.append(int(input("Qual o preço deste produto? ")))
    resp = str(input("Deseja comprar mais produtos? [S/N] ")).upper().strip()
    if resp == 'S':
        continue
    else:
        break
print(f'{lista} {preço}')
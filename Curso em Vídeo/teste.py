from time import sleep
n = int(input('''[1] Ir para Outlet
[2] Ir para Universal
[3] Ir para Disney Springs
[4] Ir para Panda Express
Esolha uma opção:'''))
while True:
    if n == 1:
        print('Outlet está fechado.')
    elif n == 2:
        print('Universal está fechada.')
    elif n == 3:
        print('Disney Springs não abre durante furacão.')
    elif n == 4:
        print('Panda Express!!! Lá é TOP!')
    else:
        print(input('Escolha novamente.'))
    break

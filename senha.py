from time import sleep

print('Dica: a senha é 123456')
senhaoriginal = '123456'

def input_senha ():
    senha = 0
    tentativas = 0
    while senha != senhaoriginal:
        senha = str(input('Digite a senha: '))
        
        if senha == senhaoriginal:
            print('ACESSO CONCEDIDO!')
        elif tentativas >= 3:
            print('TENTATIVAS MÁXIMAS ATINGIDAS')
            for tempo in range (10,-1,-1):
                print(f'Espere {tempo} segundos...')
                sleep(1)
        else:            
            print('ACESSO NEGADO')
            tentativas += 1

def mudar_senha ():
    print('=-'*15)
    novasenha = int(input('Digite a nova senha: '))
    senhaoriginal = novasenha

while True:
    sleep(1)
    ato = int(input('''O que deseja fazer:

    {1} Para digitar a senha
    {2} Para alterar a senha
    '''))

    if ato == 1:
        input_senha()
    elif ato == 2:
        mudar_senha()
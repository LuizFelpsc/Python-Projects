from random import randint
from time import sleep

print('-='*20)
print('Jogo do acerto - O PC IRÁ ESCOLHER UM NÚMERO DE 1 A 4')

while True:

    print('-='*20)
    pessoa = int(input('Digite um número de 1 a 4:'))
    chute = randint(1,4)

    print(f'O pc chutou o número \033[32m{chute}\033[m e você escolheu o número \033[32m{pessoa}\033[m')

    sleep(1)

    if pessoa == chute:
        print(f'\033[32mParabéns!\033[m')
    else:
        print('\033[31mTente novamente\033[m')    

    sleep(1.3)        
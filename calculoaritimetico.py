#Construir um algoritimo que calcule a media aritmética de vários valores inteiros positivos, lidos do teclado. O final da leitura acontecerá quando for lido o valor 0.
valortotal = 0
valores = ''
qntd= 0
print('>>>>>Calculo de media aritmética<<<<<')
while valores != 0:
    valores = float(input(f'Digite o {qntd + 1}º Valor e Depois para Confirmar Digite 0: '))
    if valores != 0:
        valortotal = valortotal + valores
        qntd = qntd + 1
        art = valortotal/qntd
    print(qntd)
print(f'O valor da media aritimética e {art}')

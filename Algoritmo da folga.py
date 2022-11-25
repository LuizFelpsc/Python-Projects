# A pessoa escolherá o que fará em seu dia de folga entre algumas opções
# conseguir escolher cada um e a quantidade do lanche

caso = int(input('''Escolha o que você irá fazer hoje:
{1} Para ficar em casa e pedir um lache 
{2} Para ir ao cinema e escolher um filme 
{3} Para ir ao Estadio ver um jogo
'''))


match caso:
    case 1:
        pizzaprecos = {'peq': 30, 'med': 45, 'grande': 60}
        hambprecos = {'peq': 10, 'med': 15, 'grande': 20}
        hotdogprecos = {'peq': 5, 'med': 10, 'grande': 14}

        lanche = int(input('''Escolha o lanche que irá pedir para hoje:
            Lanches   -   Pequeno  -  Média   -   Grande 
        [1] Pizza         R$ 30       R$ 45       R$ 60
        [2] Hambúrguer    R$ 10       R$ 15       R$ 20
        [3] Hotdog        R$ 5        R$ 10       R$ 14
        '''))

        qtd = int(input('Escolha a quantidade do item selecionado: '))
        tamanho = str(input('Qual será o tamanho do seu lanche? Digite\n"P" para pequeno\n"M" para médio\n"G" Para grande').upper().strip())
        valorlanche = 0
                          
        match lanche:
            case 1:
                if tamanho == 'P':
                    valorlanche = pizzaprecos['peq'] * qtd
                elif tamanho == 'M':
                    valorlanche = pizzaprecos['med'] * qtd
                else:
                    valorlanche = pizzaprecos['grande'] * qtd 
            case 2:
                if tamanho == 'P':
                    valorlanche = hambprecos['peq'] * qtd
                elif tamanho == 'M':
                    valorlanche = hambprecos['med'] * qtd
                else:
                    valorlanche = hambprecos['grande'] * qtd
            case 3:
                if tamanho == 'P':
                    valorlanche = hotdogprecos['peq'] * qtd
                elif tamanho == 'M':
                    valorlanche = hotdogprecos['med'] * qtd
                else:
                    valorlanche = hotdogprecos['grande'] * qtd 
        print(f'O valor a ser pago é R${valorlanche}... seu lanche está a caminho')
    case 2:
        filmes = ['Vingadores Ultimato','Rio 2','It a coisa']
        filme = int(input('''Escolha qual filme você irá escolher: 
        [1] Vingadores Ultimato 
        [2] Rio 2
        [3] It a coisa
        '''))

        print(f'O filme escolhido foi {filmes[filme - 1]}')
    case 3:
        jogos = ['Brasil x Sérvia','Japão x Alemanha','Equador x Holanda']
        jogo = int(input('''Escolha qual filme você irá assistir: 
        [1] Brasil x Sérvia
        [2] Japão x Alemanha
        [3] Equador x Holanda
        '''))

        print(f'O filme escolhido foi {jogos[jogo - 1]}')


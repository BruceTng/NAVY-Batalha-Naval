# -*- coding: UTF-8 -*-
# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
## INICIANDO ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Importando biblioteca
import random

# Definindo cores
negrito = '\033[1m'
italico = '\033[3m'
underline = '\033[2m'
reset = '\033[0m'

# Definindo as Regras
Objetivo = 'Afundar todos os navios do adversário antes que ele afunde os seus.'
Regras_Basicas1 = 'O jogador começa com 2 Quadros 10x10. Em um será colocado os navios do jogador e o outro é um quadro branco para marcar as tentativas de posições.'
Regras_Basicas2 = ('O jogador alterna em turnos com o computador, informando qual a coordenada X e Y que deseja arriscar um tiro,\n'
                   ' caso erre sua vez será passada e a posição arriscada marcada para referencia mas se acertar pode atirar novamente até errar.')
Regras_Importantes1 = 'Os navios não podem se tocar.'
Regras_Importantes2 = 'Não podem ser posicionados na diagonal.'
Regras_Importantes3 = 'Não pode passar a vez.'

# Sorteando Inimigos
inimigos1  = [(1,1),(2,3),(4,1),(4,2),(5,3)]
inimigos2  = [(1,2),(2,4),(3,1),(4,5),(5,2)]
inimigos3  = [(1,3),(2,1),(3,4),(4,3),(5,5)]
inimigos4  = [(1,4),(2,2),(3,5),(4,4),(5,1)]
inimigos5  = [(1,5),(2,5),(3,2),(4,1),(5,4)]
inimigos6  = [(1,1),(2,4),(3,3),(4,5),(5,2)]
inimigos7  = [(1,3),(2,2),(3,1),(4,4),(5,5)]
inimigos8  = [(1,5),(2,1),(3,4),(4,2),(5,3)]
inimigos9  = [(1,2),(2,5),(3,3),(4,1),(5,4)]
inimigos10 = [(1,4),(2,3),(3,5),(4,3),(5,1)]

todos_inimigos = [inimigos1,inimigos2,inimigos3,inimigos4,inimigos5,
                  inimigos6,inimigos7,inimigos8,inimigos9,inimigos10]

inimigo = random.choice(todos_inimigos)
## FIM DA INICIALIZAÇÃO ------------------------------------------------------------------------------------------------------------------------------------------------
print('Bem vindo ao NAVY - Batalha Naval \n')
# Apresentando Menu
while True:
    print('========MENU========')
    print('1.Jogar')
    print('2.Regras')
    print('3.Sair')
    opcao = int(input('Digite o número da opção desejada: '))

    # Saindo do Jogo
    if opcao == 3:
        print('Saindo...')
        break

    # Apresentando Regras
    elif opcao == 2:
        print(f'{negrito}Objetivo:{reset} '
            f'\n {Objetivo}')
        print(f'{negrito}Regras básicas:{reset} '
            f'\n {Regras_Basicas1}'
            f'\n {Regras_Basicas2}')
        print(f'{negrito}Regras Importantes:{reset} '
            f'\n {Regras_Importantes1}'
            f'\n {Regras_Importantes2}'
            f'\n {Regras_Importantes3}')
        prosseguir = (input('Pressione ENTER para retornar ao menu.'))

    # Rodando o Jogo
    elif opcao == 1:
        # -Pedindo Posições
        aliados = []
        i = 0

        while i < 5:
            posicaoX = int(input('Insira a posição X do seu barco: '))
            posicaoY = int(input('Insira a posição Y do seu barco: '))
            aliados.append((posicaoX,posicaoY))
            i += 1
        print(f'A posição dos seus barcos são \n{negrito}{aliados}')

        # Batalha
        tentativas = 0

        while tentativas < 20:
            tiroX = int(input('Digite a posição X do barco inimigo: '))
            tiroY = int(input('Digite a posição Y do barco inimigo: '))
            if (tiroX, tiroY) in inimigos1: # MUDAR DEPOIS, ESTA SELECIONANDO LISTA 1 APENAS (TESTES)
                inimigos1.remove((tiroX, tiroY))
                print('Barco inimigo afundado!')
            else:
                print('Errou!')
            tentativas += 1
            if inimigos1 == []:
                print('Você Ganhou, Parabéns!')
                break
            elif tentativas == 20:
                print('Suas tentativas acabaram!')
            # Fim do jogo
        voltar = input('Deseja voltar ao menu? (s/n): ').strip().lower()
        if voltar != 's':
            print('Saindo...')
            break







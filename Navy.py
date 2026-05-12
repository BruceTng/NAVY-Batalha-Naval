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
azul = '\033[1;34m'
vermelho = '\033[1;31m'
verde = '\033[1;32m'
reset = '\033[0m'

# Definindo as Regras
Objetivo = 'Afundar todos os navios do adversário antes que ele afunde os seus.'
Regras_Basicas1 = 'O jogador começa com 1 Quadro 5x5, onde será marcado os navios do jogador e as tentativas de posições.'
Regras_Basicas2 = ('O jogador alterna em turnos com o computador, informando qual a coordenada X e Y que deseja arriscar um tiro,\n'
                   ' caso erre sua vez será passada e a posição arriscada marcada para referencia.')
Regras_Importantes1 = 'Os navios não podem estar na mesma posição.'
Regras_Importantes2 = 'Não podem ser posicionados na diagonal.'
Regras_Importantes3 = 'Não pode passar a vez.'

#Definindo Tamanho do Mapa
mapa = [(1,1),(1,2),(1,3),(1,4),(1,5),      #linha 1
        (2,1),(2,2),(2,3),(2,4),(2,5),      #linha 2
        (3,1),(3,2),(3,3),(3,4),(3,5),      #linha 3
        (4,1),(4,2),(4,3),(4,4),(4,5),      #linha 4
        (5,1),(5,2),(5,3),(5,4),(5,5)]      #linha 5

mapa_usuario = ("(1,1),(1,2),(1,3),(1,4),(1,5)\n"
                "(2,1),(2,2),(2,3),(2,4),(2,5)\n"
                "(3,1),(3,2),(3,3),(3,4),(3,5)\n"
                "(4,1),(4,2),(4,3),(4,4),(4,5)\n"
                "(5,1),(5,2),(5,3),(5,4),(5,5)\n")

#Definindo Inimigos
inimigos = []
i = 0

while i < 5:
    inimigo = random.choice(mapa)
    inimigos.append(inimigo)
    i += 1

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
        # Pedindo Posições
        aliados = []
        i = 0

        while i < 5:
            print(mapa_usuario)
            posicaoX = int(input('Insira a posição X do seu barco: '))
            while posicaoX < 0 or posicaoX > 5:
                print('Posição invalida!')
                posicaoX = int(input('Insira a posição X do seu barco: '))
            posicaoY = int(input('Insira a posição Y do seu barco: '))
            while posicaoY < 0 or posicaoY > 5:
                print('Posição invalida!')
                posicaoY = int(input('Insira a posição Y do seu barco: '))
            else:
                aliados.append((posicaoX, posicaoY))
                i += 1
        print(f'A posição dos seus barcos são \n{negrito}{aliados}{reset}')

        # Batalha
        print(f'{negrito}Vamos batalhar!{reset}')
        tentativas = 0

        while tentativas < 20:
            tiroX = int(input('Digite a posição X do barco inimigo: '))
            while tiroX < 0 > 5:
                print('Posição X não encontrada')
                tiroX = int(input('Digite a posição X do barco inimigo: '))
            tiroY = int(input('Digite a posição Y do barco inimigo: '))
            while tiroY < 0 > 5:
                print('Posição Y não encontrada')
                tiroY = int(input('Digite a posição Y do barco inimigo: '))
            if (tiroX, tiroY) in inimigos:
                inimigos.remove((tiroX, tiroY))
                print('Barco inimigo afundado!')
            else:
                print('Errou!')
            print(mapa_usuario)
            # Vez do computador
            tiro_pc = random.choice(mapa)
            if tiro_pc in aliados:
                aliados.remove(tiro_pc)
                print(f'Seu barco foi derrubado na posição {tiro_pc}!')
            else:
                print(f'O Computador atirou na posição {tiro_pc} e errou!')
            tentativas += 1

            if inimigos == []:
                print('Você Ganhou, Parabéns!')
                break
            if tentativas == 20:
                print('Suas tentativas acabaram!')
            if aliados == []:
                print('Todos os seus barcos afundaram!')

            # Fim do jogo
        voltar = input('Deseja voltar ao menu? (s/n): ').strip().lower()
        if voltar != 's':
            print('Saindo...')
            break







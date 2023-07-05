#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador
# vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.

from random import randint
print('=-' * 13)
print('___ ADIVINHA O NÚMERO ___ ')
print('=-' * 13)

# print('Vamos jogar o adivinha ? Qual número acabei de pensar ????')
# computador = randint(0,10)
# jogador = int(input('Digite um valor entre o e 10: '))
# cont = 1
# while jogador != computador:
#     print('NÃO !!!')
#     if computador > jogador:
#         print(' Pense em um número MAIOR !!!')
#     elif computador < jogador:
#         print('Pense em um número MENOR !!!')
#     jogador = int(input('Digite um valor entre o e 10: '))
#     cont += 1
# if jogador == computador:
#     print('Muito bem você adivinhou o número !!!')
#     print(f'Você precisou de {cont} tentativas até acertar !!!')

# SOLUÇÃO GUANABARA --------------------------------------------------------

from random import randint

computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10')
print('Será que vc consegue adivinhar ?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite ?: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador :
            print('Mais ... Tente mais uma vez !!!')
        elif jogador > computador:
            print('Menos... Tente mais uma vez !!!')
print(f'Você acertou com {palpites} tentativas. Parabéns !!!! ')
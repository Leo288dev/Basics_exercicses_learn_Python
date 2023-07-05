#Exercício Python 68: Faça um programa que jogue
# par ou ímpar com o computador. O jogo só será interrompido
# quando o jogador perder, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.

print('=-' * 20)
print('JOGO DO PAR OU ÍMPAR')
print('=-' * 20)
from random import randint
vence = 0

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
     tipo = str(input('Par ou Ímpar? P/I: ')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador {computador}, Total de {total} ', end='')
    print('Deu PAR' if total % 2 == 0 else 'Deu Ímpar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Jogador Vence !!!')
            vence += 1
        else:
            print('Jogador Perdeu !!!')
            break

    elif tipo == 'I':
        if tipo % 2 == 1:
            print('Jogador venceu !!!')
            vence += 1
        else:
            print('Jogador Perdeu !!!')
            break
    print('Vamos jogar novamente ...')
print(f'Você venceu {vence} vezes !!! ')


#Exercício Python 059: Crie um programa que leia dois valores e
# mostre um menu na tela:
#[ 1 ] somar, [ 2 ] multiplicar, [ 3 ] maior, [ 4 ] novos números,
# [ 5 ] sair do programa
from time import sleep

menu = False
primeiro = float(input('Insira o Primeiro valor: '))
segundo = float(input('Iinsira o segundo valor: '))
while menu == False:
    print('[1] SOMAR\n'
          '[2] MULTIPLICAR\n'
          '[3] MAIOR\n'
          '[4]  NOVOS NÚMEROS\n'
          '[5] SAIR')
    opcao = int(input('Digite a operação desejada: '))

    if opcao == 1:
        print('=-' * 10)
        print(f'{primeiro} + {segundo} =', (primeiro + segundo))
        print('=-' * 10)

    elif opcao == 2:
        print('=-' * 10)
        print(f'{primeiro} X {segundo} = ', (primeiro * segundo))
        print('=-' * 10)

    elif opcao == 3:
        print('=-' * 10)
        if primeiro > segundo:
            print(f'O número {primeiro} é maior que o segundo {segundo}')
        elif primeiro < segundo:
            print(f'O número {segundo} é maior que o primeiro {primeiro}')
        else:
            print('Os números tem o mesmo valor !!!')
        print('=-' * 10)

    elif opcao == 4:
        print('=-' * 10)
        primeiro = float(input('Primeiro valor: '))
        segundo = float(input('Segundo valor: '))
        print('=-' * 10)

    elif opcao == 5:
        print('=-' * 10)
        menu = True
        print('FIM DO PROGRAMA !!!')
        print('=-' * 10)

    else:
        print('=-' * 10)
        print('Escolha um número entre 1 e 5 conforme MENU...')
        print('=-' * 10)
    sleep(2)
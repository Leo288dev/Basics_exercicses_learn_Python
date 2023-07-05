# Exercício Python 67: Faça um programa que mostre
# a tabuada de vários números, um de cada vez, para cada
# valor digitado pelo usuário. O programa será interrompido
# quando o número solicitado for negativo.
print('=' * 20)
print('PROGRAMA DE TABUADA')
print('=' * 20)

while True:
    n = int(input('Digite um número [numero negativo encerra]: '))
    print('-' * 20)
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} x {i} = ', (n * i))
    print('-' * 20)
print('PROGRAMA ENCERRADO, volte sempre !!!')

